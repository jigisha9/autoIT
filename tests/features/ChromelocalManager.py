# Created by by Jigisha.shah
from abc import ABC
from selenium import webdriver
from tests.features.DriverManager import DriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
caps = {}
build = int(time.time())


def createDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-core-security")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-infobars")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    capabilities["prerun"] = {"executable": "storage:filename=autoit.exe", "args": ["--silent", "-a", "-q"], "background": True}
    driver = webdriver.Chrome(executable_path='webdrivers/chromedriver.exe', desired_capabilities=capabilities, options=options)
    return driver

class ChromelocalManager(DriverManager, ABC):

    def __init__(self):
        self.driver = None

    def getDriver(self):
        if not self.driver:
            self.driver = createDriver()
        return self.driver
