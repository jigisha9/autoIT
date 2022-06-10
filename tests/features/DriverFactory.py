from tests.features.SauceLabsManager import SauceLabsManager
from tests.features.ChromelocalManager import ChromelocalManager


class DriverFactory:
    def __init__(self):
        self.driver = None

    def getManager(self, browser_name=None):
        # Which is the browser that we ar going to use
        browser = browser_name
        print(browser)
        if not browser_name:
            browser = 'chromelocal'

        elif browser == 'chromelocal':
            self.driver = ChromelocalManager.getDriver(self)

        elif browser == 'saucelabs':
            self.driver = SauceLabsManager.getDriver(self)

        return self.driver

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()