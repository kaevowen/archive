from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(r'C:\webdriver\chromedriver.exe')
url = 'https://airvisual.com/'
driver.get(url)
print(dir(driver.find_element_by_class_name('ranking')))
driver.find_element_by_class_name('ranking')
driver.save_screenshot('1.png')
#html = BeautifulSoup(driver.find_element_by_class_name('city_right'), 'html.parser')
sleep(5)
driver.close()