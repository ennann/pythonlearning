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

# ad = web.find_element(By.XPATH, '//*[@id="loginNavSlider"]/div/div/a[6]/div/span')
# ad.click()
# time.sleep(3)

web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("架构", Keys.ENTER)
time.sleep(3)

job_list = web.find_elements(By.XPATH, '//*[@id="s_position_list"]/ul/li')

for job in job_list:
    job_name = job.find_element(By.TAG_NAME, "h3").text
    job_location = job.find_element(By.XPATH, "./div/div/div/a/span/em").text
    job_money = job.find_element(By.XPATH, "./div/div/div[2]/div/span").text
    job_requre = job.find_element(By.XPATH, './div/div/div[2]/div').text
    job_company = job.find_element(By.XPATH, "./div/div[2]/div/a").text
    print(job_name, job_location, job_money, job_requre, job_company)

print(web.title)

"""
//*[@id="s_position_list"]/ul/li[1]
//*[@id="s_position_list"]/ul/li[1]/div[1]/div[2]/div[1]/a/text()
//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[2]/div
//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/span/em
//*[@id="s_position_list"]/ul/li[2]/div[1]/div[1]/div[2]/div/span
"""
