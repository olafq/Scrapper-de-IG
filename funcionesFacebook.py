from funcionesGenerales import *

def Ingresar_a_facebook(us,pas):
    #inicializo google 
    driver = inicializarChrome()
    #Iir a la pagina de instagram 
    driver.get('https://www.facebook.com/?locale=es_LA')
    ingresar_us_cont(driver,us,pas)
    #inicia sesion 
    driver.find_element(By.NAME,'login').click()
    time.sleep(100)
    
 

def ingresar_us_cont(driver,us,pas):
    print(pas)
    # Espera hasta que el elemento esté presente en la página
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    # Ingresa el nombre de usuario en el campo usuario de la web
    username_input.send_keys(us)
    # Espera hasta que el elemento esté presente en la página
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'pass')))
    # Ingresa la contraseña en el campo contraseña de la web
    username_input.send_keys(pas)