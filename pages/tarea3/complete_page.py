from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CompletePage:

    TITLE = ( By.CLASS_NAME,"complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_mensaje(self):

        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text