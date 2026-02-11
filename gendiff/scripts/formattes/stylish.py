INDENT = 4
SHIFT = 2


def format_value(value, depth) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        result = ['{']
        indent = ' ' * INDENT * (depth + 1)
        for k, v in value.items():
            result.append(f'{indent}{k}: {format_value(v, depth + 1)}')
        result.append(f'{(' ' * INDENT * depth)}}}')
        return '\n'.join(result)
    elif value == '':
        return ''
    elif value == 0:
        return 0
    elif value is None:
        return 'null'
    else:
        return value


def stylish(diff: dict, depth=1) -> str:
    indent = ' ' * INDENT * depth
    indent_with_shift = ' ' * (INDENT * depth - SHIFT)
    result = ['{']
    for data in diff:
        if 'childrens' in data:
            childrens = stylish(data['childrens'], depth + 1)
            result.append(f'{indent}{data['key']}: {childrens}')
        elif data['operation'] == 'not changed':
            result.append(
                f'{indent}{data['key']}: {
                    format_value(data['value'], depth)
                    }'
                )
        elif data['operation'] == 'updated':
            result.append(
                f'{indent_with_shift}- {data['key']}: {
                    format_value(data['value old'], depth)
                    }'
                )
            result.append(
                f'{indent_with_shift}+ {data['key']}: {
                    format_value(data['value new'], depth)
                    }'
                )
        elif data['operation'] == 'removed':
            result.append(
                f'{indent_with_shift}- {data['key']}: {
                    format_value(data['value'], depth)
                    }'
                )
        else:
            result.append(
                f'{indent_with_shift}+ {data['key']}: {
                    format_value(data['value'], depth)
                    }'
                )
    result.append(f'{(' ' * INDENT * (depth - 1))}}}')
    return '\n'.join(result)