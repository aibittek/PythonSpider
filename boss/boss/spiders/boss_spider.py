import scrapy
from boss.items import BossItem

class BossSpiderSpider(scrapy.Spider):
    name = 'boss_spider'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101120100/?query=python&page=1']
    base_url = 'https://www.zhipin.com'
    def parse(self, response):
        job = response.xpath ("//div[@class='job-list']/ul/li")
        for i in job:
            job_name = i.xpath (".//span[@class='job-name']/a/text()").get ()
            print(job_name)
            money = i.xpath (".//span[@class='red']/text()").get ()
            name = i.xpath (".//h3[@class='name']/a/text()").get ()
            tags = i.xpath (".//div[@class='tags']/span/text()").getall ()
            tags = ''.join (tags)
            info_desc = i.xpath (".//div[@class='info-desc']/text()").get ()

            yield BossItem (job_name=job_name, money=money, name=name, tags=tags, info_desc=info_desc)
        # 获取下一页的地址
        page = response.xpath("//div[@class='page']/a[last()]/@href").get()
        next_url = self.base_url + page
        if not next_url:
            print("退出")
            return
        else:
            print ("下一页地址：",next_url)
            yield scrapy.Request (next_url)
