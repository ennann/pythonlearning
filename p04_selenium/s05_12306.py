import linecache
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://kyfw.12306.cn/otn/resources/login.html"

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

# Open 12306.
web = Chrome(options=option)
web.get(url)

# Read the username and password from local file.
usr = linecache.getline('/Users/Elton/Code-stuff/userinfo.txt', 13).strip()
pwd = linecache.getline('/Users/Elton/Code-stuff/userinfo.txt', 14).strip()

# Input the username and password and click login.
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys(usr)
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys(pwd)
web.find_element(By.XPATH, '//*[@id="J-login"]').click()

time.sleep(1)

# process the block
bottom = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(bottom, 300, 0).perform()
