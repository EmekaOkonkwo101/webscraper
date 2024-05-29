from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from webscraper.items import BookItem

class CrawlingSpider(CrawlSpider):
    name = 'demoCrawler'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://books.toscrape.com/']
    

    
    rules = (
        Rule(LinkExtractor(allow=r'catalogue/category')),
        Rule(LinkExtractor(allow=r'catalogue', deny='category'), callback='parse_item'),
    )
    

    
    def parse_item(self, response):
        item = BookItem()    
        item["name"] = response.css('.product_main h1::text').extract_first()

        yield{        
            'title': response.css('.product_main h1::text').get(),
            'price': response.css('.price_color::text').get(),
            'description': response.css('.availability::text')[1].get().replace('\n', '').replace(' ','')
        }