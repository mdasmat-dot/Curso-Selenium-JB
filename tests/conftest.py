import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
 
from pages.clase5.login_page import LoginPage 
from pages.clase5.inventory_page import InventoryPage 
from pages.clase5.alerts_page import AlertsPage 
from pages.clase5.upload_page import UploadPage 

#Navegacion Headless para pruebas sin interfaz grafica, ideal para integracion continua y ejecucion rapida de pruebas.
 
@pytest.fixture 
def driver(): 
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    navegador = webdriver.Chrome(options=chrome_options)
 
    yield navegador 
 
    navegador.quit() 
 
@pytest.fixture(scope="class") 
def driver_class(): 
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    navegador = webdriver.Chrome(options=chrome_options)
    navegador.maximize_window() 
 
    yield navegador 
 
    navegador.quit() 
 
@pytest.fixture 
def login_page(driver): 
    return LoginPage(driver) 
 
@pytest.fixture 
def inventory_page(driver): 
    return InventoryPage(driver)
pytest.fixture(scope="class") 
def login_page_class(driver_class): 
    return LoginPage(driver_class) 
 
@pytest.fixture(scope="class") 
def inventory_page_class(driver_class): 
    return InventoryPage(driver_class) 
 
@pytest.fixture 
def alerts_page(driver): 
    return AlertsPage(driver) 
 
@pytest.fixture 
def upload_page(driver): 
     return UploadPage(driver) 