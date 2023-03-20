import re

import scrapy

from pep_parse.items import PepParseItem

PEP_NUMBER_REG_EXPRESSION = r'^PEP\s(?P<number>\d+)\s–\s'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.xpath(
            '//section[@id="index-by-category"]'
            '//a[@class="pep reference internal"]/@href'
        ).getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.xpath('//h1[@class="page-title"]/text()').get()
        pep_number = int(
            re.search(PEP_NUMBER_REG_EXPRESSION, pep_title).group('number')
        )
        name = response.css('dt:contains("Author") + dd::text').get()
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': pep_number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
