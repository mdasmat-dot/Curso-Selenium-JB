from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def llenar_formulario(self, nombre, apellido,codigo):

        self.wait.until( EC.visibility_of_element_located( self.FIRSTNAME) ).send_keys(nombre)

        self.wait.until(EC.visibility_of_element_located(self.LASTNAME)).send_keys(apellido)

        self.wait.until(EC.visibility_of_element_located(self.POSTAL)).send_keys(codigo)

    def continuar(self):

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def finalizar(self):

        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()