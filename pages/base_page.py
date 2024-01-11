import time
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.get(self.url)

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def save_screenshot(self, name):
        screenshot_dir = "screenshots"  # Имя папки для сохранения скриншотов
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, name + ".png")
        self.browser.save_screenshot(screenshot_path)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_form(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_FORM)
        link.click()

    def log_in_by_valid_password(self):
        mail = self.browser.find_element(*BasePageLocators.MAIL_AREA)
        mail.send_keys("m.sergeev@magnatmedia.com")
        password = self.browser.find_element(*BasePageLocators.PASSWORD_AREA)
        password.send_keys("GL1kGIm29a")
        button = self.browser.find_element(*BasePageLocators.ENTER)
        button.click()

    def log_in_by_invalid_password(self):
        mail = self.browser.find_element(*BasePageLocators.MAIL_AREA)
        mail.send_keys("m.sergeev@magnatmedia.com")
        password = self.browser.find_element(*BasePageLocators.PASSWORD_AREA)
        password.send_keys("Rhi4")
        button = self.browser.find_element(*BasePageLocators.ENTER)
        button.click()

    def check_the_message_about_entering_an_incorrect_password(self):
        invalid_password = self.browser.find_element(*BasePageLocators.INVALID_PASSWORD)
        assert invalid_password.is_displayed(), "If you enter the wrong password, the warning will not be displayed"

    def check_authorization_by_profile_icon(self):
        profile_icon = WebDriverWait(self.browser,
                                     10).until(EC.presence_of_element_located(BasePageLocators.PROFILE_ICON))
        assert profile_icon.is_displayed(), "The profile panel is missing"

    def start_of_the_search_valid(self):
        wait = WebDriverWait(self.browser, 10)
        search_in_header = wait.until(EC.presence_of_element_located(BasePageLocators.SEARCH_IN_HEADER))
        search_in_header.click()
        search_in_header_area = wait.until(EC.presence_of_element_located(BasePageLocators.SEARCH_IN_HEADER_AREA))
        search_in_header_area.send_keys("тест", Keys.ENTER)

    def start_of_the_search_invalid(self):
        wait = WebDriverWait(self.browser, 10)
        search_in_header = wait.until(EC.presence_of_element_located(BasePageLocators.SEARCH_IN_HEADER))
        search_in_header.click()
        search_input = self.browser.find_element(*BasePageLocators.SEARCH_IN_HEADER_AREA)
        search_input.send_keys("тст", Keys.ENTER)

    def test_check_go_to_project_page_from_the_header(self):
        wait = WebDriverWait(self.browser, 10)
        project_button_main = wait.until(EC.presence_of_element_located(BasePageLocators.PROJECT_IN_HEADER))
        project_button_main.click()
        time.sleep(5)
        current_url = self.browser.current_url
        assert "projects" in current_url, "The project is not in URL"

    def activate_admin_dropdown(self):
        profile_icon = self.browser.find_element(*BasePageLocators.PROFILE_ICON)
        profile_icon.click()
        profile_dropdown = self.browser.find_element(*BasePageLocators.PROFILE_DROPDOWN)
        time.sleep(1)
        assert profile_dropdown.is_displayed(), "Profile drop-down not visible"

    def go_to_favorite_page(self):
        favorite_page = self.browser.find_element(*BasePageLocators.FAVORITE)
        favorite_page.click()
        time.sleep(5)
        profile_icon = self.browser.find_element(*BasePageLocators.PROFILE_ICON)
        profile_icon.click()
        current_url = self.browser.current_url
        assert "favorite" in current_url, "The favorite is not in URL"

    def go_to_my_photos_page(self):
        my_photos_page = self.browser.find_element(*BasePageLocators.MY_PHOTOS)
        my_photos_page.click()
        time.sleep(5)
        profile_icon = self.browser.find_element(*BasePageLocators.PROFILE_ICON)
        profile_icon.click()
        current_url = self.browser.current_url
        assert "profile" in current_url, "The profile is not in URL"

    def go_to_setting_page(self):
        my_photos_page = self.browser.find_element(*BasePageLocators.SETTING)
        my_photos_page.click()
        time.sleep(5)
        profile_icon = self.browser.find_element(*BasePageLocators.PROFILE_ICON)
        profile_icon.click()
        current_url = self.browser.current_url
        assert "setting" in current_url, "The setting is not in URL"

    def go_to_statistics_page(self):
        my_photos_page = self.browser.find_element(*BasePageLocators.STATISTICS)
        my_photos_page.click()
        time.sleep(5)
        profile_icon = self.browser.find_element(*BasePageLocators.PROFILE_ICON)
        profile_icon.click()
        current_url = self.browser.current_url
        assert "stats" in current_url, "The stats is not in URL"
