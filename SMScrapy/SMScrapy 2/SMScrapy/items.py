# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SmscrapyItem(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    last_close = scrapy.Field()
    today_open = scrapy.Field()
    today_max = scrapy.Field()
    today_min = scrapy.Field()
    today_now = scrapy.Field()
    delta_amount = scrapy.Field()
    delta_percentage = scrapy.Field()
    volume_times = scrapy.Field()
    volume_amount = scrapy.Field()
    arise_amount = scrapy.Field()
    arise_percentage = scrapy.Field()

