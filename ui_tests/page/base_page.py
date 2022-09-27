from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def click_on_element(self, locator, timeout=10):
        return self.find_element(locator, timeout).click()

    def scroll_to_element(self, locator, timeout=10):
        return self.driver.execute_script("arguments[0].scrollIntoView();",
                                          self.find_element(locator, timeout))

    def navigate_to(self, url):
        return self.driver.get(url)
