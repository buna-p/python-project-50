from pathlib import Path
from gendiff.scripts.gendiff import generate_diff


def get_path(filename):
    return Path(__file__).parent/'test_data'/filename


def test_gendiff_stylish_json():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    diff = generate_diff(file1, file2, 'stylish')
    diff_file_path = get_path('diff_stylish.txt')
    with open(diff_file_path) as file:
        result = file.read()
    assert diff == result


def test_gendiff_stylish_yaml():
    file1 = get_path('file1.yaml')
    file2 = get_path('file2.yaml')
    diff = generate_diff(file1, file2, 'stylish')
    diff_file_path = get_path('diff_stylish.txt')
    with open(diff_file_path) as file:
        result = file.read()
    assert diff == result


def test_gendiff_plain_json():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    diff = generate_diff(file1, file2, 'plain')
    diff_file_path = get_path('diff_plain.txt')
    with open(diff_file_path) as file:
        result = file.read()
    assert diff == result


def test_gendiff_plain_yaml():
    file1 = get_path('file1.yaml')
    file2 = get_path('file2.yaml')
    diff = generate_diff(file1, file2, 'plain')
    diff_file_path = get_path('diff_plain.txt')
    with open(diff_file_path) as file:
        result = file.read()
    assert diff == result