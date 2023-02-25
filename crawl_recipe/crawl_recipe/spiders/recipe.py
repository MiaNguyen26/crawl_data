"""
    Date Created: 2023-02-25
    Date Modified: 2023-02-25
    Author: MiaNguyen
    Description: This file contains the spider for crawling the recipe
    
"""

import scrapy
import numpy as np
import pandas as pd
import json
from tqdm import tqdm 
import time

from crawl_recipe.items import CrawlRecipeItem
# from crawl_recipe.settings import CHROME_DRIVER_PATH


class EsheepRecipeSpider(scrapy.Spider):
    name = 'esheep_recipe'
    allowed_domains = ['esheepkitchen.com']
    start_urls = [
                    'https://www.esheepkitchen.com/category/recipe/',
                    ]
    

    def parse(self, response):
        #loop over all recipe
        for food in response.xpath('//div[@class="grid-header-box"]/h2[@class="grid-title"]/a/@href').getall():
            yield scrapy.Request(food, callback=self.parse_recipe)

        # get the next page
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    
    def parse_recipe(self, response):
        #create an item to store the recipe
        item = CrawlRecipeItem()
        #get the recipe name
        item['r_url'] = str(response.url)
        item['r_name'] = response.css('h1.post-title ::text').get()
        item['r_content'] = ' '.join([item.strip() for item in response.css('div.inner-post-entry ::text').getall() if item.strip()!=''])

        yield item



class SavouryRecipeSpider(scrapy.Spider):
    name = "savoury_recipe"
    allowed_domains = ["www.savourydays.com"]
    start_urls = [
                    "http://www.savourydays.com/muc-luc-mon-an/",
                    # "http://www.savourydays.com/cach-lam-bunrt-cheesecake-mem-chay/",
                ]


    def parse(self, response):
        #loop over all kind of food
        for food in response.xpath('//h3[@class="entry-title"]/a/@href').getall():
            yield scrapy.Request(food, callback=self.parse_food)
    

    def parse_food(self, response):
        #loop over all recipe of the food
        for food in tqdm(response.xpath('//h3[@class="entry-title"]/a/@href').getall()):
            yield scrapy.Request(food, callback=self.parse_recipe)

        # get the next page
        next_page = response.xpath('//div[@class="pagination woo-pagination"]/a[@class="next page-numbers"]/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse_food)


    def parse_recipe(self, response):
        #create an item to store the recipe
        item = CrawlRecipeItem()
        #get the recipe name
        a = str(response.url)
        # print('ma======', a)

        item['r_url'] = a
        item['r_name'] = response.css('div.recipe-info-single > h1.fn::text').get()
        item['r_content'] = ' '.join([line.strip() for line in response.css('div.boxinc > p ::text').getall()])

        yield item


        
