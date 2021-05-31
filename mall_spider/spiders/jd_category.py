import scrapy
import json
from mall_spider.items import Category


class JdCategorySpider(scrapy.Spider):
    name = 'jd_category'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        # print(response.body.decode('GBK'))
        result = json.loads(response.body.decode('GBK'))
        datas = result['data']
        for data in datas:
            item = Category()
            b_category = data['s'][0]
            b_category_info = b_category['n']
            # print("big category:{}".format(b_category_info))
            item['b_category_name'], item['b_category_url'] = self.get_category_name_url(b_category_info)
            m_category_s = b_category['s']
            for m_category in m_category_s:
                m_category_info = m_category['n']
                # print("middle category:{}".format(m_category_info))
                item['m_category_name'], item['m_category_url'] = self.get_category_name_url(m_category_info)
                s_category_s = m_category['s']
                for s_category in s_category_s:
                    s_category_info = s_category['n']
                    # print("small category:{}".format(s_category_info))
                    item['s_category_name'], item['s_category_url'] = self.get_category_name_url(s_category_info)
                    # print(item)
                    yield item

    def get_category_name_url(self, category_info):
        """
       :param category_info:
        :return: category name and url
        """
        categorys = category_info.split('|')
        category_url = categorys[0]
        category_name = categorys[1]
        if category_url.count('jd.com') == 1:
            category_url = 'https://' + category_url
        elif category_url.count('-') == 1:
            category_url = 'https://channel.jd.com/{}.html'.format(category_url)
        else:
            # 9987-12854-12856|phone||0
            category_url = category_url.replace('-', ',')
            category_url = 'https://list.jd.com/list.html?cat={}'.format(category_url)


        return category_name, category_url
