import requests
import json
import os
from datetime import datetime

now = datetime.now()
minute_plus_one = now.minute + 1
url = f"https://jsonplaceholder.typicode.com/todos/{minute_plus_one}"

response = requests.get(url)
new_data = response.json()

file_path = "data/seokbeen_test.json"

data_list = []
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data_list = json.load(f)
            if not isinstance(data_list, list):
                data_list = [data_list]
        except json.JSONDecodeError:
            data_list = []

data_list.append(new_data)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4, ensure_ascii=False)

print(f"Successfully updated: {url}")