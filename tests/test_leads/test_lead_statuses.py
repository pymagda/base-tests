import pytest
from unittestzero import Assert
from pages.login import LoginPage

@pytest.mark.usefixtures('driver_setup')
class TestLeads:
    def test_change_lead_status_name(self, user, lead, lead_statuses):
        login_page = LoginPage(self.driver)
        main_page = login_page.log_in(user['email'], user['password'])
        leads_page = main_page.navigation_bar.switch_to_leads()
        new_lead_page = leads_page.add_new_lead()
        new_lead_page.type_first_name(lead['first_name'])
        new_lead_page.type_last_name(lead['last_name'])
        lead_page = new_lead_page.save_new_lead()
        Assert.equal(lead_page.lead_status, lead_statuses['prev_status'])
        profile_page = lead_page.navigation_bar.switch_to_settings()
        leads_sources_page = profile_page.settings_navigation_bar.customize_leads()
        leads_statuses_page = leads_sources_page.lead_settings_bar.switch_to_lead_statuses()
        leads_statuses_page.edit_status_name(lead_statuses['prev_status'], lead_statuses['new_status'])
        leads_statuses_page.navigation_bar.switch_to_leads()
        lead_page = leads_page.select_lead(lead)
        Assert.equal(lead_page.lead_status, lead_statuses['new_status'])

        # clean up
        lead_page.delete_lead()
        lead_page.navigation_bar.switch_to_settings()
        leads_sources_page = profile_page.settings_navigation_bar.customize_leads()
        leads_statuses_page = leads_sources_page.lead_settings_bar.switch_to_lead_statuses()
        leads_statuses_page.edit_status_name(lead_statuses['new_status'], lead_statuses['prev_status'])

        leads_statuses_page.navigation_bar.log_out()
