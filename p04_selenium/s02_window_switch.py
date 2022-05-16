import time

from selenium.webdriver import Chrome
# import By function, because python will
from selenium.webdriver.common.by import By
# import Keyboard.
from selenium.webdriver.common.keys import Keys

web = Chrome()

url = "https://www.lagou.com/"

web.get(url)

city = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
city.click()

time.sleep(1)

# Get all the data from the web
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("架构", Keys.ENTER)
time.sleep(3)

# Open new window one by one, and switch to the new window, get the info from the new window, close it,


# open the new window.
list = web.find_element(By.XPATH, '//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3')
list.click()

# when you open the new window, selenium still stay at the old one.
# How to enter the new window
web.switch_to.window(web.window_handles[-1])

jd = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text

print(f"Test print: {jd}")

# Close the window, and back to the main window.
web.close()
web.switch_to.window(web.window_handles[0])

# How to handle iframe using selenium.
# Located the iframe, and using web.switch_to.frame to switch.
#
# iframe = web.switch_to.frame("Xpath location")
# SWITCH to frame
# web.switch_to.frame(iframe)

# SWITCH to default
# web.switch_to.default_content()
