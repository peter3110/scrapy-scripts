import scrapy
from tutorial.items import *

class QuotesSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = [
        'lanacion.com.ar'
    ]

    def start_requests(self):
        yield scrapy.Request('http://www.lanacion.com.ar/comunidad-de-negocios', self.parse)

    def parse(self, response):

        elem = response.xpath('//title').extract()
        print 'Titulo nuevo: ', elem

        elem += response.xpath('//p[@class="primero"]').extract()
        print 'Parrafo nuevo: ', elem
        
        yield ArticuloEconomia(articulo = elem)

        for url in response.xpath('//a[@class="f-linkNota"]/@href').extract():
            yield scrapy.Request('http://lanacion.com.ar'+url, callback=self.parse)