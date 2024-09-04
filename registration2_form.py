from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")

    # Находим name и вводим его
    input_firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
    input_firstname.send_keys("Иван")

    # Находим lastname и вводим его
    input_firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input_firstname.send_keys("Иванов")


    # Находим email и вводим
    input_firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input_firstname.send_keys("a@a.com")

    # Находим phone и вводим его
    input_firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone']")
    input_firstname.send_keys("555")

    # Находим address и вводим
    input_firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your address']")
    input_firstname.send_keys("main st")

    # Нажимаем на кнопку отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла
