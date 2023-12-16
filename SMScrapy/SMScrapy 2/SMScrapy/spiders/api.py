import json
import scrapy
import pandas as pd
from dateutil.parser import parse
from ..items import SmscrapyItem

class APISpider(scrapy.Spider):
    instruments = pd.read_csv("Stock.csv")["Identifier"].to_list()#[:2]
    print(instruments)
    shanghai = []
    shenzhen = []
    name = 'api'
    allowed_domains = ['yunhq.sse.com.cn','www.szse.cn']
    start_urls = []
    for instrument in instruments:
        SE = instrument.split(".")[1]
        if SE == "SS":
            instrument = instrument.split(".")[0]
            api = f"https://yunhq.sse.com.cn:32042/v1/sh1/snap/{instrument}?&select=name%2Cprev_close%2Copen%2Chigh%2Clow%2Clast%2Cchange%2Cchg_rate%2Cvolume%2Camount%2Ccpxxlmttype%2Cup_limit%2Cdown_limit%2Ctradephase%2Cbid%2Cask%2Chlt_tag%2Cgdr_ratio%2Cgdr_prevpx%2Cgdr_currency%2Ccpxxprodusta%2Cfp_volume%2Cfp_amount%2Cfp_phase%2Ccpxxextendname&_=1699236673494"
            start_urls.append(api)
            shanghai.append(instrument)
        if SE == "SZ":
            instrument = instrument.split(".")[0]
            api = f"https://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.2024269370830547&marketId=1&code={instrument}"
            start_urls.append(api)
            shenzhen.append(instrument)

    def parse(self, response):
        result = json.loads(response.text)

        if result['code'] in self.shanghai:
            item = SmscrapyItem()
            item['code'] = "%s.SS"%result['code']
            item['name'] = result['snap'][0]
            item['time'] = parse(f"{result['date']}{result['time']}").strftime("%Y-%m-%d %H:%M:%S")
            item['last_close'] = result['snap'][1]
            item['today_open'] = result['snap'][2]
            item['today_max'] = result['snap'][3]
            item['today_min'] = result['snap'][4]
            item['today_now'] = result['snap'][5]
            item['delta_amount'] = result['snap'][6]
            item['delta_percentage'] = result['snap'][7]
            item['volume_times'] = result['snap'][8]
            item['volume_amount'] = result['snap'][9]
            item['arise_amount'] = item['today_open'] - item['last_close']
            item['arise_percentage'] = item['arise_amount'] / item['last_close']
            yield item

        elif result['data']['code'] in self.shenzhen:
            item = SmscrapyItem()
            item['code'] = "%s.SZ"%result['data']['code']
            item['name'] = result['data']["name"]
            item['time'] = result['datetime']
            item['last_close'] = result['data']['close']
            item['today_open'] = result['data']['open']
            item['today_max'] = result['data']['high']
            item['today_min'] = result['data']['low']
            item['today_now'] = result['data']['now']
            item['delta_amount'] = result['data']["delta"]
            item['delta_percentage'] = result['data']["deltaPercent"]
            item['volume_times'] = result['data']['volume']
            item['volume_amount'] = result['data']['amount']
            item['arise_amount'] = float(item['today_open']) - float(item['last_close'])
            item['arise_percentage'] = float(item['arise_amount']) / float(item['last_close'])
            yield item