# coding=utf-8

import requests
import os

# 京东商品页面的爬取
url = "https://item.jd.com/2967929.html"
try :
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except :
    print("爬取失败")

# 网络图片的爬取和存储
url = "https://cdn.jsdelivr.net/gh/aibittek/ImageHost/img/20210406112916.jpeg"
root = ".//"
path = root + "beauty.jpg"
try :
    if not os.path.exists(root) :
        os.mkdir(root)
    if not os.path.exists(path) :
        r = requests.get(url)
        with open(path, "wb") as f :
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else :
        print("文件已存在")
except :
    print("爬取失败")

# IP地址归属地的自动查询
url = "https://m.ip138.com/ip.asp?ip="
try :
    r = requests.get(url+'45.67.223.227')
    print(r)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except :
    print("爬取失败")
