from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    val_x = browser.find_element(By.ID, 'input_value')

    x = val_x.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    answer_field = browser.find_element(By.ID, 'answer').send_keys(y)

    robotCheckbox = browser.find_element(By.ID, 'robotCheckbox').click()

    robotsRule = browser.find_element(By.ID, 'robotsRule').click()


    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()