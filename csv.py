import csv

# 创建CSV文件
f = open('./favorite_movies.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
writer.writerow(('电影名', '得分', '演员', '链接地址'))
writer.writerow(('机器人总动员', 9.3, '瓦力', 'kui.ge'))