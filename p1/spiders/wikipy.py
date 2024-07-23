import scrapy
from p1.items import P1Item
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst


class WikipySpider(scrapy.Spider):
    name = "wikipy"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://scrapethissite.com/pages/simple/"]

    def parse(self, response, **kwargs):
        for country in response.css('div.country'):
            c = ItemLoader(item=P1Item(), selector=country)
            c.add_css('name', 'h3.country-name')
            c.add_css('capital', 'span.country-capital::text')
            c.add_css('population', 'span.country-population::text')

            yield c.load_item()