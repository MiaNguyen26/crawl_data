import scrapy


class ProductSpider(scrapy.Spider):
    name = "anphat_product"
    allowed_domains = ["anphatpc.com.vn"]
    start_urls = [
                    "https://www.anphatpc.com.vn/may-tinh-xach-tay-laptop.html",
                    ]

    def parse(self, response):
        pass
