def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value == '':
        return "''"
    elif value is None:
        return 'null'
    return f"'{value}'"


def plain(diff: dict, path='') -> str:
    result = []
    for data in diff:
        operation = data['operation']
        property_path = f'{path}{data['key']}'
        if operation == 'added':
            result.append(
                f"Property '{property_path}' was {operation} with value: {
                    format_value(data['value'])
                    }"
                )
        elif operation == 'removed':
            result.append(f"Property '{property_path}' was {operation}")
        elif operation == 'updated':
            result.append(
                f"Property '{property_path}' was {operation}. From {
                    format_value(data['value old'])
                    } to {
                        format_value(data['value new'])
                        }"
                )
        elif operation == '[complex value]':
            result.append(plain(data['childrens'], property_path + '.'))
    return '\n'.join(result)