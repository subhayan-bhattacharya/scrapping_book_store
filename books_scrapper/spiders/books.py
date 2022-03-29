import scrapy
from scrapy.loader import ItemLoader
from books_scrapper.items import BooksScrapperItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    filename = 'book_titles.txt'

    def __init__(self, *args, **kwargs):
        super(BooksSpider, self).__init__(*args, **kwargs)
        self._page_number = 1

    def parse(self, response):
        # This is the code to just extract all the items from the book website
        # loader = ItemLoader(item=BooksScrapperItem(), response=response)
        # loader.add_xpath('book_titles', '//*[@id="default"]/div/div/div/div/section/div/ol/li/article/h3/a/text()')
        # loader.add_value('page_number', self._page_number)
        # yield loader.load_item()
        # self._page_number += 1
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_url_next_page = response.urljoin(next_page_url)
        # yield scrapy.Request(absolute_url_next_page)
        book_individual_urls = response.xpath(
            '// *[ @ id = "default"] / div / div / div / div / section / div / ol / li / article / h3 / a/@href'
        ).extract()
        for book_url in book_individual_urls:
            absolute_book_url = response.urljoin(book_url)
            yield scrapy.Request(absolute_book_url, callback=self._parse_individual_book)

        # now go to the next page
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)

    def _parse_individual_book(self, response):
        pass

