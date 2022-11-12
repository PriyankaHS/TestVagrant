import config
from Library.selenium_wrapper import SeleniumWrapper
from selenium import webdriver


class PageWIKI:
    _input_search = "id", "searchInput"
    _button_search = "id", "searchButton"
    _text_pushpa = "xpath", "//h1/i[text()='Pushpa: The Rise']"
    _text_country = "xpath", "//th[text()='Country']/..//td"
    _text_date_of_release = "xpath", "//div[text()='Release date']/../..//li"

    def __init__(self, driver):
        self.driver: webdriver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def enter_movie_name(self, movie_name):
        self.selenium_wrapper.goto_url(config.wiki_url)
        self.driver.find_element(*self._input_search).send_keys(movie_name)
        self.driver.find_element(*self._button_search).click()
        self.driver.find_element(*self._text_pushpa).click()
        movie_title = self.driver.find_element(*self._text_pushpa).text
        assert movie_name in movie_title

    def get_country_of_origin(self):
        country = self.driver.find_element(*self._text_country)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", country)
        return country.text

    def get_release_date(self):
        release_date = self.driver.find_element(*self._text_date_of_release).text
        return release_date.split()

