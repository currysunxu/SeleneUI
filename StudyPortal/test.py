from ptest.decorator import TestClass, Test
from selene import by, config
import time
from StudyPortal.pages.LoginPage import LoginPage
from StudyPortal.pages.PtReviewPage import PtReviewPage
from StudyPortal.pages.HomePage import HomePage


@TestClass()
class test():

    @Test(data_provider=[("Take Test","You can take the test now."),("Continue","You can continue your test."),("View Result","")])
    def test_whole_flow(self):
        print("hello world")
        login = LoginPage()
        login.openWebSite()
        login.loginPortal()
        home = HomePage()
        home.open_ptreview()
        pt_review = PtReviewPage()
        pt_review.switch_specific_book("D")
        pt_review.check_before_test_text()
        time.sleep(3)

    @Test(data_provider=[("Take Test","You can take the test now."),("Continue","You can continue your test."),("View Result","")])
    def test_whole_flow1(self,status,desc):
        print(status)
        print(desc)
