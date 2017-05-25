#encoding:utf8
import requests

URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
try:
    r = requests.get(URL, params={'ip': '110.8.8.8'}, timeout=1)
    r.raise_for_status()    # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)
else:
    result = r.json()

    print(type(result), result, sep=' ')

from requests.auth import HTTPBasicAuth

r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
# r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
print(r.json())