import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Config headless browser
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)  # Config the headless to the chrome.

url = 'https://www.endata.com.cn/BoxOffice/BO/Year/index.html'

web.get(url)

# GET select elements;
sel_element = web.find_element(By.XPATH, '//*[@id="OptionDate"]')  # GET element

# Packed the element to become selectable.
sel = Select(sel_element)

# Let the browser switch option

for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(3)
    table = web.find_element(By.XPATH, '//*[@id="TableList"]/table')
    print(table.text)
    print("**********************************************************")

web.close()
