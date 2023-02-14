from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    browser = webdriver.Chrome()

    browser.get('http://suninjuly.github.io/selects1.html')

    value1 = browser.find_element(By.ID,'num1')
    num1 = value1.text

    value2 = browser.find_element(By.ID,'num2')
    num2 = value2.text

    sum = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum) # ищем элемент с текстом "Python"

    subm = browser.find_element(By.CSS_SELECTOR, "button.btn")
    subm.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()