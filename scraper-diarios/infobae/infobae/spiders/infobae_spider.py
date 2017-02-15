import scrapy
import re
from datetime import date

from infobae.items import *

class QuotesSpider(scrapy.Spider):
    name = 'infobae_spider'
    allowed_domains = [
        'infobae.com'
    ]
    start_urls = [
        'http://www.infobae.com/deportes',
        'http://www.infobae.com/politica',
        'http://www.infobae.com/economia',
        'http://www.infobae.com/sociedad',
        'http://www.infobae.com/tecno',
        'http://www.infobae.com/tendencias',
        'http://www.infobae.com/salud',
        'http://www.infobae.com/autos',
        'http://www.infobae.com/turismo',
        'http://www.infobae.com/horoscopo',
    ]

    def start_requests(self):
        yield scrapy.Request(
                url = self.start_urls[0],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[0])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[1],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[1])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[2],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[2])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[3],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[3])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[4],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[4])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[5],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[5])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[6],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[6])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[7],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[7])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[8],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[8])[-1])
            )
        yield scrapy.Request(
                url = self.start_urls[9],
                callback = lambda r: self.parse(r, re.split('/', self.start_urls[9])[-1])
            )
                

    def parse(self, response, cat):

        # Levanto los datos del articulo actual
        fecha     = date.today()
        categoria = cat
        titulo    = response.xpath('//title').extract()
        # TODO: MEJORAR ESTO
        texto     = response.xpath('//p[@class="element element-paragraph"]').extract()
        
        # Guardo el articulo de la pagina actual
        yield ArticuloEconomia(dia = fecha, categoria = categoria, titulo = titulo, texto=texto)

        # Si es una pagina que tiene links a otras notas, voy a recorrer esas notas
        for url in response.xpath('//a[@data-pb-url-field="canonical_url"]/@href').extract():
            yield scrapy.Request(
                url = 'http://www.infobae.com' + url,
                callback = lambda r: self.parse(r, cat)
            )

