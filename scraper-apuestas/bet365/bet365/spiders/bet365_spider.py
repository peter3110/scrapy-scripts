import scrapy
from scrapy_splash import SplashRequest

import re
from datetime import date

from bet365.items import *

class QuotesSpider(scrapy.Spider):
    name = 'bet365_spider'
    allowed_domains = [
        "bet365.com"
    ]

    start_urls = [
        'https://www.bet365.com/?lng=3&cb=105802124239#/AC/B13/C1/D50/E2/F163/'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        # Levanto los datos del articulo actual
        day     = date.today()
        
        print "###"