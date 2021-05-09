import scrapy
import os
from girls.items import GirlsItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['https://nice.ruyile.com']
    start_urls = ['https://nice.ruyile.com/?f=3&p=' + str(i) for i in range(1, 358)]

    def parse(self, response):
        allPics = response.xpath('//div[@class="tp_a"]/a')
        for pic in allPics:
            item = GirlsItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            item['name'] = name
            item['addr'] = addr
            # 返回爬取到的数据
            yield item
