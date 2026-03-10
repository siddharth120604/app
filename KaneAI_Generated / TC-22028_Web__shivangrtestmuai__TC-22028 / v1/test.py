
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : open https://kaneai-playground.lambdatest.io/
    driver.get("https://kaneai-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Read browser url → {{page_url}}
    page_url = driver.current_url

    print("page_url:", page_url)
    driver.implicitly_wait(6)

    # Step - 3 : Check if page url is google.com or not
    _conditions_v1Qk = [ResolvedCondition.from_string(condition) for condition in ["{{page_url}} == 'https://google.com'"]]
    _connectors_v1Qk = [ConcatenationOperator(connector) for connector in []]
    _condition_v1Qk = Condition(_conditions_v1Qk, _connectors_v1Qk)
    _result_v1Qk, _ = _condition_v1Qk.evaluate(user_variables, get_variable_value)

    if _result_v1Qk:
        print("if is unresolved")

    else:
        print("else is unresolved")

    driver.implicitly_wait(6)

    # Step - 5 : Read browser url → {{page_url_c892ce}}
    page_url_c892ce = driver.current_url

    print("page_url_c892ce:", page_url_c892ce)
    driver.implicitly_wait(6)

    # Step - 6 : Check if page url is google.com or not
    _conditions_it7K = [ResolvedCondition.from_string(condition) for condition in ["{{page_url_c892ce}} == 'https://google.com'"]]
    _connectors_it7K = [ConcatenationOperator(connector) for connector in []]
    _condition_it7K = Condition(_conditions_it7K, _connectors_it7K)
    _result_it7K, _ = _condition_it7K.evaluate(user_variables, get_variable_value)

    if _result_it7K:
        print("if is unresolved")

    else:
        print("else is unresolved")


    driver.quit()
except Exception as e:
    driver.quit()
