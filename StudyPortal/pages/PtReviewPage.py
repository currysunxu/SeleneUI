from selene import by, be, have
from StudyPortal.pages.BasePage import BasePage


class PtReviewPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    @property
    def switch_book_button(self):
        return self.browser.element(by.xpath("//span[text()='Progress Test']/ancestor::div//button"))

    @property
    def previous_button(self):
        return self.browser.element(by.xpath("//div[@class='swiper-button-prev']"))

    @property
    def specify_book(self, book_name):
        return self.browser.element(
            by.xpath("//span[text()='Book {0}']/preceding-sibling::div/a/img".format(book_name)))

    @property
    def start_test(self,status):
        return self.browser.element(by.text(status))

    @property
    def start_test_text(self,description):
        return self.browser.element(by.text(description))

    def switch_specific_book(self, book_name):
        self.switch_book_button.click()
        if self.previous_button.is_displayed():
            self.previous_button.click()
        if self.specify_book(book_name).is_displayed():
            self.specify_book(book_name).click()

    def check_before_test_text(self,status,description):
        self.start_test(status).with_(timeout=3).should(have.text(status))
        self.start_test_text(description).with_(timeout=3).should(have.text(description))
