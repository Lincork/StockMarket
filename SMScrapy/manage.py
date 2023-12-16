import time
from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'api', '-o StockData(%s).csv'%time.time()])


