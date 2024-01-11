import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import BasePageLocators, MainPageLocators, SearchResultPageLocators


class Search(BasePage):

    def search_face(self):
        uploader = self.browser.find_element(*MainPageLocators.UPLOADER_PHOTO)
        select_file = self.browser.find_element(*MainPageLocators.SELECT_A_FILE)
        select_file.click()
        uploader.send_keys('C:/Users/darya/AquaProjects/Test_Photobank_Roscongress/IMG_3265.jpeg')


class Project(BasePage):

    def test_check_go_to_project_page_from_button_To_All_projects(self):
        wait = WebDriverWait(self.browser, 10)
        project_button_main = wait.until(EC.presence_of_element_located(BasePageLocators.PROJECT_MAIN))
        project_button_main.click()
        time.sleep(5)
        current_url = self.browser.current_url
        assert "projects" in current_url, "The project is not in URL"

    def test_check_go_to_project_page_from_All_projects(self):
        all_project_button = None
        while all_project_button is None:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                all_project_button = self.browser.find_element(*BasePageLocators.ALL_PROJECT)
            except SomeException:
                all_project_button.click()
                time.sleep(3)
                current_url = self.browser.current_url
                assert "projects" in current_url, "The project is not in URL"
