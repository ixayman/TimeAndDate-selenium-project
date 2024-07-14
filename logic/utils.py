from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def accept_cookies_pop(driver):
    try:
        WebDriverWait(driver, 2).until(ec.presence_of_element_located
                                       ((By.XPATH, '//span[text()="AGREE"]'))).click()
    except:
        pass
