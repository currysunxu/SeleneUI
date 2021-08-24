from selene.support import by
from StudyPortal.pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    @property
    def progress_test(self):
        return self.browser.element(by.xpath("//div[text()='Progress Test']"))

    def open_ptreview(self):
        self.progress_test.click()
