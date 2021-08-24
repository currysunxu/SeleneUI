from selene.support import by
from selene.support.conditions import have

from Salesforce.pages.BasePage import BasePage


class ToolPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    @property
    def all_rows(self):
        return self.browser.elements(by.xpath("//div[@class ='row listw clearfix']"))

    @property
    def loading(self):
        return self.browser.elements(by.xpath("//div[contains(text(),'正在加载')]"))

    def wait_loading_disappear(self):
        while self.loading.matching(have.text('正在加载')):
            print("loading")
            if not self.loading.matching(have.text('正在加载')):
                break
