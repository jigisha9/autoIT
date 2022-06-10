from abc import ABC
from json import loads, dumps
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from tests.features.DriverManager import DriverManager
from pathlib import Path
import json

def createDriver():
    browser_setup = loads(dumps(read_file_from_path("features", "sauce_labs_setup.json")))
    browser_args = 'args'
    chrome_options = 'chromeOptions'
    selenium_host = 'sauceHost'
    username = 'sauceUser'
    access_key = 'sauceKey'

    # Add the capabilities
    caps = DesiredCapabilities.CHROME
    for k, v in browser_setup.items():
        print(k)
        if 'deviceProperties' not in k and selenium_host not in k:
            caps[k] = v


    options = webdriver.ChromeOptions()
    # Add the webdriver options
    if browser_args in browser_setup:
        for value in browser_setup[chrome_options][browser_args]:
            options.add_argument(value)

    remote_url = browser_setup[selenium_host].format(browser_setup[username], browser_setup[access_key])

    print(remote_url)

    driver = webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=caps,
        options=options
    )
    return driver

def read_file_from_path(base_ui_directory, file_name):
    path = Path(__file__).parent.parent.joinpath(base_ui_directory).joinpath(file_name)
    print(path)
    with path.open(mode='r') as f:
        return json.load(f)

class SauceLabsManager(DriverManager, ABC):

    def __init__(self):
        self.driver = None

    def getDriver(self):
        if not self.driver:
            self.driver = createDriver()

        return self.driver
