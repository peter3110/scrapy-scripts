import scrapy
from scrapy_splash import SplashRequest

import re
from datetime import date

from nytimes.items import *

class QuotesSpider(scrapy.Spider):
    name = 'buscador_spider'
    allowed_domains = [
        "nytimes.com",
        "query.nytimes.com"
    ]


    start_urls = [
        'https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/trump/since1851/allresults/1/',
        'https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/trump/since1851/allresults/2/',
    ]

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )
        yield SplashRequest(self.start_urls[1], self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        # Levanto los datos del articulo actual
        day     = date.today()
        category = 'busqueda Trump'
        title    = response.xpath('//h1[@id="headline"]').extract()
        text     = 'texto' #response.xpath('//p').extract()
        
        # Guardo el articulo de la pagina actual
        yield nytimesArticle(date = day, category = category, title = title, text=text)
        
        # TODO: terminar esto!!!
        for url in response.xpath('//li[@class="story"]//a/@href').extract():
            print "######",url





          