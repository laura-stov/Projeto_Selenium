from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def adicionarProduto(lista):
    itens = (driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_'))
    
    for item in itens:
        cel_nome = item.find_element(By.CLASS_NAME, 'ProductCard_ProductCard_Name__U_mUQ').text
        cel_preco = item.find_element(By.CLASS_NAME, 'Text_MobileHeadingS__HEz7L').text

        produto = ((cel_nome, cel_preco))
        lista.append(produto)

        
driver = webdriver.Edge()
driver.get('https://www.zoom.com.br/')

#concordando com os termos do site
popup = driver.find_element(By.CLASS_NAME, 'PrivacyPolicy_Button__1RxwB')
popup.click()

sleep(3)
pesquisa = driver.find_element(By.CLASS_NAME, 'AutoCompleteStyle_autocomplete__BvELB')
digitar = pesquisa.find_element(By.TAG_NAME, 'input')
digitar.send_keys('smartphone', Keys.ENTER)

#lista de mais relevante na página 1
sleep(3)
lista1 = []
adicionarProduto(lista1)

sleep(3)
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 2"]')
#tive que fazer por meio do javascript, pois vários métodos não funcionaram para fazer o botão ser clicado
driver.execute_script("arguments[0].click();", botao)

#lista de mais relevante na página 2
sleep(3)
lista2= []
adicionarProduto(lista2)

sleep(3)
#sem declarar de novo a página não funciona
prox_pagina = driver.find_element(By.CLASS_NAME, 'Paginator_fullPage__YLBmh')
botao = prox_pagina.find_element(By.XPATH, '//a[@aria-label="Página 3"]')
driver.execute_script("arguments[0].click();", botao)

#lista de mais relevante na página 3
sleep(3)
lista3= []
adicionarProduto(lista3)

#voltando para a página 1
sleep(3)
pagina1 = driver.find_element(By.CLASS_NAME, 'Paginator_page__LYvDd')
botao_volta = pagina1.find_element(By.XPATH, '//a[@aria-label="Página 1"]')
driver.execute_script("arguments[0].click()", botao_volta)

#mudando para menor preço
sleep(3)
selecao = driver.find_element(By.CLASS_NAME, 'Select_Select__1HNob')
menor_preco = selecao.find_element(By.XPATH, '//option[@value="price_asc"]')
menor_preco.click()
sleep(10)

driver.close()