from requests import get, post, delete


print(get("http://127.0.0.1:8080/api/jobs").text)
print(delete("http://127.0.0.1:8080/api/jobs/5").text)
print(get("http://127.0.0.1:8080/api/jobs").text)
print(delete("http://127.0.0.1:8080/api/jobs").text)  # запрос без указания id
print(delete("http://127.0.0.1:8080/api/jobs/999").text)  # id нет в базе данных
print(delete("http://127.0.0.1:8080/api/jobs/q").text)  # в качестве id передана строка




