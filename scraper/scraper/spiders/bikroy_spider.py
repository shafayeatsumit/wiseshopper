import scrapy
from scraper.items import ScraperItem2
import re

class ekhaneispider(scrapy.Spider):
    name = "bikroy"
    allowed_domains = ["http://bikroy.com/en"]
    start_urls=[
        "http://bikroy.com/en/ads/mobile-phones-in-bangladesh-230",
        "http://bikroy.com/en/ads/cars-in-bangladesh-193",
        "http://bikroy.com/en/ads/apartments-flats-in-bangladesh-211",
        "http://bikroy.com/en/ads/motorbikes-scooters-in-bangladesh-203",
        "http://bikroy.com/en/ads/computers-tablets-in-bangladesh-893",
        "http://bikroy.com/en/ads/bicycles-and-three-wheelers-in-bangladesh-908",
    ]
    count=0
    def parse(self,response):
        category=response.xpath('//nav[@class="ui-crumbs"]/ul/li/h1/a/text()').extract()[0]
        for href in response.xpath('//div[@class="serp-items"]/div[@class="ui-item"]'):
            item=ScraperItem2()
            item['date']=href.xpath('div[@class="item-content"]/p[@class="item-location"]/span[1]/text()').extract()[0]
            item['location']=href.xpath('div[@class="item-content"]/p[@class="item-location"]/span[@class="item-area"]/text()').extract()[0]
            item['price']=href.xpath('div[@class="item-content"]/p[@class="item-info"]/strong/text()').extract()[0]
            item['title']=href.xpath('div[@class="item-content"]/a/text()').extract()[0]
            link=href.xpath('div[@class="item-content"]/a/@href').extract()[0]
            item['link']=response.urljoin(link)
            try:
                image=href.xpath('div[@class="item-thumb has-frames"]|div[@class="item-thumb"]/a/img').extract()[0]
                item['image']="https://"+re.findall(r'i.bikroy-st.com\/[^\s\\]*',image)[1]

            except:
                item['image']="https://goo.gl/QUlUNB"
            item['time']=''
            item['description']='no description available'
            item['category']=category
            yield item
            next_page_url=response.xpath('//a[@class="col-6 lg-3 pag-next"]/@href').extract()[0]
            next_page=response.urljoin(next_page_url)

        if next_page and self.count<2:

            self.count +=1
            yield scrapy.Request(next_page, self.parse,dont_filter=True)
