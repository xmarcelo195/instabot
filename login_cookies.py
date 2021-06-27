#script para criar os cookies e não precisar ficar sempre fazendo login manual

from selenium import webdriver
import pickle
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/?hl=pt-br&next=%2Ftudogostosooficial%2F")
sleep(5)
# find buttons
user = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

user.send_keys("")
password.send_keys("")
sleep(1)

enter = driver.find_element_by_xpath('//button/div[text()="Entrar"]')
enter.click()
sleep(1)

driver.get("https://www.instagram.com/accounts/login/?hl=pt-br&next=%2Ftudogostosooficial%2F")
pickle.dump(driver.get_cookies(), open(r"D:\Linux\pycharm\data\instabot\insta_sobremesas\Cookies.pkl", "wb"))
