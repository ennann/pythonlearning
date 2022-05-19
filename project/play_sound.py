import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = "https://onlineservices.immigration.govt.nz/?WHS"
web = Chrome()
web.get(url)
time.sleep(2)
host_status = web.find_element(By.XPATH, '/html/body/section[1]/div/h1').text

while True:
    if host_status == "Host error":
        continue
    else:
        import os

        os.system("open /Users/Elton/Downloads/alarm.mp3")

    web.refresh()
    host_status = web.find_element(By.XPATH, '/html/body/section[1]/div/h1').text
