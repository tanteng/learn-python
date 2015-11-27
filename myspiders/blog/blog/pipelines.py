# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BlogPipeline(object):

    def __init__(self):
        pass
        # self.file = open('./blog.json','wb')

    def process_item(self, item, spider):
        # self.file.write(json.dumps(dict(item), ensure_ascii=False).encode('utf8') + '\n')
        if(item['description']):
            item['description'] = ''.join(item['description'])

        return item


    def spider_closed(self, spider):
        pass
        # self.file.close()
