import requests
# url='http://www.amazon.cn/'
# try:
#    r=requests.get(url)
#    print(r.status_code)
#    r.encoding=r.apparent_encoding
#    print(r.text[:1000])
# except:
#     print('爬取失败 ')
kv={'wd':'python'}
r=requests.get('http://www.baidu.com/s',params=kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))