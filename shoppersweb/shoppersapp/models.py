from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class ScraperItem(models.Model):
    time=  models.CharField(max_length=32)
    date = models.CharField(max_length=100)
    image =  models.CharField(max_length=344)
    link= models.CharField(max_length=324)
    title= models.CharField(max_length=255)
    description= models.CharField(max_length=322)
    location= models.CharField(max_length=32)
    price= models.CharField(max_length=32)
    category= models.CharField(max_length=32)

    def __str__(self):
        return self.title

    # date=scrapy.Field()
    # time=scrapy.Field()
    # image=scrapy.Field()
    # link=scrapy.Field()
    # title=scrapy.Field()
    # description=scrapy.Field()
    # location=scrapy.Field()
    # price=scrapy.Field()
    # category=scrapy.Field()
