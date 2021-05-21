# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    job_name = scrapy.Field()
    money = scrapy.Field()
    name = scrapy.Field()
    tags = scrapy.Field()
    info_desc = scrapy.Field()
    pass
