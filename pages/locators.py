from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#app > header > div.header-login")
    MAIL_AREA = (By.CSS_SELECTOR, "#app > header > div.modal > div.email > input[type=text]")
    PASSWORD_AREA = (By.CSS_SELECTOR, "#app > header > div.modal > div.password > input[type=password]")
    ENTER = (By.CSS_SELECTOR, "#app > header > div.modal > div.loginBtn")
    PROFILE_ICON = (By.CSS_SELECTOR, "#app > header > div.header-profile.mobile")
    PROFILE_DROPDOWN = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active")
    FAVORITE = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active > div.mobileProfile-list > "
                                 "a:nth-child(1)")
    MY_PHOTOS = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active > div.mobileProfile-list > "
                                  "a:nth-child(2)")
    SETTING = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active > div.mobileProfile-list > "
                                "a:nth-child(3)")
    STATISTICS = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active > div.mobileProfile-list "
                                   "> a:nth-child(4)")
    ADMINISTRATION = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active > "
                                       "div.mobileProfile-list > a:nth-child(5)")
    SING_OUT = (By.CSS_SELECTOR, "#app > header > div.mobileProfile.mobileProfile--active > div.mobileProfile-logout "
                                 "> a")
    INVALID_PASSWORD = (By.CSS_SELECTOR, "#app > header > div.modal > div.modal-alert")

    LOGO = (By.CSS_SELECTOR, "#app > header > div.header-logo > a")
    PROJECT_IN_HEADER = (By.CSS_SELECTOR, "#app > header > div.header-menu > a:nth-child(1)")
    PROJECT_MAIN = (By.CSS_SELECTOR, "#app > div.p > main > div.intro > div.description > a")
    ALL_PROJECT = (By.CSS_SELECTOR, "#projects > div > a")
    PHOTO_OF_THE_DAY = (By.CSS_SELECTOR, "#app > header > div.header-menu > a:nth-child(2)")
    SEARCH_IN_HEADER = (By.CSS_SELECTOR, "#app > header > div.header-search")
    SEARCH_IN_HEADER_AREA = (By.CSS_SELECTOR, "#app > header > div.header-search.mobileAdaptive.expanded > input["
                                              "type=text]")


class SearchResultPageLocators():
    SEARCH_RESULT = (By.CSS_SELECTOR, "#app > div.p > div > div.search-head > div.search-head__subtitle")
    NOSING_FOUND = (By.CSS_SELECTOR, "#app > div.p > div > div.search-list > div.search-list__notfound")


class MainPageLocators():
    SEE_ALL_EVENTS = (By.CSS_SELECTOR, "#app > div.p > main > div.intro > div.description > a")
    GENERAL_SEARCH = (By.CSS_SELECTOR, "#app > div.p > main > div.search > div > div.search__input-wrapper > "
                                       "div.search__submit")
    GENERAL_SEARCH_INPUT = (By.CSS_SELECTOR, "#app > div.p > main > div.search > div > div.search__input-wrapper > "
                                             "form > input")

    UPLOADER_PHOTO = (By.CSS_SELECTOR, "#hiddenUploader")
    SELECT_A_FILE = (By.CSS_SELECTOR, "#app > div.p > main > div.search > div > div.search__input-wrapper > "
                                      "div.search__scan.search__scan--active > div > div > div.scan-modal__blocks > "
                                      "div.scan-modal__drag > div.scan-modal__block-btn")


class AdminPageLocators():
    ADMIN_SEARCH_INPUT = (
        By.CSS_SELECTOR, "#app > div.p > main > div > div.content > div > div.list > div.search > input[type=text]")
