from requests import get, post, delete, put
print(put("http://127.0.0.1:8080/api/jobs", json={'id': 2, 'team_leader': 2, 'work_size': 1}).text)

