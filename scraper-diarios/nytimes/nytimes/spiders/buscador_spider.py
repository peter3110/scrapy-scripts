import scrapy
from scrapy_splash import SplashRequest

import re
import copy
import time
from datetime import date

from nytimes.items import *

class QuotesSpider(scrapy.Spider):
    name = 'buscador_spider'
    allowed_domains = [
        "nytimes.com",
        "query.nytimes.com"
    ]

    search = 'trump'
    waiting_time = 10
    n_pages = 10

    init = 'https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/trump/since1851/allresults/'
    start_urls = [
        init + str(i) + '/' 
        for i in range(1, n_pages)
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield SplashRequest(u, self.parse,
                endpoint='render.html',
                args={'wait': self.waiting_time},
            )

    def parseinner(self, response):
        # Levanto los datos del articulo actual
        day      = date.today()
        category = 'trump'
        title    = response.xpath('//h1[@id="headline"]/text()').extract()
        text     = response.xpath('//p[@class="story-body-text story-content"]/text()').extract()
        
        # Guardo el articulo de la pagina actual
        yield nytimesArticle(date = day, category = category, title = title, text=text)

    def parse(self, response):
        
        # NOTA : dependiendo de distintos intervalos de paginas en la respuesta al query,
        # hay que parsear los links (a href), y los titulos (title) de distinta manera
            #for url in response.xpath('//li[@class="story"]//a/@href').extract():

        for url in response.xpath('//h3//a/@href').extract():
            #print "#### URL ###",url
            yield scrapy.Request(
                url = url,
                callback = lambda r: self.parseinner(r)
            )





          