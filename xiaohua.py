import requests
import json
import time
import csv

 # 创建CSV文件
fp = open('xiaohua.csv','w',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('名称', '学校', '链接'))

# 访问前三页，每页显示20
for a in range(3):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(a*20)
    r = requests.get(url, headers=headers)
    file = r.json()   #这里跟之前的不一样，因为返回的是 json 文件
    time.sleep(2)
	# 显示20行的电影名，得分，演员，链接地址
    for i in range(20):
        dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
        urlname=dict['url']
        title=dict['title']
        rate=dict['rate']
        cast=dict['casts']
    
        result = '{},{},{},{}\n'.format(title,rate,'  '.join(cast),urlname)
        print(result)

        # 写入CSV文件,  使用' '.json(cast)把多名演员名字用空格分开
        writer.writerow((title, rate, '  '.join(cast), urlname))
