# Baixar imagem e descrição que contenham a palavra chave

from selenium import webdriver
from time import sleep
import urllib.request
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
# get final 'https://www.instagram.com/accounts/login/?next=%2F_receitasdoces_'
browser.get('https://www.instagram.com/accounts/login/?next=%2Flivro_de_receitas_/')


sleep(3)
# path_login = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input'
# path_senha = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input'
# path_submit = '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button'
login = browser.find_element_by_name('username')
senha = browser.find_element_by_name('password')

login.send_keys("login")
senha.send_keys("senha")

browser.find_element_by_xpath("//button[@type='submit']").click()

sleep(35)

numero_post = 2375
path_txt = '/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span'
path_img = '/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/img'

sleep(10)

palavras_chave = ['chocolate', 'leite condensado', 'brigadeiro', 'açucar']

i = 1
while i <= (int(numero_post)):
    try:
        texto = browser.find_element_by_xpath(path_txt).text
        img = browser.find_element_by_xpath(path_img).get_attribute("src")

        texto_lower = str(texto).lower()

        if any(x in texto_lower for x in palavras_chave):
            with open(r"D:\Linux\pycharm\data\instabot\exemplo\post{}.txt".format(i), "a+",
                      encoding='utf8') as f:
                f.write(texto)
            # adicionei a linha 50 para baixar direto, não testei depois disso
            urllib.request.urlretrieve(img, "D:\\Linux\\pycharm\\data\\instabot\\exemplo\\post{}.jpg".format(i))

            print('Salvou o {}'.format(i))
        else:
            print('não tem as palavras chaves em {}'.format(i))

    except:
        print('Não pegou o post', i)
    sleep(1)
    if i == 1:
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
    else:
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
    i = i + 1
    sleep(3)

