# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import logging
import scrapy
from itemloaders.processors import TakeFirst


def _construct_image_full_path(value):
    logging.debug(f"what do i get as a value of image path : {value}")
    return value[0].replace("../../", 'https://books.toscrape.com/')


def _extract_star_rating(value):
    logging.debug(f"The value of the book rating is {value}")
    return value[0].replace("star-rating ", "")


class SingleBookItem(scrapy.Item):
    # this is just a simple Item class which does two things
    # gets all the book titles and the page number and takes the page number
    # out from a single element list using the TakeFirst processor
    # book_titles = scrapy.Field()
    # page_number = scrapy.Field(output_processor=TakeFirst())

    book_url = scrapy.Field(output_processor=TakeFirst())
    book_title = scrapy.Field(output_processor=TakeFirst())
    book_price = scrapy.Field(output_processor=TakeFirst())
    book_image = scrapy.Field(
        input_processor=_construct_image_full_path,
        output_processor=TakeFirst()
    )
    book_rating = scrapy.Field(
        input_processor=_extract_star_rating,
        output_processor=TakeFirst()
    )
    book_description = scrapy.Field(output_processor=TakeFirst())
    upc = scrapy.Field(output_processor=TakeFirst())
    product_type = scrapy.Field(output_processor=TakeFirst())
    availability = scrapy.Field(output_processor=TakeFirst())
    number_of_reviews = scrapy.Field(output_processor=TakeFirst())

    image_urls = scrapy.Field(input_processor=_construct_image_full_path)
    images = scrapy.Field()


