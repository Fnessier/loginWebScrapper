from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
import time

# Configurar el logging
logging.basicConfig(filename='automatizacion.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Inicializar el navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

#Comentar las siguientes lineas para ejecutar sin la ventana de navegador
#options = Options()
#options.add_argument("--headless")
#driver = webdriver.Chrome(options=options)

# Funcion ingreso credenciales
def logginF(email, password):
    try:
        # Esperar y encontrar los elementos
        email_field = wait.until(EC.presence_of_element_located((By.ID, "login-email")))            #buscar los ID de elementos en la pagina web
        password_field = wait.until(EC.presence_of_element_located((By.ID, "login-password")))

        # Ingresar datos y hacer clic
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_field.click()
        actions.send_keys(Keys.ENTER) # Enter porque no se obtiene el elemento del boton avanti (averiguar captchas)
        actions.perform()
    except:
        pass

# Funcion de carga correcta de pagina
def unavailable(link):
    enterPage = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html"),))
    # Testeo de entrada o carga pagina "Unavailable"
    i = 0
    while "Unavailable" in enterPage[0].text:
        driver.get(link)
        logginF(email, password)
        enterPage = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html"),))
        i +=1
        if i>=3:
            raise Exception("No se pudo iniciar sesión después de 3 intentos.")

# Credenciales
email = "juancito@email.com"  #tu email
password = "Juancito123"            #tu password

try:
    # Abrir la página y maximizar la ventana
    linkPrinc = "https://paginaweb.org"       #URL de la web a ingresar
    driver.get(linkPrinc)
    driver.maximize_window()

    logginF(email, password)
    unavailable(linkPrinc)
            
    #Seleccion elemento Reserva 'Reconstruccion Iuris Sanguinis' y click O usamos url
    linkRes = "https://paginaweb.org/Services/Booking/974"
    driver.get(linkRes) #uso de URL mas simple
    unavailable(linkRes)

    # Registrar acción exitosa
    logging.info("Se ha hecho clic en el botón 'Reservar'.")

    # Registrar No hay turnos disponibles
    confm = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "jc-bs3-container container" ), ))       #buscar CLASS o ID necesario
    if "Sorry, all appointments for " in confm[0].text :
        logging.info("No hay turnos disponibles.")
        driver.quit()
    else:
        time.sleep(360000)

except Exception as e:
    # Registrar error
    logging.error(f"Ocurrió un error: {e}")

# Mantener el navegador abierto
# driver.quit()  # Comentar esta línea para mantener el navegador abierto

finally:
    # Cerrar el navegador si hay algún error
    driver.quit()