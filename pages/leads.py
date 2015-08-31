from pages.base import BasePage, NavigationBar


class LeadsPage(BasePage):
    _new_leads_button = ('id', 'leads-new')

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)

    def add_new_lead(self):
        self.click(self._new_leads_button)
        return NewLeadPage(self.driver)

    def select_lead(self, lead):
        lead_row = ('xpath', '//div/h3/a[contains(., "%s%s%s")]' % (lead['first_name'], ' ', lead['last_name']))
        self.click(lead_row)
        return LeadPage(self.driver)


class LeadPage(BasePage):
    _status = ('css', '.lead-status')
    _delete_button = ('css', '#actions > a.btn.delete')

    @property
    def lead_status(self):
        return self.get_element(self._status).text

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)

    def delete_lead(self):
        self.click(self._delete_button)
        delete_lead_modal = DeleteLeadModal(self.driver)
        delete_lead_modal.confirm_remove_lead()


class NewLeadPage(BasePage):
    _first_name_field = ('id', 'lead-first-name')
    _last_name_field = ('id', 'lead-last-name')
    _save_button = ('xpath', '//button[contains(., "Save")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_bar = NavigationBar(self.driver)

    def type_first_name(self, first_name):
        self.send_keys(self._first_name_field, str(first_name))

    def type_last_name(self, last_name):
        self.send_keys(self._last_name_field, str(last_name))

    def save_new_lead(self):
        self.click(self._save_button)
        return LeadPage(self.driver)


class DeleteLeadModal(BasePage):
    _remove_button = ('xpath', '//div/div/div/a[contains(., "Remove")]')

    def confirm_remove_lead(self):
        from time import sleep
        sleep(1)
        self.click(self._remove_button)
