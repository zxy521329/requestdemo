import requests


s=requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/12345678')

r=s.get("http://httpbin.org/cookies")

print(r.text)