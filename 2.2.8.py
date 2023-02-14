from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    FName = browser.find_element(By.NAME, 'firstname').send_keys('ivan')
    LName = browser.find_element(By.NAME, 'lastname').send_keys('bivan')
    Email = browser.find_element(By.NAME, 'email').send_keys('bivan@mai.ru')

    #current_dir = os.path.abspath(os.path.dirname(''))
    directory = "C:/Users/vakaraeva/Desktop/LEARNING/"
    file_name = "2.2.8.txt"
    file_path = os.path.join(directory, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()







    ######################
    Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:

1. вбить руками

element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

 

2. задать с помощью переменных

# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)
3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)
"""
итоговый код:

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)