from .argparser import parse_args
from .read import json_to_python
from .find_diff import find_diff


def generate_diff(file_path1, file_path2) -> str:
    data1 = json_to_python(file_path1)
    data2 = json_to_python(file_path2)
    diff = find_diff(data1, data2)
    return diff

def main():
    parse_args()


if __name__ == "__main__":
    main()