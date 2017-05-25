#encoding：utf8

import requests

req = requests.get(url='http://www.baidu.com') # 最基本的GEt请求

print (req.status_code) #获取状态码

r=requests.get(url='http://dict.baidu.com/s',params={'wd':'python'}) #带参数的get请求

print (r.url)#打印请求URL
#print(r.text) #打印返回数据


r1=requests.post(url='http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例
print (r1.url)#打印请求URL
print (r1.status_code) #获取状态码


import json
r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())
data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)