from scrapy import cmdline

cmdline.execute('scrapy crawl boss_spider -o boss.csv'.split())