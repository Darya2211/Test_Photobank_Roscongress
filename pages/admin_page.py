import time

from .base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import AdminPageLocators, BasePageLocators


class Admin(BasePage):


