# -*- coding: utf-8 -*-
import scrapy
#from scrapy import Selector

class ClimatebotSpider(scrapy.Spider):
    name = 'climatebot'
    #allowed_domains = ['http://berkeleyearth.org/data/']
    start_urls = ['http://berkeleyearth.org/data/']

    
    def parse(self, response):
        #print(response.url) // Just to make sure spider is scraping and crawling correct website
        for href in response.xpath('//a[re:test(@href, "Raw_TAVG_complete")]//@href'): # Looking for Raw data for monthly average temperature data 
            url = response.urljoin(href.extract()) #
            yield scrapy.Request(url, callback = self.parse_dir_contents)   # create a request to follow the link from the page
    
    def parse_dir_contents(self,response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving file %s', path)
        with open(path, 'wb') as f:
            f.write(response.body) # Download the link into folder for easy access

    
