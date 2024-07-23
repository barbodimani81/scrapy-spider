# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import MapCompose
from itemloaders.processors import TakeFirst



class P1Item(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            lambda value: value.strip(),
        ),
        output_processor=TakeFirst()
    )
    capital = scrapy.Field(output_processor=TakeFirst())
    population = scrapy.Field(output_processor=TakeFirst())


