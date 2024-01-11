import pytest

from .pages.base_page import BasePage
from .pages.main_page import Search, Project
from .pages.search_result_page import SearchResultPage

link = "https://stage.rcfb.abolsoft.ru/ru/"


@pytest.mark.admin_page
def test_admin(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_form()
    page.log_in_by_valid_password()
    page.activate_admin_dropdown()
    page.go_to_favorite_page()
    page.go_to_my_photos_page()
    page.go_to_setting_page()
    page.go_to_statistics_page()



