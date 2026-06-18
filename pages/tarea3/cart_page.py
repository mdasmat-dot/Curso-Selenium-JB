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
        # Asegura que el navegador haya terminado de cargar la página del carrito
        self.wait.until(EC.url_contains("cart.html"))
        return self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME)).text

    def checkout(self):
        btn = self.wait.until(EC.presence_of_element_located(self.CHECKOUT_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)