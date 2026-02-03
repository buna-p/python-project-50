def find_diff(data1: dict, data2: dict) -> str:
    diff = []
    keys = sorted(set(data1.keys() | data2.keys()))

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f'  {key}: {data1[key]}')
            else:
                diff.append(f'- {key}: {data1[key]}')
                diff.append(f'+ {key}: {data2[key]}')
        elif key in data1:
            diff.append(f'- {key}: {data1[key]}')
        else:
            diff.append(f'+ {key}: {data2[key]}')
    return '\n'.join(diff)