from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, usuario, password):

        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(usuario)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

         
    def obtener_mensaje_error(self):
        mensaje_error = self.driver.find_element(*self.ERROR_MESSAGE)
        return mensaje_error.text