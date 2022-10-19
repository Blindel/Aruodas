from email import header
from importlib.resources import path
from multiprocessing.sharedctypes import Value
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
<<<<<<< HEAD
                    PageMethod("click", "#quickValue_FRoomNum_2"),
                    PageMethod("click", "#display_text_obj"),
                    PageMethod("screenshot", path="view.png"),
=======
                    PageMethod("click", "span#display_text_obj"),
                    PageMethod("click", "label.dropDownLabel[for=input_obj_2]"),
                    PageMethod("click", "span#display_text_FRegion"),
                    PageMethod("click", "label.dropDownLabel[for=input_FRegion_461]"),

>>>>>>> a6e9858b7e20d5947ef38337bce8b67d61ceb491
                ]
            }
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]
<<<<<<< HEAD
    
=======
        
>>>>>>> a6e9858b7e20d5947ef38337bce8b67d61ceb491
        html_body = await page.inner_html("body")
        await page.close()
        
        body = Selector(text=html_body)
<<<<<<< HEAD
        yield {
        #     "div.search-form-content" : response.css("body div.main.filter-form div.header-strip div.header-filter-strip div.header-filter form div.filter-col div.search-form-content").get(),
        #     "div#searchFormContainer" : response.css("body div.main.filter-form div.header-strip div.header-filter-strip div.header-filter form div.filter-col div.search-form-content div#searchFormContainer").get()
         }
=======
        # yield {
            
        # }
>>>>>>> a6e9858b7e20d5947ef38337bce8b67d61ceb491
         
    