from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import SearchResultPageLocators


class SearchResultPage(BasePage):
    def check_search_result_valid(self):
        wait = WebDriverWait(self.browser, 20)
        search_result = wait.until(EC.presence_of_element_located(SearchResultPageLocators.SEARCH_RESULT)).text
        assert search_result == "Найдено 488 фото", "Incorrect result"

    def check_search_result_invalid(self):
        wait = WebDriverWait(self.browser, 10)
        search_result = wait.until(EC.presence_of_element_located(SearchResultPageLocators.NOSING_FOUND)).text
        assert search_result == "Ничего не найдено", "Incorrect result"


