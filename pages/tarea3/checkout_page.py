import time
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

    def _escribir_texto_seguro(self, locator, texto):
        for i in range(3):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.click()
            element.clear()
            element.send_keys(texto)
            try:
                WebDriverWait(self.driver, 5).until(lambda d: element.get_attribute("value") == texto)
                return
            except Exception as e:
                try:
                    val = element.get_attribute("value")
                except Exception as ex:
                    val = f"Error obteniendo valor: {ex}"
                print(f"[Intento {i+1}] Error escribiendo en {locator}. Valor actual: '{val}'. Excepcion: {e}")
                time.sleep(0.5)
        raise AssertionError(f"No se pudo escribir el texto '{texto}' en el elemento {locator}")

    def llenar_formulario(self, nombre, apellido, codigo):
        # Espera de cortesía para permitir que React termine de vincular los campos en ambientes CI lentos
        time.sleep(0.5)
        self._escribir_texto_seguro(self.FIRSTNAME, nombre)
        self._escribir_texto_seguro(self.LASTNAME, apellido)
        self._escribir_texto_seguro(self.POSTAL, codigo)

    def continuar(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def finalizar(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH)).click()