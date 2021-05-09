# coding=utf-8

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': 'll="118220"; bid=moeyEWqiUeI; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1615726386%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; push_noty_num=0; push_doumail_num=0; __yadk_uid=EV8br1Vpw4ohEooxn3lX0m3sU8Hk5prf; __utmv=30149280.14616; __gads=ID=ec7d24c7d3e9324d-22411b916bc60071:T=1615727710:RT=1615727710:S=ALNI_MZyjYGOmWYx-50ugCz62rL4xKyL2g; _pk_id.100001.8cb4=02e15f49fe8fbc7e.1615726386.1.1615728157.1615726386.; __utmz=30149280.1616376130.6.6.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1620106219.1615699905.1616329977.1616376130.6; douban-fav-remind=1; dbcl2="146164910:XUTQGYHXpOs"; ck=HvO0; ap_v=0,6.0'}
url = 'https://www.douban.com/'

# 使用cookie登录
r = requests.get(url, cookies = cookies, headers = headers)

# 上面已经登录了,下面继续登录首页,看看我们是否登录了
session = requests.session()
html = session.get(url, cookies = cookies, headers = headers).text
# L的账号是我的豆瓣昵称,登录之后会显示出来
if "L的帐号" in html:
    print("已经登录")
else:
    print("未登录")
with open('douban.txt', 'wb+') as f:
    f.write(str.encode(html)) #把登陆主页后返回的数据保存到文件中