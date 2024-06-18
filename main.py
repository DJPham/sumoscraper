# scrapy will be used for HTML scraping
import scrapy
from scrapy.crawler import CrawlerProcess

# using selenium for JavaScript scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

# needed to help with selenium processes
# automates the process instead of needing to manually set things up
from webdriver_manager.chrome import ChromeDriverManager

import time

class SumoSpider(scrapy.Spider):
    name = 'sumo_spider'
    # the spider will start scraping from the home page
    start_urls = ['https://www.sumo.or.jp/En/']

    # the *args and **kwargs allows a variable # of arguments, for flexibility
    def __init__(self, *args, **kwargs):
        # initialize the parent class, scrapy.Spider, super() returns a temp object to call its methods
        super(SumoSpider, self).__init__(*args, **kwargs)

        # initialize the Chrome Webdriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def parse(self, response):
        # it will try and find the "Find Rikishi" link
        link = response.css('div.aboutSumo > a[href*="EnSumoDataRikishi/search"]::attr(href)').get()

        # if the link is valid, return the results 
        if link:
            # selenium's webdriver navigates to the full URL
            # will also open up a Chrome window of the link
            self.driver.get(response.urljoin(link))

            # give time for the JS to load
            # could swap with WebDriverWait for more precise control
            time.sleep(5)

            # using selenium's functions to drive down to the specific code
            # returns the names of every sumo wrestler in Makuuchi division
            rikishi_elements = self.driver.find_elements(By.CSS_SELECTOR, 'table.mdTable3 tbody tr td.mdBr:first-of-type a')

            # extract the values and put into an array
            rikishi_names = [element.text for element in rikishi_elements]

            for name in rikishi_names:
                self.log(name)

            yield {'rikishi_names': rikishi_names}

    # used to properly close selenium whenever the spider is closed
    def closed(self, reason):
        self.driver.quit()

process = CrawlerProcess()

process.crawl(SumoSpider)

process.start()