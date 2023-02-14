from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button").click()

    browser.switch_to.window(browser.window_handles[1])

    val = browser.find_element(By.ID,'input_value')

    x = val.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer').send_keys(y)

    submit = browser.find_element(By.TAG_NAME, "button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()