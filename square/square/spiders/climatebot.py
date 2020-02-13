# -*- coding: utf-8 -*-
import scrapy


class ClimatebotSpider(scrapy.Spider):
    name = 'climatebot'
    #allowed_domains = ['http://berkeleyearth.org/data/']
    start_urls = ['http://berkeleyearth.org/data/']

    def parse(self, response):
        #pass
        print(response.url)
        # Get all the <a> tags
        a_selectors = response.xpath("//a")
        # Loop on each tag
        for selector in a_selectors:
            # Extract the link text
            text = selector.xpath("text()").extract_first()
            # Extract the link href
            link = selector.xpath("@href").extract_first()
            # Create a new Request object
            request = response.follow(link, callback=self.parse)
            # Return it thanks to a generator
            yield request