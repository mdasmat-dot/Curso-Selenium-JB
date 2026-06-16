from selenium.webdriver.common.by import By

class CompletePage:

    TITLE = ( By.CLASS_NAME,"complete-header")

    def __init__(self, driver):
        self.driver = driver

    def obtener_mensaje(self):

        return self.driver.find_element(*self.TITLE).text