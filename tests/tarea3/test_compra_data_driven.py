import logging
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.data_helper import leer_json
from helpers.screenshot_helper import guardar_captura
from helpers.text_helper import textos_son_iguales

from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.cart_page import CartPage
from pages.tarea3.checkout_page import CheckoutPage
from pages.tarea3.complete_page import CompletePage


logger = logging.getLogger(__name__)

datos = leer_json("data/tarea3/inventario.json")

@pytest.mark.data
@pytest.mark.parametrize("caso",datos["casos_agregar_producto"], ids=[c["caso"]for c in datos["casos_agregar_producto"]])

def test_compra_data_driven(driver,caso):

    if caso["caso"] == "caso_forzado_error":
        pytest.xfail("Este caso esta disenado para fallar como prueba de captura de evidencias")

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CompletePage(driver)

    logger.info( f"Ejecutando {caso['caso']}")

    login.abrir()

    
    login.login("standard_user", "secret_sauce")

    guardar_captura(driver,caso["caso"] )

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

    inventory.ordenar(caso["orden"])

    guardar_captura(driver,caso["caso"] )

    producto = inventory.agregar_producto_por_indice( caso["indice_producto"])

   
    assert inventory.obtener_cantidad_carrito() \
           == caso["cantidad_esperada"]

    inventory.abrir_carrito()

    guardar_captura(driver,caso["caso"] )

    producto_carrito = cart.obtener_producto()

    assert textos_son_iguales(producto_carrito, caso["producto_esperado"] )

    cart.checkout()

    guardar_captura(driver,caso["caso"] )

    checkout.llenar_formulario( "Mario","Davila","15001")

    guardar_captura(driver,caso["caso"] )

    checkout.continuar()

    guardar_captura(driver,caso["caso"] )

    checkout.finalizar()

    guardar_captura(driver,caso["caso"] )
    
    mensaje = complete.obtener_mensaje()

    assert textos_son_iguales( mensaje, "Thank You For Your Order!" )

    
