from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element(By.ID, "treasure")
    sunduk_value = sunduk.get_attribute('valuex')


    #x = sunduk_value.text
    y = calc(sunduk_value)

    ans = browser.find_element(By.ID, "answer").send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox").click()

    radbut = browser.find_element(By.ID, "robotsRule").click()

    subm = browser.find_element(By.CSS_SELECTOR, "button.btn")
    subm.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()