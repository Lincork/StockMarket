# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd
from sqlalchemy import create_engine
from itemadapter import ItemAdapter
# import mysql.connector

class SmscrapyPipeline:
    def __init__(self):
        pass

    # @classmethod
    # def open_spider(self, spider):
    #     self.result = pd.DataFrame()

    # def process_item(self, item, spider):
    #     self.pditem = pd.DataFrame(item)
    #     self.result = pd.concat([self.result, self.pditem], axis=0)
    #     return item
    
    # def close_spider(self, spider):
    #     print("result:")
    #     print(self.result)
    #     self.result.to_excel("result.xlsx")


    # def __init__(self, db_config):
    #     self.db_config = db_config

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler.settings.getdict("MYSQL_CONFIG"))

    # def open_spider(self, spider):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         port = 3306,
    #         user = 'root',
    #         password = 'CHENxz0817',
    #         db = 'china.highfrequence'
    #         )
    #     self.cursor = self.conn.cursor()

    # def close_spider(self, spider):
    #     self.conn.commit()
    #     self.cursor.close()
    #     self.conn.close()

    # def process_item(self, item, spider):
    #     values = (
    #         item['code'],
    #         item['name'],
    #         item['time'],
    #         item['last_close'],
    #         item['today_open'],
    #         item['today_max'],
    #         item['today_min'],
    #         item['today_now'],
    #         item['delta_amount'],
    #         item['delta_percentage'],
    #         item['volume_times'],
    #         item['volume_amount'],
    #         item['arise_amount'],
    #         item['arise_percentage']
    #     )
    #     sql = "INSERT INTO articles (code, name, time, last_close, today_open, today_max, today_min, today_now, delta_amount, delta_percentage, volume_times, volume_amount, arise_amount, arise_percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     self.cursor.execute(sql, values)
    #     return item


