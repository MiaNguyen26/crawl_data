# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlRecipeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    r_url = scrapy.Field()
    r_name = scrapy.Field()
    r_content = scrapy.Field()
    # pass
