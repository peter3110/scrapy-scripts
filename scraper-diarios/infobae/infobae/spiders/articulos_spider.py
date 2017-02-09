import scrapy
import re
from datetime import date

from articulos.items import *

class QuotesSpider(scrapy.Spider):
    name = 'articulos_spider'
    allowed_domains = [
        'infobae.com.ar'
    ]
    start_urls = [
        
    ]

    def start_requests(self):
        
                

    def parse(self, response, cat):

        pass



