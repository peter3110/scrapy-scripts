import scrapy
import re
from datetime import date

from articulos.items import *

class QuotesSpider(scrapy.Spider):
    name = 'articulos_spider'
    allowed_domains = [
        'lanacion.com.ar'
    ]
    start_urls = [
        'http://www.lanacion.com.ar/deportes',
        'http://www.lanacion.com.ar/vida-y-ocio',
        'http://www.lanacion.com.ar/comunidad-de-negocios',
        'http://www.lanacion.com.ar/ideas',
        'http://www.lanacion.com.ar/espectaculos',
        'http://www.lanacion.com.ar/politica',
        'http://www.lanacion.com.ar/el-mundo',
        'http://www.lanacion.com.ar/sociedad',
        'http://www.lanacion.com.ar/seguridad',
        'http://www.lanacion.com.ar/buenos-aires',
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
        dia       = date.today()
        categoria = cat
        titulo    = response.xpath('//title').extract()
        texto     = response.xpath('//p[@class="primero"]').extract()
        
        # Guardo el articulo de la pagina actual
        yield ArticuloEconomia(dia = dia, categoria = categoria, titulo = titulo, texto=texto)

        # Si es una pagina que tiene links a otras notas, voy a recorrer esas notas
        for url in response.xpath('//a[@class="f-linkNota"]/@href').extract():
            yield scrapy.Request(
                url = 'http://lanacion.com.ar'+url, 
                callback = lambda r: self.parse(r, cat)
            )



