import time

from selenium import webdriver
# from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

browsers = webdriver.Chrome()
# web = Chrome()

url = "https://servicedesk-mig.bytedance.net/admin/groupMng"

browsers.get(url)

# Waiting for scanning the QR code.
time.sleep(15)

# Table
table = browsers.find_element(By.XPATH,
                              '//*[@id="root"]/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/table/tbody')
print(table.text)

# for colum in table:
#     print(colum.text)


# Find the EDIT bottom.
edit = '//*[@id="root"]/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[5]/a'
edit.click()

notification_setting = '//*[@id="root"]/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[5]'
notification_setting.click()
print(edit.text, "click success...")

# city = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
# city.click()
