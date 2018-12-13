# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from douban_spider import items
from douban_spider import settings

class DoubanSpiderPipeline(object):

    def __init__(self):

        #连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset=settings.MYSQL_CHARSET,
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            if isinstance(item, items.movie):
                print('执行到这里了')

                #查重处理
                self.cursor.execute(
                    '''
                    select * from doubanspider.movie 
                    where id = %s;
                    ''',
                   item['id']
                )

                #是否有重复数据
                repetition = self.cursor.fetchone()

                #重复
                if repetition:
                    pass
                else:
                    #插入数据
                    self.cursor.execute(
                        '''
                        insert into doubanspider.movie value 
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                        ''',
                        (
                            item['id'],
                            item['rate'],
                            item['title'],
                            item['url'],
                            item['playable'],
                            item['cover_x'],
                            item['cover_y'],
                            item['cover'],
                            item['is_new'],
                        )
                    )
                    self.connect.commit()
                    print('------------------------------------------------------------')

            elif isinstance(item, items.shortComment):
                # 查重处理
                print('**************************')
                self.cursor.execute(
                    '''
                    select * from doubanspider.shortcomment 
                    where id = %s;
                    ''',
                    item['id']
                )

                # 是否有重复数据
                repetition = self.cursor.fetchone()

                # 重复
                if repetition:
                    pass
                else:
                    print('&&&&&&&&&&&&&&&&&')
                    # 插入数据
                    self.cursor.execute(
                        '''
                        insert into doubanspider.shortcomment value 
                        (%s, %s, %s, %s);
                        ''',
                        (
                            item['id'],
                            item['rate'],
                            item['movie_id'],
                            item['comment'],
                        )
                    )
                    self.connect.commit()

            elif isinstance(item, items.movieComment):
                self.cursor.execute(
                    '''
                    select * from doubanspider.moviecomment 
                    where id = %s;
                    ''',
                    item['id']
                )

                # 是否有重复数据
                repetition = self.cursor.fetchone()

                # 重复
                if repetition:
                    pass
                else:
                    print('&&&&&&&&&&&&&&&&&')
                    # 插入数据
                    self.cursor.execute(
                        '''
                        insert into doubanspider.moviecomment value 
                        (%s, %s, %s, %s, %s);
                        ''',
                        (
                            item['id'],
                            item['title'],
                            item['rate'],
                            item['movie_id'],
                            item['comment'],
                        )
                    )
                    self.connect.commit()



        except Exception as e:

            print('error:%s', e)
        return item
