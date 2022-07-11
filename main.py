import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
game_url = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(chrome_driver_path)
driver.get(game_url)

cookie = driver.find_element(By.ID, "cookie")


def check():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    active_elements = []
    for element in store:
        if element.get_attribute("class") == "":
            active_elements.append(element.get_attribute("id"))
    return active_elements


def buy(elem_list):
    elem = driver.find_element(By.ID, elem_list[-1])
    elem.click()


start = time.time()
check_time = start + 5
end_time = start + 60

while end_time > time.time():

    while time.time() < check_time:
        cookie.click()

    buy(check())
    check_time = time.time() + 5

cps = driver.find_element(By.ID, "cps")
print(cps.text)

driver.quit()
