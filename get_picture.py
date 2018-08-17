import requests
path='D:/abc.jpg'
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534502904862&di=7465e679ebad2108cfeaf1e61e4e0372&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0117e2571b8b246ac72538120dd8a4.jpg%401280w_1l_2o_100sh.jpg'
r=requests.get(url)
print(r.status_code)
with open(path,'wb')as f:
    f.write(r.content)
    f.close()