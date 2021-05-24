# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class RecruitPipeline:
    def __init__(self):
        # 获取连接
        client = pymongo.MongoClient(host='192.168.56.128', port=27017)
        # 设置数据库
        db = client['recruit']
        #设置集合(表)
        self.col = db['job51']

    def process_item(self, item, spider):
        #写入集合(表)
        self.col.insert(dict(item))
        print('插入成功')
        return item
