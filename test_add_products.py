#from __future__ import absolute_import
import unittest
from selenium.webdriver.support import expected_conditions as EC
from pytractor.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait

from lib.page_obj import *


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://www.shipt.com/"
        self.driver = Chrome('http://localhost:8080/base_url')

    def test_store(self):
        driver = self.driver
        driver.get_page(self.base_url)
        wait = WebDriverWait(driver, 10)

        #Entering the account login page
        login_btn = driver.find_element_by_xpath("//ul[2]/li[3]/a")
        login_btn.click()

        #login to the Shipt account
        login(driver)

        #searching for the 1st product from the menu, asserting it's name and price, adding to the cart
        menu = "//ion-view/div/button[1]"
        click_on(driver, By.XPATH, menu)
        baby = "//div[2]/ion-list/div/ion-item[1]"
        click_on(driver, By.XPATH, baby)

        first_product = driver.find_element_by_xpath("//div[(@class='row responsive-md')]/div[1]/"
                                                     "ion-item/div[1]/p").text.strip()
        print "First product: ", first_product

        first_product_price = driver.find_element_by_xpath("//div[1]/ion-item/div[1]/div[5]/p[2]/span[1]").text[1:]
        print "First product price: ", first_product_price

        add_button = "//div[(@class='row responsive-md')]/div[1]/ion-item/div/div[4]/button[2]"
        click_on(driver, By.XPATH, add_button)

        #If the cart price equals fist product price after adding
        cart_price_main = driver.find_element_by_xpath("//div[3]/span/web-cart-button/button").text.replace("$", "")
        print "Cart price is: ", cart_price_main

        home_button = ".//*[@id='productsIonContent']/div/div/div[1]/div[1]/div[1]"
        click_on(driver, By.XPATH, home_button)

        #searching for 2nd item in the search field
        search_field = "//div[2]/ion-header-bar//form/label/input"
        search_text = "Banana"
        enter_text(driver, By.XPATH, search_field, search_text)

        second_product = driver.find_element_by_xpath("//div/div[1]/div/div/div[1]/ion-item/div[1]/p").text.strip()
        print "Second product: ", second_product
        second_product_price = driver.find_element_by_xpath("//div[1]/ion-item/div[1]/div[5]/p[2]/span[1]").text[1:]
        print "Second product price: ", second_product_price

        button_add = "//div[1]/div/div/div[1]/ion-item/div[1]/div[4]/button[2]"
        click_on(driver, By.XPATH, button_add)


        home = driver.find_element_by_xpath("//ion-nav-bar/div[2]/ion-header-bar/div[1]/span[1]"
                                            "/web-home-logo-button/button")
        home.click()

        #Going to the cart
        cart_btn = "html/body/ion-nav-view/ion-side-menus/ion-side-menu-content/ion-nav-bar/div[2]" \
                   "/ion-header-bar/div[3]/span/web-cart-button/button"
        wait.until(EC.visibility_of_element_located((By.XPATH, cart_btn)))
        click_on(driver, By.XPATH, cart_btn)

        #Checking items in cart and assert it then (name and the price)
        item_1_in_cart = driver.find_element_by_xpath("//ion-content/div/div/div[1]/div[1]/div/div[2]"
                                                      "/div[3]/div/p").text.strip()
        print "Item1 in cart: ", item_1_in_cart
        price_item_1_in_cart = driver.find_element_by_xpath(
            "//ion-content/div/div/div[1]/div[1]/div/div[2]/div[1]/p/span").text[1:]
        print price_item_1_in_cart

        item2_in_cart = driver.find_element_by_xpath("//div/div/div[1]/div[1]/div/div[3]/div[3]/div/p").text.strip()
        print "Item2 in cart: ", item2_in_cart
        price_item_2_in_cart = driver.find_element_by_xpath("//ion-content/div/div/div[1]/div[1]/div/div[3]"
                                                            "/div[1]/p/span").text[1:]
        print price_item_2_in_cart

        self.assertEqual(first_product_price, price_item_1_in_cart, "Product 1 price doesn't match")
        self.assertEqual(first_product, item_1_in_cart, "Product 1 doesn't match")
        print "First product match in cart"

        self.assertEqual(second_product_price, price_item_2_in_cart, "Product 2 price doesn't match")
        self.assertEqual(second_product, item2_in_cart, "Product 2 doesn't match")
        print "Second product match in cart"

        #Empty cart after the assertion is done
        empty_cart = "empty-cart"
        click_on(driver, By.CLASS_NAME, empty_cart)

        button_yes = "//div[(@class='popup-container popup-showing active')]/div/div[3]/button[2]"
        wait.until(EC.visibility_of_element_located((By.XPATH, button_yes)))
        click_on(driver, By.XPATH, button_yes)

        #Checking the Subtotal price is 0.00 after the removing items from cart
        Subtotal = (driver.find_element_by_xpath("//ion-content//div[2]/div[2]/div/div/div[1]/div[2]").text[1:])
        print "Subtotal: ", Subtotal
        subtotal = float(Subtotal)
        self.assertEqual(subtotal, 0.00, "Subtotal assertion failed")
        print "Test is done"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
