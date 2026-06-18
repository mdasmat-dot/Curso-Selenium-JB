import logging
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.tarea3.data_helper import leer_json
from helpers.tarea3.screenshot_helper import guardar_captura
from helpers.tarea3.text_helper import textos_son_iguales
from helpers.tarea3.allure_helper import adjuntar_error

from pages.tarea3.login_page import LoginPage
from pages.tarea3.inventory_page import InventoryPage
from pages.tarea3.cart_page import CartPage
from pages.tarea3.checkout_page import CheckoutPage
from pages.tarea3.complete_page import CompletePage

logger = logging.getLogger(__name__)

datos = leer_json(
    "data/tarea3/inventario.json"
)

@allure.epic("E-commerce")
@allure.feature("Proceso de Compra")
@allure.story("Compra exitosa de producto")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Integrador Final")

@pytest.mark.data
@pytest.mark.regression
@pytest.mark.critical
@pytest.mark.coverage
@pytest.mark.smoke
@pytest.mark.parametrize(
    "caso",
    datos["casos_agregar_producto"],
    ids=[c["caso"] for c in datos["casos_agregar_producto"]]
)
def test_integrador(driver, caso):

    if caso["caso"] == "caso_forzado_error":
        pytest.xfail("Este caso esta disenado para fallar como prueba de captura de evidencias")

    try:

        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)
        complete = CompletePage(driver)

        logger.info(f"Ejecutando {caso['caso']}")

        with allure.step("Login"):
            login.abrir()
            login.login(
                "standard_user",
                "secret_sauce"
            )

        with allure.step("Validar inventario"):
            WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
                   
            assert "inventory" in driver.current_url

        with allure.step("Ordenar productos"):
            inventory.ordenar(caso["orden"])

        with allure.step("Agregar producto"):
            inventory.agregar_producto_por_indice(
                caso["indice_producto"]
            )

        with allure.step("Validar carrito"):
            assert inventory.obtener_cantidad_carrito() \
                   == caso["cantidad_esperada"]

        inventory.abrir_carrito()

        with allure.step("Validar producto"):
            producto_carrito = cart.obtener_producto()

            assert textos_son_iguales(
                producto_carrito,
                caso["producto_esperado"]
            )

        with allure.step("Checkout"):
            cart.checkout()

            checkout.llenar_formulario(
                "Mario",
                "Davila",
                "15001"
            )

            checkout.continuar()
            checkout.finalizar()

        with allure.step("Validar mensaje final"):

            mensaje = complete.obtener_mensaje()

            assert textos_son_iguales(
                mensaje,
                "Thank You For Your Order!"
            )

    except Exception as e:

        logger.error(str(e))

        allure.attach(
            str(e),
            name="mensaje_error",
            attachment_type=allure.attachment_type.TEXT
        )

        ruta = guardar_captura(
            driver,

            f"error_{caso['caso']}"
        )

        adjuntar_error(ruta)

        raise