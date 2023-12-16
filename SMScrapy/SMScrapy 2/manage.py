import time
from scrapy import cmdline

# scrapy crawl api -o StockData(1116).csv
cmdline.execute(['scrapy', 'crawl', 'api', '-o StockData(%s).csv'%time.time()])
