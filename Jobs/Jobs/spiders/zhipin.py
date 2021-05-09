import scrapy


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['https://www.zhipin.com']
    start_urls = [r'https://www.zhipin.com/c100010000/?query=网络爬虫&page=1&ka=page-1']

    def parse(self, response):
        item = BOSSItem()
        job = response.css('.info-primary h1:nth-child(1)::text').extract()[0]
        company_name = response.css('.job-sec.prop-item+div h3+div::text').extract()[0]
        salary = response.css('.info-primary span.salary::text').extract()[0]
        salary = str(re.search(".*?(\d+.*\d)",salary).group(1)).strip().replace('-',',')
        location = response.css('.info-primary>p::text').extract()[0]
        experience = response.css('.info-primary>p::text').extract()[1]
        edu = response.css('.info-primary>p::text').extract()[2]
        job_content = response.css('.detail-content div:nth-child(2)::text').extract()[1]
        job_requirement =response.css('.detail-content div:nth-child(2)::text').extract()[3]
        com_num = response.css('.sider-company p:nth-child(4)::text').extract()[0]
        com_type = response.css('a[ka="job-detail-brandindustry"]::text').extract()[0]
        com_level = response.css('.sider-company p:nth-child(3)::text').extract()[0]

        item['job'] = job
        item['company_name'] = company_name
        item['salary'] = salary
        item['location'] = location
        item['experience'] = experience
        item['edu'] = edu
        item['job_content'] = job_content
        item['job_requirement'] = job_requirement
        item['com_num'] = com_num
        item['com_type'] = com_type
        item['com_level'] = com_level
        yield item
