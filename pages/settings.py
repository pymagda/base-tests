from pages.base import BasePage, NavigationBar


class SettingsNavigationBar(BasePage):
    _leads = ('xpath', '//*[@id="sidebar"]/ul/li/a[contains(., "Leads")]')

    def customize_leads(self):
        self.click(self._leads)
        return LeadsSourcesPage(self.driver)


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)
        self.settings_navigation_bar = SettingsNavigationBar(self.driver)


# leads settings
class LeadsSourcesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)
        self.settings_navigation_bar = SettingsNavigationBar(self.driver)
        self.lead_settings_bar = LeadSettingsBar(self.driver)


class LeadsStatusesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)
        self.settings_navigation_bar = SettingsNavigationBar(self.driver)
        self.lead_settings_bar = LeadSettingsBar(self.driver)

    def edit_status_name(self, prev_status, new_status):
        edit_button = ('xpath', '//label/h4[contains(., "%s")]/../../div/div/button' % prev_status)
        self.click(edit_button)
        name_field = ('xpath', '//input[@id="name" and @value="%s"]' % prev_status)
        self.send_keys(name_field, new_status)
        save_button = ('xpath', '//input[@id="name" and @value="%s"]/../../../div/div/button' % prev_status)
        self.click(save_button)


class LeadSettingsBar(BasePage):
    _lead_status = ('xpath', '//*[@id="leads-settings-tabs"]/li/a[contains(., "Lead Statuses")]')

    def switch_to_lead_statuses(self):
        self.click(self._lead_status)
        return LeadsStatusesPage(self.driver)
