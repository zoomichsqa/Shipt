from selenium.webdriver.common.by import By


def enter_text(driver, by, selector, text):
    element = driver.find_element(by, selector)
    element.clear()
    element.send_keys(text)


def click_on(driver, by, locator):
    element = driver.find_element(by, locator)
    element.click()

def login(driver, username="qatest@shipt.com", password="Sh1pt123!"):
    enter_text(driver, By.XPATH, "//form/div/label[1]/input", username)
    enter_text(driver, By.XPATH, "//form/div/label[2]/input", password)
    driver.find_element_by_id("start_shopping_login_button").click()

