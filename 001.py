from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service())
driver.get("https://es.wikipedia.org/wiki/Louis_Armstrong")

# Captura de un solo elemento
from selenium.webdriver.common.by import By
titulo = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
print(titulo.text)

# Captura de varios elementos
secciones = driver.find_elements(By.TAG_NAME, "h2")
for seccion in secciones:
    print(seccion.text)


# Captura de un elemento 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    element = WebDriverWait(driver= driver,
                            timeout=10,
                            poll_frequency=0.01).until(
            EC.presence_of_element_located((By.ID, "ca-talk"))
        )
    print(element.text)
except Exception as e:
    print("Elemento no encontrado")
