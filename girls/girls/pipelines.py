# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import os

class GirlsPipeline:
    def process_item(self, item, spider):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        res = requests.get(item['addr'], headers=headers)
        file_name = os.path.join(r'E:\imgs',item['name']+'.jpg')
        print(res, file_name)
        with open(file_name,'wb') as fp:
            fp.write(res.content)
        return item
