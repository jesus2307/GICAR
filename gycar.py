from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    # Definir la ruta del archivo de cookies, nombre de usuario, contraseña y URL de inicio de sesión
    ruta_archivo_cookies = "ruta_del_archivo.txt"
    usuario = "nombre_de_usuario"
    contrasena = "contrasena_del_usuario"
    url_login = "https://preproduccio.autenticaciogicar1.extranet.gencat.cat/"
    
    # Inicializar el navegador
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Navegar a la página de inicio de sesión y esperar a que se cargue
    page.goto(url_login)
    page.wait_for_url("https://preproduccio.autenticaciogicar1.extranet.gencat.cat/*")
    
    # Introducir nombre de usuario y contraseña
    page.get_by_placeholder("DNI o NIE").click()
    page.get_by_placeholder("DNI o NIE").fill(usuario)
    page.get_by_placeholder("DNI o NIE").press("Tab")
    page.locator("input[name=\"PASSWORD\"]").fill(contrasena)
    page.locator("input[name=\"PASSWORD\"]").press("Enter")
    
    # Esperar a que la página de inicio de sesión se cargue completamente y esperar un tiempo adicional
    page.wait_for_url(url_login)
    time.sleep(2)
    
    # Crear archivo para guardar las cookies y obtener las cookies de la página actual
    file = open(ruta_archivo_cookies, "w")
    cookies = context.cookies()
    
    # Lista de nombres de cookies que se desean capturar
    lista_cookies = ["nombre_de_cookie_1", "nombre_de_cookie_2"]
    
    # Escribir las cookies en el archivo de texto si el nombre de la cookie está en la lista de cookies
    for cookie in cookies:
        if cookie["name"] in lista_cookies:
            nombre = cookie["name"]
            valor = cookie["value"]
            file.write(f"{nombre}={valor};")
    
    # Cerrar el contexto del navegador, el navegador y el archivo de cookies
    context.close()
    browser.close()
    file.close()

# Ejecutar la función run con Playwright
with sync_playwright() as playwright:
    run(playwright)
