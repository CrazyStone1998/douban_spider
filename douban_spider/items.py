# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class movie(scrapy.Item):
    '''
    "rate": "6.3",
    "cover_x": 1371,
    "title": "摩天营救",
    "url": "https://movie.douban.com/subject/26804147/",
    "playable": true,
    "cover": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2527484082.webp",
    "id": "26804147",
    "cover_y": 1920,
    "is_new": false,
    '''

    id = scrapy.Field()
    rate = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    playable = scrapy.Field()
    cover_x = scrapy.Field()
    cover_y = scrapy.Field()
    cover = scrapy.Field()
    is_new = scrapy.Field()

class shortComment(scrapy.Item):

    id = scrapy.Field()
    movie_id = scrapy.Field()
    rate = scrapy.Field()
    comment = scrapy.Field()

class movieComment(scrapy.Item):

    id = scrapy.Field()
    title = scrapy.Field()
    movie_id = scrapy.Field()
    rate = scrapy.Field()
    comment = scrapy.Field()







