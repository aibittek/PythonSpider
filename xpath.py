import urllib.request
import bs4

# 打开网页
res = urllib.request.urlopen("file:///E:/Source/python/tacotronv2_wavernn_chinese/link.html")

# 建立一个BeautifulSoup解析器
soup = bs4.BeautifulSoup(res,"html.parser")

# 查找元素
div = soup.find(attrs={'class':'m_list'})
alist = div.findAll('a')
for a in alist:
    print(a.text)