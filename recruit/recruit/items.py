# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitItem(scrapy.Item):
    #职位名称
    title = scrapy.Field()
    #公司名称
    company = scrapy.Field()
    #公司的人数
    companyperson = scrapy.Field()
    #公司类别
    companycategory = scrapy.Field()
    #公司主要做什么的
    companydo = scrapy.Field()
    #工作地点
    location = scrapy.Field()
    #工作地址
    address = scrapy.Field()
    #薪水
    salary = scrapy.Field()
    #招聘人数
    person = scrapy.Field()
    #发布时间
    data = scrapy.Field()
    #学历要求
    request = scrapy.Field()
    #工作经验
    experience = scrapy.Field()
