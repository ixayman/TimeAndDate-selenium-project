from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def accept_cookies_pop(driver):
    try:
        # Wait for the "AGREE" button to be present and click it
        WebDriverWait(driver, 2).until(ec.presence_of_element_located
                                       ((By.XPATH, '//span[text()="AGREE"]'))).click()
    except:
        # If the "AGREE" button does not appear within the timeout, ignore the exception
        pass
