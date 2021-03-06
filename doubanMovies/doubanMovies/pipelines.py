# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class DoubanmoviesPipeline:
    def process_item(self, item, spider):
        return item
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in [item['image']]:
            ## meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            # yield Request(image_url, meta={'name': item['movieName']})
            yield Request(image_url)

        # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1] # 提取url前面名称作为图片名。
        filename = u'{0}'.format(image_guid)  #保存图片
        return filename
