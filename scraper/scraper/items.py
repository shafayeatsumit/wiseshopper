# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from shoppersapp.models import ScraperItem
from scrapy.item import Field

class ScraperItem2(DjangoItem):
    "fields for this item are automatically created from the django model"
    django_model = ScraperItem
    # date=scrapy.Field()
    # time=scrapy.Field()
    # image=scrapy.Field()
    # link=scrapy.Field()
    # title=scrapy.Field()
    # description=scrapy.Field()
    # location=scrapy.Field()
    # price=scrapy.Field()
    # category=scrapy.Field()
