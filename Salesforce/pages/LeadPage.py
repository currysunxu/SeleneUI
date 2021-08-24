from selene.support import by
from selene.support.conditions import have

from Salesforce.Utils.CommonUtils import CommonUtils
from Salesforce.pages.BasePage import BasePage


class LeadPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    @property
    def leads(self):
        return self.browser.element(by.text("Leads"))

    @property
    def new_lead(self):
        return self.browser.element(by.name("new"))

    @property
    def continue_lead(self):
        return self.browser.element(by.xpath("//input[@Value='Continue']"))

    @property
    def account_last_name(self):
        return self.browser.element(by.id("name_lastlea2"))

    @property
    def center(self):
        return self.browser.element(
            by.xpath('//label[text()="Center (Pref.)"]/parent::td/following-sibling::td//span/input'))

    @property
    def mobile(self):
        return self.browser.element(
            by.xpath('//label[contains(text(),"Main Mobile")]/parent::td/following-sibling::td/div/input'))

    @property
    def marketing_channel_group(self):
        return self.browser.element(
            by.xpath('//label[text()="Marketing Channel Group"]/parent::td/following-sibling::td//select'))

    @property
    def marketing_channel(self):
        return self.browser.element(
            by.xpath('//label[text()="Marketing Channel"]/parent::td/following-sibling::td//select'))

    @property
    def submit_save(self):
        return self.browser.element(by.xpath('//input[@title="Save"]'))

    def choose_leads(self):
        self.leads.click()

    def open_new_leads(self):
        self.new_lead.should(have.attribute("class", "btn")).click()

    def open_continue_leads(self):
        self.continue_lead.should(have.attribute("class", "btn")).click()

    def input_account_last_name(self):
        random_last_name = CommonUtils.random_gen_str()
        self.account_last_name.should(have.attribute("type", "text")).type(random_last_name)
        return random_last_name

    def input_center(self):
        self.center.should(have.attribute("type", "text")).type("CN OMNI Test")

    def input_random_mobile(self):
        self.mobile.should(have.attribute("type", "text")).type(CommonUtils.random_gen_number())

    def select_marketing_channel_group(self):
        self.marketing_channel_group.send_keys("ALT")

    def select_marketing_channel(self):
        self.marketing_channel.send_keys("Direct Mail")

    def click_save(self):
        self.submit_save.should(have.attribute("type", "submit")).click()
