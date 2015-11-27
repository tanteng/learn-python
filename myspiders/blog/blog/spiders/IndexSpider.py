from scrapy.spiders import Spider
from scrapy.selector import Selector

from blog.items import BlogItem


class BlogIndexSpider(Spider):
    name = "index"
    allowed_domains = ["tantengvip.com"]
    start_urls = [
        "http://www.tantengvip.com/",
    ]

    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//div[@id="content"]/article')
        items = []

        for article in articles:
            item = BlogItem()
            item['title'] = article.xpath('header/h1[@class="entry-title"]/a/text()').extract()
            item['link'] = article.xpath('header/h1[@class="entry-title"]/a/@href').extract()
            item['description'] = article.xpath('div[@class="entry-content"]/p[position()<3]/text()').extract()

            items.append(item)

        return items