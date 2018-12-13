# -*- coding: utf-8 -*-

# Scrapy settings for douban_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_spider'

SPIDER_MODULES = ['douban_spider.spiders']
NEWSPIDER_MODULE = 'douban_spider.spiders'

# DATABASE MYSQL
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'doubanspider'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'Shijunyu'
MYSQL_CHARSET = 'utf8'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# HTTPERROR_ALLOWED_CODES = [301,302]
# REDIRECT_ENABLED = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.3',
  'Connection': 'keep-alive',
  'Cache-Control': 'max-age=0',
  'Referer': 'https://movie.douban.com/subject/3168101/?from=showing',
  'Host': 'movie.douban.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
  'Cookies': '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1544505759%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=61ea429397de3c8b.1542290873.7.1544505770.1544492718.; __yadk_uid=Rr2Rv5ZCTX37YHS74CBOY9zUrB9aQETt; _pk_ses.100001.4cf6=*; ck=4g32; ll="118220"; push_doumail_num=0; _vwo_uuid_v2=DD3FE4D3A89CA9181885131D162A0BF61|4b837621ae67007bc47ae53c3472d736; ap_v=0,6.0; bid=Xx_fr3Ndgak; ue="1453793807@qq.com"; ps=y; push_noty_num=0; dbcl2="188523178:sNyZEYycJkw"; ct=y'}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_spider.middlewares.DoubanSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'douban_spider.middlewares.DoubanSpiderDownloaderMiddleware': 543,
#    #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'douban_spider.pipelines.DoubanSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
