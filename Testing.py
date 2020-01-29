#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import subprocess

__author__ = 'Guido Parra'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#for x in range(8):
 #  os.system('taskkill /f /T /im "chrome.exe" >nul 2>&1')
 
driver = webdriver.Chrome('./Webdrivers/chromedriver')
driver.get("http://automationpractice.com/index.php")

driver.maximize_window()#agranda la pantalla

print (driver.title)

"//h1[@class='page-heading  product-listing']//span[@class='lighter'][contains(text(),'Blouse')]"


# Valida condición PASSED FAILED
try:
    assert "My Store" in driver.title
    print("Se encontró el título esperado: Passed")
except Exception as inst:
    print("No se encontró el título esperado: Failed")
    

#BUSCAR BLOUSE 
search_bar = driver.find_element_by_name("search_query")
search_bar.clear()
search_bar.send_keys("Blouse")

search_btn = driver.find_element_by_name("submit_search")
search_btn.click()

#COMPRAR  
blouse = driver.find_element_by_xpath("//img [@class='replace-2x img-responsive'][@src='http://automationpractice.com/img/p/7/7-home_default.jpg'][@alt='Blouse'][@title='Blouse'][@itemprop='image']")
blouse.click()

# Valida condición PASSED FAILED
try:
    assert "Blouse - My Store" in driver.title
    print("Se encontró el título esperado: Passed")
except Exception as inst:
    print("No se encontró el título esperado: Failed")

time.sleep (2)   
    
#Agregar al carrito
add_car = driver.find_element_by_id("add_to_cart")
add_car.click()

#Proceder a agregar al carrito
compra = driver.find_element_by_xpath("//*[@id='layer_cart']/div[1]/div[2]/div[4]/a/span")
time.sleep (3)
compra.click() 

# Valida condición PASSED FAILED
try:
    assert "Order - My Store" in driver.title
    print("Se encontró el título esperado: Passed")
except Exception as inst:
    print("No se encontró el título esperado: Failed")

time.sleep (3)

#Procede a la compra
compra_final = driver.find_element_by_xpath("//*[@id='center_column']/p[2]/a[1]/span")
time.sleep (3)
compra_final.click()

# Valida condición PASSED FAILED
try:
    assert "Login - My Store" in driver.title
    print("Se encontró el título esperado: Passed")
except Exception as inst:
    print("No se encontró el título esperado: Failed")

time.sleep (2)

# Crear cuenta Email
email = driver.find_element_by_id ("email_create").send_keys("test@gmail.com");
time.sleep (2)

#Boton de crear cuenta
create_account = driver.find_element_by_xpath ("//*[@id='SubmitCreate']/span")
create_account.click()
time.sleep (2)

#Verificación del mensaje de error 1
error1 = driver.find_element_by_xpath("//*[@id='create_account_error']/ol/li").text
assert error1 == "An account using this email address has already been registered. Please enter a valid password or request a new one."
print ("Mensaje de error 1 ya existe la cuenta: correcto")

#limpiar el campo email
email = driver.find_element_by_id ("email_create").clear()
create_account.click()

time.sleep (5)

#Verificación del mensaje de error 2

error2 = driver.find_element_by_xpath("//*[@id='create_account_error']/ol/li").text
assert error2 == "Invalid email address."
print ("Mensaje de error 2 campo vacio: correcto")

#limpiar el campo email
email = driver.find_element_by_id ("email_create").clear()
time.sleep (2)
email = driver.find_element_by_id ("email_create").send_keys("testing_0011@gmail.com");

create_account = driver.find_element_by_xpath ("//*[@id='SubmitCreate']/span")
create_account.click()	
time.sleep (3)

# Valida condición PASSED FAILED
try:
    assert "Login - My Store" in driver.title
    print("Se encontró el título esperado: Passed")
except Exception as inst:
    print("No se encontró el título esperado: Failed")

#LLenar los campos correctamente

Gender = driver.find_element_by_id ("id_gender1") #checkbox
time.sleep (3)
Gender.click()

first_name = driver.find_element_by_id ("customer_firstname").send_keys("Guido"); #campo nombre
last_name = driver.find_element_by_id ("customer_lastname").send_keys("Parra"); #campo apellido
password = driver.find_element_by_id ("passwd").send_keys("hola123"); #campo password
time.sleep (2)

day = driver.find_element_by_id("days")#Ingreso de Dia
day.click()
day.send_keys("29")
day.click()

month = driver.find_element_by_id("months")#Ingreso de Mes
month.click()
month.send_keys("March")
month.click()

year = driver.find_element_by_id("years")#Ingreso de Año
year.click()
year.send_keys("1980")
year.click()

check_box1 = driver.find_element_by_id ("newsletter").click() # check box
check_box2 = driver.find_element_by_id ("optin").click() # check box
company = driver.find_element_by_id ("company").send_keys("VATES"); #campo de empresa
address = driver.find_element_by_id ("address1").send_keys("Billinghurst 1833"); #campo de direccion
city = driver.find_element_by_id ("city").send_keys("CABA"); #campo de empresa

state = driver.find_element_by_id("id_state")#Ingreso Estado
state.click()
state.send_keys("Texas")
state.click()

postcode = driver.find_element_by_id("postcode")#Ingreso de codigo postal
postcode.click()
postcode.send_keys("00000")


phone_mobile = driver.find_element_by_id("phone_mobile")#Ingreso de telefono mobil
phone_mobile.click()
phone_mobile.send_keys("1111111111")


register = driver.find_element_by_xpath ("//*[@id='submitAccount']/span")#Hacer click en registrarse
register.click()

#address = driver.find_element_by_xpath ("//*[@id='order_step']/li[3]/span").text #validacion en Adress
#assert address == "Address"

#print ("Todo va ok")


time.sleep (10)
#driver.close()



    






