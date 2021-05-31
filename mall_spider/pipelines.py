# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from mall_spider.spiders.jd_category import JdCategorySpider
from mall_spider.settings import MONGODB_URL
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CategoryPipeline:

    def open_spider(self, spider):
        if isinstance(spider, JdCategorySpider):
            self.client = MongoClient(MONGODB_URL)
            self.collection = self.client['jd']['category']

    def process_item(self, item, spider):
        if isinstance(spider, JdCategorySpider):
            self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        if isinstance(spider, JdCategorySpider):
            self.client.close()
