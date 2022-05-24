"""







"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = "https://status.human-zoo.club/"
web = Chrome()
web.get(url)
# time.sleep(1)


host_status = web.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/div/div/small').text
print(host_status)


def get_host_status():
    pass


while True:
    if host_status == "运行中":
        continue
    else:
        import os

        os.system("open /Users/Elton/Downloads/alarm.mp3")
