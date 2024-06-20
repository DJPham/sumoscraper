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

# import the database class
from database import Database

# import the viz class
from visualizations import Visualization

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

        # initialize the database class
        self.db = Database('sumo_data.db')

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

            rikishi_rank_elements = self.driver.find_elements(By.CSS_SELECTOR, 'table.mdTable3 th a')
            rikishi_name_elements = self.driver.find_elements(By.CSS_SELECTOR, 'table.mdTable3 tbody tr td.mdBr:first-of-type a')
            rikishi_origin_elements = self.driver.find_elements(By.CSS_SELECTOR, 'table.mdTable3 tbody tr td.mdBr:nth-of-type(2) a')
            rikishi_stable_elements = self.driver.find_elements(By.CSS_SELECTOR, 'table.mdTable3 tbody tr td:nth-of-type(3) a')

            # extract the values and put into an array
            rikishi_names = [element.text for element in rikishi_name_elements]
            rikishi_ranks = [element.text for element in rikishi_rank_elements]
            rikishi_origins = [element.text for element in rikishi_origin_elements]
            rikishi_stables = [element.text for element in rikishi_stable_elements]

            for rank, name, origin, stable in zip(rikishi_ranks, rikishi_names, rikishi_origins, rikishi_stables):
                self.log(f"Rank: {rank}, Name: {name}, Origin: {origin}, Stable: {stable}")

                self.db.insert_rikishi(rank, name, origin, stable)

            yield {
                'rikishi_ranking': rikishi_ranks, 
                'rikishi_names': rikishi_names, 
                'rikishi_origin': rikishi_origins, 
                'rikishi_stable': rikishi_stables
                }

    # used to properly close selenium and database connection whenever the spider is closed
    def closed(self, reason):
        self.driver.quit()
        self.db.close()

process = CrawlerProcess()

process.crawl(SumoSpider)

process.start()

db = Database('sumo_data.db')

#db.clear_table()

db.print()
db.close()

viz = Visualization('sumo_data.db')

viz.fetch_data()
viz.plot_origin_distribution()
viz.plot_stable_distribution()
viz.close()