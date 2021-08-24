from selene.support import by
from Salesforce.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, env):
        BasePage.__init__(self, env)

    @property
    def login_username(self):
        return self.browser.element(by.id("username"))

    @property
    def login_password(self):
        return self.browser.element(by.xpath("//input[@id='password']"))

    @property
    def login_button(self):
        return self.browser.element(by.xpath("//input[@id='Login']"))

    def openWebSite(self):
        self.browser.open('')

    def loginSalesforce(self):
        self.login_username.type("test.eileen.chen@ef.com.qa")
        self.login_password.type("efEF@321")
        self.login_button.click()
