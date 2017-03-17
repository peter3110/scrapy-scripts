import scrapy
import time
from selenium import webdriver
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import XPathSelector

class ItalkiSpider(CrawlSpider):
    name = "italki"
    allowed_domains = ['italki.com']
    start_urls = ['http://www.italki.com/entries/korean']
    # not sure if the rule is set correctly
    rules = (Rule(LxmlLinkExtractor(allow="\entry"), callback = "parse_post", follow = True),)
    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        # adding necessary search parameters to the URL
        self.driver.get(response.url+"#language=korean&author-language=russian&marks-min=-5&sort=1&page=1")
        # pressing the "Show More" button at the bottom of the search results page to show the next 15 posts, when all results are loaded to the page, the button disappears
        more_btn = self.driver.find_element_by_xpath('//a[@id="a_show_more"]')

        while more_btn:
            more_btn.click()
            # sometimes waiting for 5 sec made spider close prematurely so keeping it long in case the server is slow
            time.sleep(10)

        # here is where the problem begins, I am making a list of links to all the posts on the big page, but I am afraid links will contain only the first link, because selenium doesn't do the multiple selection as one would expect from this xpath...how can I grab all the links and put them in the links list (and should I?)
        links=self.driver.find_elements_by_xpath('/html/body/div[8]/div/div[1]/div[3]/div[3]/ul/li/div[2]/a')
        for link in links:
            link.click()
            time.sleep(3)

    # this is the function for parsing individual posts, called back by the *parse* method as specified in the rule of the spider; if it is correct, it should have saved at least one post into an item... I don't really understand how and where this callback function gets the response from the new page (the page of the post in this case)...is it automatically loaded to drive and then passed on to the callback function as soon as selenium has clicked on the link (link.click())? or is it all total nonsense...
    def parse_post(self, response):
        hxs = Selector(response)
        item = ItalkiItem()
        item["post_item"] = hxs.xpath('//div [@id="a_NMContent"]/text()').extract()
        return item