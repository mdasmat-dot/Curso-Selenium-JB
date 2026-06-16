from selenium.webdriver.common.by import By

class CartPage:

    ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")

    CHECKOUT_BUTTON = ( By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def obtener_producto(self):

        return self.driver.find_element(*self.ITEM_NAME).text

    def checkout(self):

        self.driver.find_element(*self.CHECKOUT_BUTTON).click()