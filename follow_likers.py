import pickle
from selenium import webdriver
from time import sleep
import pyautogui as pg
import numpy as np
from random import random

driver = webdriver.Firefox()

driver.get("https://www.instagram.com/accounts/login/?hl=pt-br&next=%2Ftudogostosooficial%2F")

for cookie in pickle.load(open(r"D:\Linux\pycharm\data\instabot\insta_sobremesas\Cookies.pkl", "rb")):
    driver.add_cookie(cookie)

driver.get("https://www.instagram.com/accounts/login/?hl=pt-br&next=%2Ftudogostosooficial%2F")

#open first image
sleep(2)
image = driver.find_element_by_xpath('//a/div/div[1]/img')
image.find_element_by_xpath('../..').click()



#abrir o box de pessoas que deram like (tem que ser foto, video dá erro)
sleep(3)
box_likers = driver.find_element_by_xpath("//*[contains(text(), 'Curtido por')]")
likers_btn = box_likers.find_elements_by_tag_name('a')
likers_btn[-1].click()

sleep(2)
i = 0
erro = 0
while i <= 300:
    like_location = pg.locateOnScreen(r"C:\Users\marcelo\Pictures\seguir.png")
    sleep(np.random.randint(10, 200)/100)
    if like_location is None:
        erro += 1
        for i in range(np.random.randint(4, 7)):
            pg.press('down')
        if erro > 5:
            print('deu muito erro')
            break
    else:
        # 68 x 37 <- tamanho do botao like
        click_position = pg.center(like_location)
        x = click_position.x + np.random.randint(0, 21)
        y = click_position.y + np.random.randint(0, 12)
        pg.click(x, y)
        i += 1
        erro = 0
