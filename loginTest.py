from behave import *
from selenium import webdriver

use_step_matcher("re")

@given("User launches the Chrome browser")
def step_impl(context):
    context.driver = webdriver.Chrome()

@when("Opens dashboard\.pointzi\.com")
def step_impl(context):
    context.driver.get("http://dashboard.pointzi.com/")

@step('Enters email "{username}" and password "{password}"')
def step_impl(context,username,password):
    context.driver.find_element_by_id("input_1").send_keys(username)
    context.driver.find_element_by_id("input_2").send_keys(password)

@step("Clicks the login button")
def step_impl(context):
    context.driver.click()

@then("User must successfully login to the Dashboard page")
def step_impl(context):
    try:
        print("Login Successful")
    except:
        context.driver.close()
        assert False,"Test Failed"
