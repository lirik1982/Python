from selenium import webdriver

import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    print("Launching Chrome...............")
    return driver

# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome...............")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#     elif browser == 'IE':
#         driver = webdriver.Ie()
#     return driver

# def pytest_addobtion(parser):
#     parser.addoption('--browser', action='store',
#                      default='chrome')
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")



# ############### HTML REPORT ################################
# def pytest_config(config):
#   config._metedata['Project Name'] = 'nop Commerce'
#   config._metedata['Module Name'] = 'Customers'
#   config._metedata['Tester'] = 'Pavan'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME', None)
#     metadata.pop('Plugins', None)
#
#
