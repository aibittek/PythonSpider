import time
import requests
import urllib.request
from bs4 import BeautifulSoup

# 该函数用于下载图片
# 传入函数： 网页的网址url
def download_picture(url):

    # 获取网页的源代码
    r = requests.get(url)
    # 利用BeautifulSoup将获取到的文本解析成HTML
    soup = BeautifulSoup(r.text, "lxml")
    # 获取网页中的电影图片
    content = soup.find('div', class_='article')
    if content is None:
        print('content is null')
        return 
    images = content.find_all('img')
    # 获取电影图片的名称和下载地址
    picture_name_list = [image['alt'] for image in images]
    picture_link_list = [image['src'] for image in images]

    # 利用urllib.request..urlretrieve正式下载图片
    for picture_name, picture_link in zip(picture_name_list, picture_link_list):
        urllib.request.urlretrieve(picture_link, './douban/%s.jpg' % picture_name)


def main():

    # 全部10个网页
    start_urls = ["https://movie.douban.com/top250"]
    for i in range(1, 10):
        start_urls.append("https://movie.douban.com/top250?start=%d&filter=" % (25 * i))

    # 统计该爬虫的消耗时间
    t1 = time.time()
    print('*' * 50)

    for url in start_urls:
        download_picture(url)
    t2 = time.time()

    print('不使用多线程，总共耗时：%s'%(t2-t1))
    print('*' * 50)

main()