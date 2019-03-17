# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripItem(scrapy.Item):
    # 用户名字
    cat_user_name = scrapy.Field()
    # 用户评论
    cat_user_comment = scrapy.Field()
    # 用户评论时间
    cat_comment_time = scrapy.Field()
