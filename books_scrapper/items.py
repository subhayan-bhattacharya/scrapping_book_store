# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class BooksScrapperItem(scrapy.Item):
    # this is just a simple Item class which does two things
    # gets all the book titles and the page number and takes the page number
    # out from a single element list using the TakeFirst processor
    # book_titles = scrapy.Field()
    # page_number = scrapy.Field(output_processor=TakeFirst())
    pass
