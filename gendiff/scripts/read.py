import json

def json_to_python(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data
