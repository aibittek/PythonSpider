# coding:utf-8

import csv
import requests
from lxml import html
from lxml import etree
from urllib.request import urlopen,Request
import pymysql

# 创建表
# CREATE TABLE `movie` (
#   `id` varchar(50) NOT NULL,
#   `name` varchar(50) NOT NULL,
#   `gener` varchar(50) NOT NULL,
#   `actor` varchar(100) NOT NULL,
#   `release_data` varchar(50) NOT NULL,
#   `rate` float(10,1) NOT NULL,
#   `comment` int NOT NULL,
#   `ranks` int NOT NULL,
#   `country` varchar(50) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

def list_douban_top250():
    db = pymysql.connect(host='45.67.223.227', port=3306, user='root', passwd='123456', db='douban_movie_top250', charset='utf8')
    # 创建数据库游标
    cursor = db.cursor()

    #创建CSV文件，并写入表头信息
    fp = open('movie.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('movie_id','电影名','电影类型','导演演员信息','发行日期','制片国家','评分','评论数','排名'))

    print('正在获取豆瓣TOP250影片信息并存入数据库...')
    index = 1
    page_count = 10
    all_link = []
    for i in range(page_count):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        # 模拟浏览器访问
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",}
        ret = Request(url, headers=headers)
        res = urlopen(ret)
        # 内容节点
        doc = etree.HTML(res.read())
        
        # 获取电影链接作为movie表格id
        url_list=doc.xpath('//div[@class="pic"]/a/@href')
        for url in url_list:
            if 'https://movie.douban.com/subject/' in str(url):
                all_link.append(url)

        for y in doc.xpath('//div[@class="info"]'):
            # 影片名称
            name = y.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
            # 影片详情
            move_content = y.xpath('div[@class="bd"]/p[1]/text()')
            # 导演演员信息
            actor = move_content[0].replace(" ", "").replace("\n", "").replace("\xa0","")
            # 上映日期
            date = move_content[1].replace(" ", "").replace("\n", "").replace("\xa0","").split("/")[0]
            # 制片国家
            country = move_content[1].replace(" ", "").replace("\n", "").replace("\xa0","").split("/")[1]
            # 影片类型
            gener = move_content[1].replace(" ", "").replace("\n", "").replace("\xa0","").split("/")[2]
            # 评分
            rate = y.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
            # 评论人数
            com_count = y.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')[0].replace('人评价', '')

            # 执行log
            print('TOP%s--%s--评分%s--人数%s' % (str(index), name, rate, com_count))
            
            # 写入csv
            writer.writerow((all_link[index-1],name,gener,actor,date,country,rate,com_count,index))

            # 写入MySQL
            sql = "INSERT INTO movie(id,name,gener,actor,release_data,country,rate,comment,ranks) \
            VALUES ('%s','%s','%s','%s','%s','%s','%f','%d','%d')"% \
            (all_link[index-1],str(name),str(gener),str(actor),str(date),str(country),round(float(rate),1),int(com_count),index)
            try:
                cursor.execute(sql)
                db.commit()
                print("结果已提交")
            except pymysql.Error as e:
                db.rollback()
                print("数据已回滚",e)
            index += 1
    print('任务执行完成！')
    cursor.close()
    db.close()
    fp.close()

list_douban_top250()
