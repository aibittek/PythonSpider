import scrapy
from recruit.items import RecruitItem
import re

class Job51Spider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['jobs.51job.com']
    start_urls = ['https://jobs.51job.com/all/p1']

    def parse(self, response):
        print(response.url)
        url = response.url.split('/')
        city = url[len(url) - 3]
        page = url[len(url) - 2]
        new_page = re.findall(r'\d+',page)[0]
        urls = response.xpath('.//div[@class="detlist gbox"]/div/p/span/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_info)
        pages = response.xpath('.//div[@class="p_in"]/span[@class="td"]/text()').get()
        pagenum = re.findall(r'\d+',pages)[0]
        if int(new_page) < int(pagenum):
            new_page = int(new_page) + 1
            new_url = "https://jobs.51job.com/" + city + "/p" + str(new_page) + "/"
            yield scrapy.Request(new_url, callback=self.parse)


    def parse_info(self, response):
        # print(response.url)
        pass
        item = RecruitItem()
        #职位名称
        item['title'] = response.xpath('//div[@class="in"]/div/h1/@title').get()
        #公司名称
        item['company'] = response.xpath('//div[@class="in"]/div/p/a[@class="catn"]/@title').get()

        #获取公司信息
        company = self.getPerAndCatAndDo(response)
        #公司类别
        item['companycategory'] = company[0]
        #公司的人数
        item['companyperson'] = company[1]
        #公司主要做什么的
        item['companydo'] = company[2]
        #薪水
        salary= response.xpath('//div[@class="tHeader tHjob"]/div/div/strong/text()').get()
        if salary is not None:
            item['salary'] = salary
        else:
            item['salary'] = ""
        #工作地址
        address = response.xpath('//div[@class="tBorderTop_box"]/div[@class="bmsg inbox"]/p/text()').get()
        if address is not None:
            item['address'] = address
        else:
            item['address'] = ''
        #获取招聘信息
        recruit = self.getRequestInfo(response)
        #工作地点
        item['location'] = recruit[0]
        #工作经验
        item['experience'] = recruit[1]
        #学历要求
        item['request'] = recruit[2]
        #招聘人数
        item['person'] = recruit[3]
        #发布时间
        item['data'] = recruit[4]
        print(item)
        yield item
    def getPerAndCatAndDo(self,response):
        result = response.xpath('//div[@class="tBorderTop_box"]/div[@class="com_tag"]/p/@title').extract()
        if len(result) <= 2:
            companycategory = result[0]
            companydo = result[1]
        elif len(result) == 3:
            companycategory = result[0]
            companyperson = re.findall(r'\d+',result[1])[0]
            companydo = result[2]
        else:
            companycategory = result[0]
            companyperson = ''
            companydo = ''
        return [companycategory,companyperson,companydo]
    def getRequestInfo(self,response):
        result = response.xpath('//div[@class="in"]/div/p[@class="msg ltype"]/text()').getall()
        # result = result.replace(r'\xa0',"")
        if len(result) >= 5:
            location = result[0].replace(u'\xa0', u'')
            experience = result[1].replace(u'\xa0', u'')
            request = result[2].replace(u'\xa0', u'')
            person = result[3].replace(u'\xa0', u'')
            data = result[4].replace(u'\xa0', u'')
        elif len(result) == 4:
            location = result[0].replace(u'\xa0', u'')
            experience = result[1].replace(u'\xa0', u'')
            request = ''
            person = result[2].replace(u'\xa0', u'')
            data = result[3].replace(u'\xa0', u'')
        return [location,experience,request,person,data]
