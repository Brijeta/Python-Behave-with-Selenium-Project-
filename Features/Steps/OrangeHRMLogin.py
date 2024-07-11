import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@when('I open orange HRM Homepage')
def openHRMHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('Enter username "{user}" and password "{pwd}"')
def enterdataLogin(context,user,pwd):
    WebDriverWait(context.driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']"))).send_keys(user)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))).send_keys(pwd)

@when('Click on login button')
def clickLoginButton(context):
    WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))).click()



@then('User must successfully login to the Dashboard page')
def loginDashboard(context):
    wait= (WebDriverWait(context.driver, 10))
    element =wait.until(
        EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
    text = element.text
    assert text=="Dashboard"
    context.driver.close()
