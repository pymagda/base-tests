import time
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = self.wait_visible(locator)
        element.click()

    def get_element_by(self, method, value):
        if method == 'id':
            return self.driver.find_element_by_id(value)
        elif method == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif method == 'css':
            return self.driver.find_element_by_css_selector(value)
        else:
            raise Exception('Invalid locator method.')

    def get_element(self, locator):
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_element_by(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def is_element_visible(self, locator):
        try:
            self.get_element(locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def wait_visible(self, locator, timeout=10):
        i = 0
        while i != timeout:
            try:
                self.is_element_visible(locator)
                return self.get_element(locator)
            except NoSuchElementException:
                time.sleep(1)
                i += 1
        raise Exception('Element never became visible: %s (%s)' % (locator[0], locator[1]))


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)


class NavigationBar(BasePage):
    _leads = ('id', 'nav-leads')
    _user_drop_down = ('id', 'user-dd')

    _dd_settings = ('css', 'li.settings')
    _dd_logout = ('xpath', '//li/a[contains(., "Logout")]')

    def _display_user_drop_down(self):
        self.click(self._user_drop_down)

    def switch_to_leads(self):
        self.click(self._leads)
        from pages.leads import LeadsPage
        return LeadsPage(self.driver)

    def switch_to_settings(self):
        self._display_user_drop_down()
        self.click(self._dd_settings)
        from pages.settings import ProfilePage
        return ProfilePage(self.driver)

    def log_out(self):
        self._display_user_drop_down()
        self.click(self._dd_logout)
        from pages.login import LoginPage
        return LoginPage(self.driver)