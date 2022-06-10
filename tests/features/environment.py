from tests.features.DriverFactory import DriverFactory
import sys
BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

def before_feature(context, feature):
    sys.setrecursionlimit(1500)
    driver_factory = DriverFactory()
    context.browser = driver_factory
    # browser=saucelabs or chromelocal
    context.browser.driver = driver_factory.getManager("saucelabs")
    context.browser.driver.get("https://the-internet.herokuapp.com/basic_auth")

def after_step(context, step):
    if hasattr(step, 'status'):
        if hasattr(step.status, 'name'):
            if step.status.name == "failed":
               pass

def after_scenario(context, scenario):
    print("AFTER SCENARIO")

def after_feature(context, feature):
    context.browser.close()
    context.browser.quit()


