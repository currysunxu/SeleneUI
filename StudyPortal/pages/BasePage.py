import os
import sys
from selene.support.shared import browser, config

sys.path.append(os.path.dirname(__file__))


class BasePage:

    def __init__(self):
        config.browser_name = 'chrome'
        config.base_url = 'https://study-qa.ef.cn/portal/#/login'
        config.timeout = 3
        self.browser = browser
