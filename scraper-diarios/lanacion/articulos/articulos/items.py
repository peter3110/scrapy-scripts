# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticuloEconomia(scrapy.Item):

	categoria = scrapy.Field()
	titulo = scrapy.Field()
	texto = scrapy.Field()
	dia = scrapy.Field()
