from gendiff.scripts.gendiff import generate_diff

JSON_OLD = 'gendiff/tests/test_data/file1.json'
JSON_NEW = 'gendiff/tests/test_data/file2.json'


def test_gendiff():
    diff = generate_diff(JSON_OLD, JSON_NEW)
    diff_file_path = 'gendiff/tests/test_data/diff.txt'
    with open(diff_file_path) as file:
        result = file.read()
    assert diff == result


if __name__ == "__main__":
    test_gendiff()