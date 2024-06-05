# import the Scrapy library which will be used to scrape the data
import scrapy
from scrapy.crawler import CrawlerProcess

class SumoSpider(scrapy.Spider):
    name = 'sumo_spider'

    def start_requests(self):
        urls = ['https://www.sumo.or.jp/En/']

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        pass

process = CrawlerProcess()

process.crawl(SumoSpider)

process.start()