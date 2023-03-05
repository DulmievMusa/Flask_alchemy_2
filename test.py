from requests import get, post

print(post('http://127.0.0.1:8080/api/jobs', json={
    "team_leader": 9,
    "job": 'test_api',
    "work_size": 12,
    "collaborators": '1, 2, 3',
    "is_finished": False}).text)  # корректный

print(post('http://127.0.0.1:8080/api/jobs', json={}).text)  # некорректный так как пустой json
print(post('http://127.0.0.1:8080/api/jobs', json={
    "team_leader": 9,
    "job": 'test_api',
    "work_size": 12,
    "collaborators": '1, 2, 3'}).text)  # некорректный так как не 'is_finished'
print(post('http://127.0.0.1:8080/api/jobs', json={
    "id": 2,
    "team_leader": 9,
    "job": 'test_api',
    "work_size": 12,
    "collaborators": '1, 2, 3',
    "is_finished": False}).text)  # некорректный так как работа с таким id уже есть
