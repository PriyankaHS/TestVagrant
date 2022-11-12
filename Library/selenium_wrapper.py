from selenium import webdriver


class SeleniumWrapper:
    def __init__(self, driver:webdriver):
        self.driver = driver

    def goto_url(self, url):
        self.driver.get(url)


