# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname=scrapy.Field()          # 职位
    city=scrapy.Field()             # 城市
    company=scrapy.Field()          # 公司
    salary=scrapy.Field()           # 薪资
    workyear=scrapy.Field()         # 工作经验
    education=scrapy.Field()        # 学历
    companytype=scrapy.Field()      # 公司类型
    companytag=scrapy.Field()       # 公司标签
    companyscale=scrapy.Field()     # 公司规模
    requirements=scrapy.Field()     # 公司技能需求
    welfare=scrapy.Field()          # 公司福利
    pass
