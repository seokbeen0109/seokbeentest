import requests
import json
import os
from datetime import datetime

now = datetime.now()
minute_plus_one = now.minute + 1
url = f"https://jsonplaceholder.typicode.com/todos/{minute_plus_one}"

try:
    response = requests.get(url)
    response.raise_for_status()
    new_data = response.json()
except Exception as e:
    print(f"데이터 수집 실패: {e}")
    exit(1)

tmp_dir = "/tmp"
file_name = "seokbeen_test.json"
tmp_file_path = os.path.join(tmp_dir, file_name)
repo_file_path = os.path.join("data", file_name)


data_list = []

if os.path.exists(repo_file_path):
    with open(repo_file_path, "r", encoding="utf-8") as f:
        try:
            data_list = json.load(f)
        except json.JSONDecodeError:
            data_list = []


data_list.append(new_data)


if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

with open(tmp_file_path, "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4, ensure_ascii=False)
    print(f"1단계: /tmp/ 에 임시 저장 완료 ({tmp_file_path})")


if not os.path.exists("data"):
    os.makedirs("data")

with open(repo_file_path, "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=4, ensure_ascii=False)
    print(f"2단계: 레포지토리 경로로 데이터 동기화 완료 ({repo_file_path})")

print(f"성공적으로 업데이트된 URL: {url}")
