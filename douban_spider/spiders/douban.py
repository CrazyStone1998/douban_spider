# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import Request
from douban_spider import items

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    movie_start_url = 'https://movie.douban.com/j/search_subjects?' \
                      'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&' \
                      'page_limit=20&page_start={page}'
    # movie_start_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=20'
    movie_num = 10000
    short_comment_num = 200
    movie_comment_num = 200
    movie_rate_dist = {
        '力荐': 5,
        '推荐': 4,
        '还行': 3,
        '较差': 2,
        '很差': 1,
    }
    # 网络请求头设置
    # headers = {
    #     'Accept': '*/*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CH,zh;q=0.9,en;q=0.8',
    #     'Connection': 'keep-alive',
    #     'Host': 'movie.douban.com',
    #     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
    #
    # }

    def start_requests(self):
        '''

        :return:
        '''
        for page in range(1, self.movie_num // 20):

            yield Request(self.movie_start_url.format(page=page*20),
                          callback=self.parse_movie)

        # yield Request(url='https://movie.douban.com/subject/26366496/reviews?start=40',
        #               callback=self.movie_comment_page
        #               )

    def parse_movie(self, response):

        '''
        json 格式：
            "rate": "6.3",
            "cover_x": 1371,
            "title": "摩天营救",
            "url": "https://movie.douban.com/subject/26804147/",
            "playable": true,
            "cover": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2527484082.webp",
            "id": "26804147",
            "cover_y": 1920,
            "is_new": false,
        影评：
            https://movie.douban.com/subject/4864908/reviews

        :param response:
        :return:
        '''
        result = json.loads(response.text)

        for movie in result.get('subjects'):

            item = items.movie()

            item['id'] = movie['id']
            item['title'] = movie['title']
            item['url'] = movie['url']
            item['rate'] = float(movie['rate'])
            item['cover_x'] = movie['cover_x']
            item['cover_y'] = movie['cover_y']
            item['cover'] = movie['cover']
            item['playable'] = movie['playable']
            item['is_new'] = movie['is_new']

            yield item

            yield Request(
                url=movie.get('url'),
                meta={'data': movie},
                callback=self.parse_short_comment,
            )

            yield Request(
                url=movie.get('url'),
                meta={'data': movie},
                callback=self.parse_movie_comment,
            )

        # yield Request(
        #     url=result.get('subjects')[0].get('url')+'comments?status=P',
        #     meta={'data': result.get('subjects')[0]},
        #     callback=self.parse_short_comment,
        # )

    def parse_short_comment(self, response):
        '''
        短评：
            https://movie.douban.com/subject/4864908/comments?start=20&limit=20&sort=new_score&status=P

        :param response:
        :return:
        '''
        url = response.meta['data']['url']
        for page in range(self.short_comment_num // 20):

            yield Request(
                url=url+'comments?start={page}&limit=20&sort=new_score&status=P'.format(page=page*20),
                meta={'data': response.meta['data']},
                callback=self.short_comment
            )
        # yield Request(
        #         url=url+'comments?start=20&limit=20&sort=new_score&status=P',
        #         meta={'data': response.meta['data']},
        #         callback=self.short_comment
        #     )

    def short_comment(self, response):
        '''

        //*[@id="comments"]/div/div[2]/p/span
        //*[@id="comments"]/div/div[2]/h3/span[2]/span[2]/@title

        力荐： 5
        推荐： 4
        还行： 3
        较差： 2
        很差： 1
        :param response:
        :return:
        '''
        movie_id = response.meta['data']['id']

        id_list = response.xpath('//*[@id="comments"]/div/@data-cid').extract()
        comment_list = response.xpath('//*[@id="comments"]/div/div[2]/p/span/text()').extract()
        rate_list = response.xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/span[2]/@title').extract()
        for each in range(20):

            item = items.shortComment()

            item['id'] = id_list[each]
            try:
                item['rate'] = self.movie_rate_dist[rate_list[each]]
            except Exception as e:
                item['rate'] = 0
            item['movie_id'] = movie_id
            item['comment'] = comment_list[each]

            yield item

    def parse_movie_comment(self, response):
        '''
        //*[@class="review-list"]/
        :param response:
        :return:
        '''
        url = response.meta['data']['url']
        for page in range(self.movie_comment_num // 20):
            yield Request(
                url=url + 'reviews?start={page}'.format(page=page * 20),
                meta={'data': response.meta['data']},
                callback=self.movie_comment_page
            )


    def movie_comment_page(self, response):
        '''
        //*[@class="review-list"]/div/div/h2/a/@href
        :param response:
        //*[@id="9513571"]/div/h2/a
        :return:
        '''

        url_list = response.xpath('//*[@class="review-list  "]/div/div/div/h2/a/@href').extract()
        for each in url_list:
            yield Request(
                url=each,
                meta={
                    'data': response.meta['data'],
                },
                callback=self.movie_comment,
            )

    def movie_comment(self, response):
        '''
        //*[@id="content"]/div/div[1]/h1/span/text()
        //*[@id="content"]/div/div[1]
        //*[@id="9513571"]
        //*[@id="9513571"]/header/span[1]
        //*[@id="link-report"]/div[1]
        :param response:
        :return:
        '''

        item = items.movieComment()

        item['movie_id'] = response.meta['data']['id']
        item['id'] = response.xpath('//*[@class="main"]/@id').extract()[0]
        try:
            item['rate'] = self.movie_rate_dist[response.xpath('//*[@class="main"]/header/span[1]/@title').extract()[0]]
        except Exception as e:
            item['rate'] = 0
        item['title'] = response.xpath('//*[@id="content"]/div/div[1]/h1/span/text()').extract()[0]
        item['comment'] = response.xpath('//*[@id="link-report"]/div[1]').extract()[0]

        yield item
