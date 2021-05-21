import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mycwpjt.items import MycwpjtItem

class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MycwpjtItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # 根据Xpath表达式提取新闻网页中的标题
        item["name"] = response.xpath("/html/head/title/text()").extract()
        # 根据Xpath表达式提取当前新闻网页的链接
        item["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        return item
