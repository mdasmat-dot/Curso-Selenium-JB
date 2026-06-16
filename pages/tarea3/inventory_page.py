from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    SORT_SELECT = (By.CSS_SELECTOR,"[data-test='product-sort-container']" )

    PRODUCTOS = ( By.CSS_SELECTOR, ".inventory_item")

    PRODUCT_NAME = ( By.CLASS_NAME, "inventory_item_name")

    #ADD_BUTTON = ( By.TAG_NAME,"button")

    #Localizador mas especifico para el boton de agregar al carrito, buscando el boton dentro del producto especifico
    ADD_BUTTON = (By.CSS_SELECTOR,"button.btn_inventory")

    CART_BADGE = (By.CLASS_NAME,"shopping_cart_badge" )

    CART_LINK = ( By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ordenar(self, valor):

        select_element = self.wait.until(EC.visibility_of_element_located(self.SORT_SELECT) )
        select = Select(select_element)
        select.select_by_value(valor)

    def obtener_producto_por_indice(self, indice):

        self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCTOS ))

        productos = self.driver.find_elements(*self.PRODUCTOS)

        return productos[indice]

    def agregar_producto_por_indice(self, indice):

        producto = self.obtener_producto_por_indice(indice)

        nombre = producto.find_element(*self.PRODUCT_NAME).text

        producto.find_element(*self.ADD_BUTTON).click()

        return nombre

    #def obtener_cantidad_carrito(self):

        #return self.wait.until(EC.visibility_of_element_located( self.CART_BADGE) ).text

    #Metodo mejorado para obtener la cantidad del carrito, manejando el caso donde el carrito esta vacio y no se muestra el badge

    def obtener_cantidad_carrito(self):

        badge = self.wait.until(EC.presence_of_element_located(self.CART_BADGE))
        return badge.text

    def abrir_carrito(self):

        self.wait.until(EC.element_to_be_clickable(self.CART_LINK) ).click()