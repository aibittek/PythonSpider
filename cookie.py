import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
cookies = {'cookie': '_ga=GA1.1.1872883470.1616029142; __utma=111872281.1872883470.1616029142.1619662301.1619662301.1; __utmz=111872281.1619662301.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_noty_num=0; push_doumail_num=0; _xsrf=2|1a821775|9a4310398c79f129d4d7ac8cc2903390|1620349509; username-localhost-8889="2|1:0|10:1620354637|23:username-localhost-8889|44:M2Y4NDAyODljZmM4NDU2NDliYmIxOTNjYjBiOWMxNjA=|ada1124d014c258513711a263199ad6124e039dedf6e3cf1e05b147f7a8d003d"; username-localhost-8888="2|1:0|10:1620523611|23:username-localhost-8888|44:YTNkOWMwOWVmZTcyNGI4MmI4ZmUzZjUwZjY1OWYwMDM=|21ba06cdcee2b5e7fc569362684448e471ee117ee3c29478886267acf38f8d2a"'}
url = 'http://localhost:8888/tree'
# 使用cookie登录
r = requests.get(url, cookies = cookies, headers = headers)

#把登陆主页后返回的数据保存到文件中
with open('jupyter_home.html', 'wb+') as f:
    f.write(str.encode(r.text, encoding='utf-8'))