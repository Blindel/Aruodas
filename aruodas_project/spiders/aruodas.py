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
        yield scrapy.Request("https://www.aruodas.lt/", headers=DEFAULT_REQUEST_HEADERS, proxies=
            meta= {
               "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [

                    #accepts cookies
                    PageMethod("wait_for_selector", "button#onetrust-accept-btn-handler"),
                    PageMethod("click", "button#onetrust-accept-btn-handler"),

                    #Object type
                    PageMethod("click", "span#display_text_obj"),
                    PageMethod("click", "label.dropDownLabel[for=input_obj_1]"),

                    #Selects region
                    PageMethod("click", "span#display_text_FRegion"),
                    PageMethod("click", "label.dropDownLabel[for=input_FRegion_461]"),

                    #range of rooms
                    PageMethod("click", "#display_FRoomNum span.icon-double-arrow-right-tiny"),
                    PageMethod("fill", "input#input_FRoomNumMin", "1"),
                    PageMethod("fill", "input#input_FRoomNumMax", "7"),

                    # PageMethod("wait_for_selector", "fieldset.recomended-boxes:last-child > img.box-img")
                    # PageMethod("click", "input#buttonSearchForm"),
                    # PageMethod("screenshot", path="aruodas2.png", full_page=True),
                ]
            }
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        html_body = await page.inner_html("body")
        await page.mouse.move(10, 10)
        await page.mouse.move(15, 100)
        await page.click("input#buttonSearchForm")

        await page.close()
        
        body = Selector(text=html_body)

        # yield {
            
        # }
