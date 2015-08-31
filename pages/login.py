from pages.base import BasePage, DashboardPage


class LoginPage(BasePage):
    _email_field = ('id', 'user_email')
    _password_field = ('id', 'user_password')
    _login_button = ('xpath', '//button[contains(., "Log in")]')

    def log_in(self, email, password):
        self.send_keys(self._email_field, str(email))
        self.send_keys(self._password_field, str(password))
        self.click(self._login_button)
        return DashboardPage(self.driver)
