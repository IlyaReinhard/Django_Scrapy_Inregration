# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from main.models import RepoInformation


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        inf = RepoInformation(name_project =item.get('name_project '), all_repos=item.get('all_repos'))
        inf.save()
        return item

