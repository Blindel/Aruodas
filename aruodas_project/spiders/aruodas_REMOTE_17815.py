from email import header
from importlib.resources import path
from queue import Full
import scrapy
from scrapy.selector import Selector

from scrapy_playwright.page import PageMethod

from aruodas_project.settings import DEFAULT_REQUEST_HEADERS

class AruodasSpider(scrapy.Spider):
    name = 'aruodas'

    def start_requests(self):
        yield scrapy.Request("https://www.aruodas.lt/", headers=DEFAULT_REQUEST_HEADERS,
            meta= {
               "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "button#onetrust-accept-btn-handler"),
                    PageMethod("click", "button#onetrust-accept-btn-handler"),
                    PageMethod("click", "span#display_text_obj"),
                    PageMethod("click", "label.dropDownLabel[for=input_obj_2]"),
                    PageMethod("click", "span#display_text_FRegion"),
                    PageMethod("click", "label.dropDownLabel[for=input_FRegion_461]"),

                ]
            }
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        
        html_body = await page.inner_html("body")
        await page.close()
        
        body = Selector(text=html_body)
        # yield {
            
        # }
         
    