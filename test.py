from requests import get, post, delete, put
print(get("http://127.0.0.1:8080/api/v2/users/3").text)
print(get("http://127.0.0.1:8080/api/v2/users").text)
print(delete("http://127.0.0.1:8080/api/v2/users/5").text)
print(get("http://127.0.0.1:8080/api/v2/users").text)
print(get("http://127.0.0.1:8080/api/v2/users/5").text)  # нет id
print(post("http://127.0.0.1:8080/api/v2/users", json={
    'surname': 'gogl',
    'name': 'mogl',
    'age': 121,
    'position': 'gnom',
    'speciality': 'gnom',
    'address': '3/9 kingdom',
    'email': 'g@nom'
}).text)
print(post("http://127.0.0.1:8080/api/v2/users", json={
    'surname': 'gogl',
    'name': 'mogl',
    'age': 121,
    'position': 'gnom',
    'speciality': 'gnom'
}).text)  # без address

