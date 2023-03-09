from requests import get, post, delete, put

print(get("http://127.0.0.1:8080/api/jobs").text)
print(put("http://127.0.0.1:8080/api/jobs", json={'id': 2, 'team_leader': '9', 'work_size': 9}).text)
print(get("http://127.0.0.1:8080/api/jobs").text)
print(put("http://127.0.0.1:8080/api/jobs").text)  # без json фаила
print(put("http://127.0.0.1:8080/api/jobs", json={'team_leader': 1, 'work_size': 9}).text)  # без указания id
print(put("http://127.0.0.1:8080/api/jobs", json={'id': 999, 'team_leader': 1, 'work_size': 9}).text)  # нет id в бд
