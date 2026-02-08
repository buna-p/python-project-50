from .argparser import parse_arguments
from gendiff.scripts.find_diff import find_diff
from gendiff.scripts.converter import converter
from gendiff.scripts.formattes.stylish import stylish
from gendiff.scripts.formattes.plain import plain

def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:
    data1 = converter(file_path1)
    data2 = converter(file_path2)
    diff = find_diff(data1, data2)
    if format_name == 'stylish':
        formated_diff = stylish(diff)
    elif format_name == 'plain':
        formated_diff = plain(diff)
    return formated_diff


def main():
    parse_arguments()
    generate_diff()


if __name__ == "__main__":
    main()