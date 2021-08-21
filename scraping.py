import scrapy 



class QuotesSpider(scrapy.Spider):
    name = 'acoes'
    allowed_domains = ["financenews.com.br"]
    start_urls = ['https://financenews.com.br/feed/']

    def parse(self,response):

        news = response.xpath('//channel/item')
    
        for new in news:
            
            link = new.xpath('link/text()').get()

            yield scrapy.Request(url=link, callback=self.extract_news)


    def extract_news(self,response):

        title = response.xpath('normalize-space(//div[@class="title-single"]//h1)').get()
        
        texto = list()

        for l in response.xpath('/html/body/div[2]/div[2]/div/div[1]/div[3]'):
            text = [t.strip() for t in l.xpath('.//text()').extract() if t.strip()]
            texto.append(' '.join(text).split("Whatsapp")[0].split("Telegram")[0].strip())

        yield{
            'title':title,
            'news':texto
        }