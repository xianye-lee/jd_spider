# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MallSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Category(scrapy.Item):
    # big categor大
    b_category_name = scrapy.Field()
    b_category_url = scrapy.Field()
    # middle category
    m_category_name = scrapy.Field()
    m_category_url = scrapy.Field()
    # small category
    s_category_name = scrapy.Field()
    s_category_url = scrapy.Field()


class Product(object):
    product_category = scrapy.Field()
    product_sku_id = scrapy.Field()
    product_name = scrapy.Field()
    product_img_url = scrapy.Field()
    product_book_info = scrapy.Field()
    product_option = scrapy.Field()
    product_shop = scrapy.Field()
    product_comments = scrapy.Field()
    product_ad = scrapy.Field()
    product_price = scrapy.Field()
