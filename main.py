from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from mongo import MongoConnect

db_client= MongoConnect().client
db= db_client.get_database('Ejercicio_final')
col= db.get_collection('PRODUCTOS')

driver = webdriver.Chrome()
driver.get("https://mikrotik.com/products/group/new")
products = driver.find_elements(By.CLASS_NAME,"product")
for c in products:
    valor=c.find_element(by=By.CLASS_NAME, value="price").text
#    valor = c.find_element(by=By.CLASS_NAME, value="product-info").find_element(by=By.CLASS_NAME, value="price").text
    description = c.find_element(by=By.CLASS_NAME, value="descr").text
    model = c.find_element(by=By.TAG_NAME, value="img").accessible_name

    document={
        "Modelo": model,
        "Descripción": description,
        "Costo": valor
    }
    col.insert_one(document=document)


    print(model)
    print(description)
    print(valor)
    print('*' * 50)

driver.close()