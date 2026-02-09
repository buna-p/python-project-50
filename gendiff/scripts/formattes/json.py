import json

def to_json(data: dict) -> str:
    result = json.dumps(data, indent=2)
    return result