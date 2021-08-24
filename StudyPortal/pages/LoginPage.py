from selene.support import by
from StudyPortal.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    @property
    def login_username(self):
        return self.browser.element(by.xpath("//input[@type='text']"))

    @property
    def login_password(self):
        return self.browser.element(by.xpath("//input[@type='password']"))

    @property
    def login_button(self):
        return self.browser.element(by.xpath("//span[text()='登录']"))

    def openWebSite(self):
        self.browser.open('/')

    def loginPortal(self):
        self.login_username.type("hf3.cn.01")
        self.login_password.type("12345")
        self.login_button.click()
