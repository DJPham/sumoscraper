# import the Scrapy library which will be used to scrape the data
import scrapy
from scrapy.crawler import CrawlerProcess

class SumoSpider(scrapy.Spider):
    name = 'sumo_spider'
    # the spider will start scraping from the home page
    start_urls = ['https://www.sumo.or.jp/En/']

    def parse(self, response):
        # it will try and find the "Find Rikishi" link
        link = response.css('div.aboutSumo > a[href*="EnSumoDataRikishi/search"]::attr(href)').get()

        # if the link is valid, return the results 
        if link:
            yield response.follow(link, self.parse_rikishi)

    def parse_rikishi(self, response):
        self.log(response.text)

process = CrawlerProcess()

process.crawl(SumoSpider)

process.start()