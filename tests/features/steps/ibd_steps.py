# Created by jigisha.shah
from behave import *
from nose.tools import eq_
import logging
import time
from tests.features.pages.receivingPage import MainPage

@step(u'User login and clicks on Receiving from menu')
def step_impl(context):
    logging.info('Starting User clicks on Receiving from menu')
    MainPage(context.browser.driver).login_with_autoit()
    time.sleep(2)
    logging.info('Completed User clicks on Receiving from menu')



