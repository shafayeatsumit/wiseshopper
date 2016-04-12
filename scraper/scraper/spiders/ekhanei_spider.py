import scrapy
from scraper.items import ScraperItem2
import re

class ekhaneispider(scrapy.Spider):
    name = "ekhanei"
    allowed_domains = ["http://www.ekhanei.com/"]
    start_urls=[
        "http://www.ekhanei.com/en/bangladesh/mobiles/for-sale",
        "http://www.ekhanei.com/en/bangladesh/cars/for-sale",
        'http://www.ekhanei.com/en/bangladesh/bicycles/for-sale',
        'http://www.ekhanei.com/en/bangladesh/laptops/for-sale',
        'http://www.ekhanei.com/en/bangladesh/apartments/all',
        'http://www.ekhanei.com/en/bangladesh/motorcycles/for-sale',
    ]
    count=0
    def parse(self,response):

        category=response.url.split('/')[-2]
        for href in response.xpath('//*[@id="list_item_thumbs"]/div'):
            item=ScraperItem2()
            date=href.xpath('abbr[@class="date dtstart value item_age"]/text()').extract()[0]
            #import pdb; pdb.set_trace()
            item['date']=str(re.sub(r'\s+','',date))
            time=href.xpath('abbr[@class="date dtstart value item_age"]/text()').extract()[1]
            item['time']=re.sub(r'\s+','',time)
            item['link']= href.xpath("a/@href").extract_first()
            try:
                item['image']=href.xpath('a[2]/img/@data-src').extract()[0]
            except:
                item['image']="https://goo.gl/QUlUNB"
            item['title']=href.xpath('div[@class="item_info"]/h2/a/text()').extract()[0]
            description=href.xpath('div[@class="item_info"]/p/text()').extract()[0]
            item['description']=re.sub(r'\n','',description)
            price=href.xpath('div[@class="item_price"]//span[@class="price_value"]/text()').extract()[0]
            item['price']=re.sub(r'\s+','',price)
            location=href.xpath('div[@class="item_info"]//small/text()').extract()[0]
            item['location']=re.sub(r'\s+','',location)
            item['category']=category
            yield item
            next_page=response.xpath('//div[@class="pagination"]/div[@class="center"]/a[@class="next pagination_button"]/@href').extract()[0]
        if next_page and self.count!=3:

            self.count +=1
            print
            print
            print self.count
            print
            yield scrapy.Request(next_page, self.parse,dont_filter=True)
