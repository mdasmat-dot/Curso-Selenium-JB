from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CartPage:

    ITEM_NAME = (By.CLASS_NAME,"inventory_item_name")

    CHECKOUT_BUTTON = ( By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_producto(self):

        return self.driver.find_element(*self.ITEM_NAME).text
    
        logger.info(f"Cantidad productos encontrados: {len(productos)}")

        for i, p in enumerate(productos):
            logger.info(f"Producto {i}: {p.text}")
            return productos[0].text

    def checkout(self):

        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()