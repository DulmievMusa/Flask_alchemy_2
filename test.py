from requests import get, post, delete, put
print(get("http://127.0.0.1:8080/api/v2/jobs").text)
print(put("http://127.0.0.1:8080/api/v2/jobs/9", json={
    'team_leader': 9,
    'job': 'mogl gogl',
    'work_size': 121,
    'collaborators': '2, 3',
    'is_finished': False,
}).content)
print(get("http://127.0.0.1:8080/api/v2/jobs").text)
print(post("http://127.0.0.1:8080/api/v2/jobs", json={
    'team_leader': 9,
    'job': 'mogl gogl',
    'work_size': 121,
    'collaborators': '2, 3',
    'is_finished': False,
}).content)
print(delete("http://127.0.0.1:8080/api/v2/jobs/99").content)  # не существует id
print(delete("http://127.0.0.1:8080/api/v2/jobs/q").content)  # id - строка
print(post("http://127.0.0.1:8080/api/v2/jobs", json={
    'team_leader': 9,
    'job': 'mogl gogl',
    'work_size': 121,
    'collaborators': '2, 3',
}).content)  # без поля is_finished
print(put("http://127.0.0.1:8080/api/v2/jobs/9", json={
    'team_leader': 9,
    'job': 'mogl gogl',
    'work_size': 121,
    'collaborators': '2, 3',
}).content)  # без поля is_finished
print(put("http://127.0.0.1:8080/api/v2/jobs/9", json={
    'team_leader': 9,
    'job': 1234567,
    'work_size': 121,
    'collaborators': '2, 3',
    'is_finished': False,
}).content)  # в поле job передаётся число, а не строка


