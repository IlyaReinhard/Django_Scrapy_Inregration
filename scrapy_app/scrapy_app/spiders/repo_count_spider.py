import scrapy
from scrapy.spiders import  CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RepoSpider(scrapy.Spider):
    name = 'repo_scr'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/orgs/scrapy/repositories']


    def parse(self, response):
         all_repos = response.xpath("//h3[@class='wb-break-all']/a/@href").getall()

         yield {
            'all_project_repositories': all_repos
        }


