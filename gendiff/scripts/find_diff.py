def find_diff(data1: dict, data2: dict) -> list:
    diff = []
    keys = sorted(set(data1.keys() | data2.keys()))

    for key in keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff.append({
                        'key': key,
                        'operation': '[complex value]',
                        'childrens': find_diff(data1[key], data2[key])
                    })
            elif data1[key] == data2[key]:
                diff.append({
                    'key': key,
                    'operation': 'not changed',
                    'value': data1[key]
                })
            else:
                diff.append({
                    'key': key,
                    'operation': 'updated',
                    'value old': data1[key],
                    'value new': data2[key],
                })
        elif key in data1:
            diff.append({
                    'key': key,
                    'operation': 'removed',
                    'value': data1[key]
                })
        else:
            diff.append({
                    'key': key,
                    'operation': 'added',
                    'value': data2[key]
                })
    return diff