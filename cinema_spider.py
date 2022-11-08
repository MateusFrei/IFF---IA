import scrapy
from ..items import Exercicio01Item

class CinemaSpiderSpider(scrapy.Spider):
    name = 'cinema'
    start_urls = ['https://www.adorocinema.com/filmes/numero-cinemas/']


    def parse(self, response):
        items = Exercicio01Item()

        #filme_name = response.css('.meta-title-link::text').extract()
        filme_name = response.css('.entity-card-list .meta-title-link').css('::text').extract()
        filme_genero = response.css('.blue-link::text').extract()

        items['filme_name'] = filme_name
        items['filme_genero'] = filme_genero

        yield items