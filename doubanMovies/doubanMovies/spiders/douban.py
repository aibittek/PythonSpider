import scrapy
from doubanMovies.items import doubanMovies
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250?start='+str(i*25) for i in range(1)]
    def parse(self, response):
        for row in response.xpath('//*[@id="content"]/div/div[1]/ol/li'):  # 获取所有li
            url = row.xpath("div/div[1]/a/@href").extract_first()
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = doubanMovies()  # 实例化

       #item["movieName"] = response.xpath('//*[@id="content"]/h1/span[1]/text()').get()  # 获取电影名称
        #item["Screenwriter"] = response.xpath('string(//*[@id="info"]/span[2]/span[2])').get()  # 编剧
        item["image"] = response.xpath('//*[@id="mainpic"]/a/img/@src').get()  # 获取影片海报图片
        yield item