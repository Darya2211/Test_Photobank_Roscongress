import pytest

from .pages.base_page import BasePage
from .pages.main_page import Search, Project
from .pages.search_result_page import SearchResultPage

link = "https://stage.rcfb.abolsoft.ru/ru/"


@pytest.mark.positive
@pytest.mark.authorization
# Пользователь пытается войти с верным паролем
def test_the_user_logs_in_with_a_valid_password(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_form()
    page.log_in_by_valid_password()
    page.check_authorization_by_profile_icon()


@pytest.mark.negative
@pytest.mark.authorization
# Пользователь пытается войти с неверным паролем
def test_the_user_logs_in_with_a_invalid_password(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_form()
    page.log_in_by_invalid_password()
    page.check_the_message_about_entering_an_incorrect_password()


@pytest.mark.positive
@pytest.mark.search
# Пользователь ищет по запросу "тест"
def test_search_valid_result(browser):
    page = BasePage(browser, link)
    page.open()
    page.start_of_the_search_valid()
    page = SearchResultPage(browser, link)
    page.check_search_result_valid()


@pytest.mark.negative
@pytest.mark.search
# Пользователь ищет по запоросу "тст"
def test_search_invalid_result(browser):
    page = SearchResultPage(browser, link)
    page.open()
    page.start_of_the_search_invalid()
    page.check_search_result_invalid()


@pytest.mark.project
# Пользователь переходит на страницу Проекты через кнопку в хедере, Ко всем проектам и Все проекты
def test_check_go_to_project_page_from_the_header(browser):
    page = BasePage(browser, link)
    page.open()
    page.test_check_go_to_project_page_from_the_header()


@pytest.mark.project
# Пользователь переходит на страницу Проекты через кнопку Ко всем проектам
def test_check_go_to_project_page_from_button_To_All_projects(browser):
    page = Project(browser, link)
    page.open()
    page.test_check_go_to_project_page_from_button_To_All_projects()


@pytest.mark.project
# Пользователь переходит на страницу Проекты через кнопку Все проекты
def test_check_go_to_project_page_from_All_projects(browser):
    page = Project(browser, link)
    page.open()
    page.test_check_go_to_project_page_from_All_projects()


@pytest.mark.test_screenshot
# Делает скриншот страницы
def test_screenshot(browser):
    page = Project(browser, link)
    page.open()
    page.save_screenshot("screenshot_name")


