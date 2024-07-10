from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
@given('Launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('open Orane hrm homepage')
def openHomePage(context):
    context.driver.get("https://www.orangehrm.com/")


@then('verify that the logo present on page')
def verifyLogo(context):
    status= context.driver.find_element(By.XPATH,"//img[@src='/_resources/themes/orangehrm/dist/images/OrangeHRM_Logo.svg']").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()
