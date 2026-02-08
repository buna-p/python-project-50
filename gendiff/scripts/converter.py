import json
import yaml


def json_to_python(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def yaml_to_python(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


def converter(file_path):
    extension_file = file_path.suffix
    if extension_file == '.json':
        data = json_to_python(file_path)
    elif extension_file in ['.yaml', '.yml']:
        data = yaml_to_python(file_path)
    return data