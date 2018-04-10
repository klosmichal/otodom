import scrapy

class Ad(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    m2 = scrapy.Field()
    rooms_n = scrapy.Field()
    floor = scrapy.Field()
    max_floor = scrapy.Field()
    market = scrapy.Field()
    building_type = scrapy.Field()
    building_material = scrapy.Field()
    windows = scrapy.Field()
    heating = scrapy.Field()
    year = scrapy.Field()
    building_status = scrapy.Field()
    rent = scrapy.Field()
    possession_type = scrapy.Field() 
    available_from = scrapy.Field()
    internet = scrapy.Field()
    cable_tv = scrapy.Field()
    telephone = scrapy.Field()
    antiburglary_blinds = scrapy.Field()
    antiburglary_doors = scrapy.Field()
    intercom = scrapy.Field()
    security = scrapy.Field()
    alarm = scrapy.Field()
    restricted_area = scrapy.Field()
    furniture = scrapy.Field()
    washing_machine = scrapy.Field()
    dish_washer = scrapy.Field()
    fridge = scrapy.Field()
    stove = scrapy.Field()
    oven = scrapy.Field()
    tv = scrapy.Field()
    balcony = scrapy.Field()
    usable_room = scrapy.Field()
    garage = scrapy.Field()
    cellar = scrapy.Field()
    garden = scrapy.Field()
    terrace = scrapy.Field()
    lift = scrapy.Field()
    duplex = scrapy.Field()
    separate_kitchen = scrapy.Field()
    ac = scrapy.Field()
    description = scrapy.Field()


class OtodomSpider(scrapy.Spider):
    name = "otodom"
    allowed_domains = ["otodom.pl"]
    start_urls = [
        'https://www.otodom.pl/sprzedaz/mieszkanie/?nrAdsPerPage=72'
        'https://www.otodom.pl/sprzedaz/dom/?nrAdsPerPage=72'
        ]

    def parse(self, response):
        for link in response.xpath('//div[@class="col-md-content"]/article/@data-url').extract():
            yield scrapy.Request(link, callback=self.parse_ad)
            
        next_page = response.xpath('//li[@class="pager-next"]/a/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_ad(self, response):
        
        ad = Ad()
        ad['name'] = response.xpath('.//header[@class="col-md-offer-content"]/h1/text()').extract_first()
        ad['address'] = response.xpath('.//header[@class="col-md-offer-content"]/address/p/a/text()').extract()
        ad['price'] = response.xpath('.//li[@class="param_price"]/span/strong/text()').extract_first()
        ad['m2'] = response.xpath('.//li[@class="param_m"]/span/strong/text()').extract_first()
        ad['rooms_n'] = response.xpath('.//li[text()="Liczba pokoi "]/span/strong/text()').extract_first()
        ad['floor'] = response.xpath('.//li[@class="param_floor_no"]/span/strong/text()').extract_first()
        ad['max_floor'] = response.xpath('.//li[@class="param_floor_no"]/span/text()').extract_first()
        ad['market'] = response.xpath('.//li/strong[text()="Rynek:"]/parent::li/text()').extract_first()
        ad['building_type'] = response.xpath('.//li/strong[text()="Rodzaj zabudowy:"]/parent::li/text()').extract_first()
        ad['building_material'] = response.xpath('.//li/strong[text()="Materiał budynku:"]/parent::li/text()').extract_first()
        ad['windows'] = response.xpath('.//li/strong[text()="Okna:"]/parent::li/text()').extract_first()
        ad['heating'] = response.xpath('.//li/strong[text()="Ogrzewanie:"]/parent::li/text()').extract_first()
        ad['year'] = response.xpath('.//li/strong[text()="Rok budowy:"]/parent::li/text()').extract_first()
        ad['building_status'] = response.xpath('.//li/strong[text()="Stan wykończenia:"]/parent::li/text()').extract_first()
        ad['rent'] = response.xpath('.//li/strong[text()="Czynsz:"]/parent::li/text()').extract_first()
        ad['possession_type'] = response.xpath('.//li/strong[text()="Forma własności:"]/parent::li/text()').extract_first()
        ad['available_from'] = response.xpath('.//li/strong[text()="Dostępne od:"]/parent::li/text()').extract_first()
        ad['internet'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "internet")]/text()').extract_first() is not None else None
        ad['cable_tv'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "telewizja kablowa")]/text()').extract_first() is not None else None
        ad['telephone'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "telefon")]/text()').extract_first() is not None else None
        ad['antiburglary_blinds'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "rolety antywłamaniowe")]/text()').extract_first() is not None else None
        ad['antiburglary_doors'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "drzwi / okna antywłamaniowe")]/text()').extract_first() is not None else None
        ad['intercom'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "domofon / wideofon")]/text()').extract_first() is not None else None
        ad['security'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "monitoring / ochrona")]/text()').extract_first() is not None else None
        ad['alarm'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "system alarmowy")]/text()').extract_first() is not None else None
        ad['restricted_area'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "teren zamknięty")]/text()').extract_first() is not None else None
        ad['furniture'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "meble")]/text()').extract_first() is not None else None
        ad['washing_machine'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "pralka")]/text()').extract_first() is not None else None
        ad['dish_washer'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "zmywarka")]/text()').extract_first() is not None else None
        ad['fridge'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "lodówka")]/text()').extract_first() is not None else None
        ad['stove'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "kuchenka")]/text()').extract_first() is not None else None
        ad['oven'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "piekarnik")]/text()').extract_first() is not None else None
        ad['tv'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "telewizor")]/text()').extract_first() is not None else None
        ad['balcony'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "balkon")]/text()').extract_first() is not None else None
        ad['usable_room'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "pom. użytkowe")]/text()').extract_first() is not None else None
        ad['garage'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "garaż/miejsce parkingowe")]/text()').extract_first() is not None else None
        ad['cellar'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "piwnica")]/text()').extract_first() is not None else None
        ad['garden'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "ogródek")]/text()').extract_first() is not None else None
        ad['terrace'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "taras")]/text()').extract_first() is not None else None
        ad['lift'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "winda")]/text()').extract_first() is not None else None
        ad['duplex'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "dwupoziomowe")]/text()').extract_first() is not None else None
        ad['separate_kitchen'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "oddzielna kuchnia")]/text()').extract_first() is not None else None
        ad['ac'] = 1 if response.xpath('.//div[@class="col-md-offer-content"]//li[contains(text(), "klimatyzacja")]/text()').extract_first() is not None else None
        ad['description'] = " ".join(response.xpath('.//div[@itemprop="description"]/p//text()').extract())
        
        yield ad