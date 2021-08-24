import time

from Salesforce.pages.LeadPage import LeadPage

class LeadAction:

    @staticmethod
    def create_new_lead():
        leadPage = LeadPage()
        leadPage.choose_leads()
        leadPage.open_new_leads()
        leadPage.open_continue_leads()
        username = leadPage.input_account_last_name()
        leadPage.input_center()
        leadPage.input_random_mobile()
        leadPage.select_marketing_channel_group()
        leadPage.select_marketing_channel()
        leadPage.click_save()
        print('lead created successfully,whose name is {0}'.format(username))
        time.sleep(5)

    @staticmethod
    def create_opptunity():
        leadPage = LeadPage()