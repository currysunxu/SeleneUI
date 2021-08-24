from selene.support import by
from selene.support.conditions import have

from Salesforce.pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    @property
    def all_tabs(self):
        return self.browser.element(by.xpath("//img[@class = 'allTabsArrow']"))

    def open_all_tabs(self):
        self.all_tabs.should(have.attribute("class", "allTabsArrow")).click()
