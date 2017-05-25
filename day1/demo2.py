#encoding:utf8
import requests

r=requests.get('http://www.baidu.com')#发送请求

print (r.status_code)

print(r.headers['content-type'])

print(r.text)

print(r.content)
print(r.encoding)
payload = {'wd': '张亚楠', 'rn': '100'}
r = requests.get("http://www.baidu.com/s", params=payload)
print (r.url)

r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
print(r.json()['data']['country'])

print(r.request.headers)



