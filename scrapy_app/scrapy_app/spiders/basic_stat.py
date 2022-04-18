import scrapy
from scrapy.spiders import  CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BasicStatistic(CrawlSpider):
    name = 'repo_scrapy'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/orgs/scrapy/repositories']

    #def average_stars(self, response):
      #  all_stars = response.xpath('//a[@class="no-wrap Link--muted mr-3"]/text()[2]').getall()
     #   stars = [i.strip() for i in all_stars]


    def parse(self, response):
         name_project = response.xpath("//a[@class='color-fg-default no-underline']/text()[2]").get().strip()
         all_repos = len(response.xpath("//h3[@class='wb-break-all']/a/@href").getall())
         #all_stars = response.xpath('//a[@class="no-wrap Link--muted mr-3"]/text()[2]').getall()
         #stars = [i.strip() for i in all_stars]
         yield {
            'all_project_repositories': all_repos,
             'name-project': name_project}

