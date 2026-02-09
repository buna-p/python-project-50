from gendiff.scripts.converter import converter
from gendiff.scripts.find_diff import find_diff
from gendiff.scripts.formattes.json import to_json
from gendiff.scripts.formattes.plain import plain
from gendiff.scripts.formattes.stylish import stylish


def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:  # noqa: E501
    data1 = converter(file_path1)
    data2 = converter(file_path2)
    diff = find_diff(data1, data2)
    match format_name:
        case 'stylish':
            formated_diff = stylish(diff)
        case 'plain':
            formated_diff = plain(diff)
        case 'to_json':
            formated_diff = to_json(diff)
    return formated_diff