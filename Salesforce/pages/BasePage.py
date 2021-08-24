import os
import sys

from selene.support.shared import browser, config

from Salesforce.config import yaml_cfg, env_key

sys.path.append(os.path.dirname(__file__))


class BasePage:
    def __init__(self, environment='Saesforce'):
        config.browser_name = 'chrome'
        config.base_url = self.get_current_env(environment)
        config.timeout = 5
        self.browser = browser

    def get_current_env(self, specific_env):

        env = ''
        try:
            env = yaml_cfg.get(specific_env)[str.upper(env_key)]
        except Exception as e:
            print(
                "{0} do not define in {1} env, just skip it, please double check if it's necessary".format(specific_env,
                                                                                                           env_key))
        finally:
            return env

    def quitBrowser(self):
        self.browser.quit()
