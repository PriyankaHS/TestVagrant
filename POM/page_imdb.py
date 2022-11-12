import config
from Library.selenium_wrapper import SeleniumWrapper
from selenium import webdriver


class PageIMDB:
    _input_search = "xpath", "//input[@name='q']"
    _button_search = "id", "suggestion-search-button"
    _text_pushpa = "xpath", "//a[contains(text(),'Pushpa') and contains(text(),'The Rise') and  contains(text()," \
                            "'Part 1')] "
    _text_country = "xpath", "//button[text()='Country of origin']/..//a"
    _text_movie_title = "xpath", "//h1"
    _img_release_arrow = "xpath", "//a[text()='Release date']/..//*[name()='svg']"
    _text_date_of_release = "xpath", "//a[contains(text(),'India')]/../..//td[@class='release-date-item__date']"

    def __init__(self, driver):
        self.driver: webdriver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def enter_movie_name(self, movie_name):
        self.selenium_wrapper.goto_url(config.imdb_url)
        self.driver.find_element(*self._input_search).send_keys(movie_name)
        self.driver.find_element(*self._button_search).click()
        self.driver.find_element(*self._text_pushpa).click()
        movie_title = self.driver.find_element(*self._text_movie_title).text
        assert movie_name in movie_title

    def get_country_of_origin(self):
        country = self.driver.find_element(*self._text_country)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", country)
        return country.text

    def get_release_date(self):
        self.driver.find_element(*self._img_release_arrow).click()
        release_date = self.driver.find_element(*self._text_date_of_release).text
        return release_date.split()


