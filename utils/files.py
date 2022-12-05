import json
import os

from conftest import root_dir


def read_json(filename: str) -> dict:
    file_path = os.path.join(root_dir, 'resources', 'data', filename)
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.loads(json_file.read())
