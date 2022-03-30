# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class BooksScrapperPipeline:
    def process_item(self, item, spider):
        """Processes books only if their rating is at least 3."""
        adapter = ItemAdapter(item)
        book_rating = adapter.get('book_rating')
        if book_rating < 3:
            raise DropItem(f"The book rating is too low to be considered {book_rating}")
        return item
