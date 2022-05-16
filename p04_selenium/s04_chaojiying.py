import linecache

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from chaojiying import Chaojiying_Client

url = "https://www.chaojiying.com/user/login"

web = Chrome()
web.get(url)

# Read the username and password from local file.
usr = linecache.getline('/Users/Elton/Code-stuff/userinfo.txt', 7).strip()
pwd = linecache.getline('/Users/Elton/Code-stuff/userinfo.txt', 8).strip()

# get the image by bit info
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client(usr, pwd, '933123')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic["pic_str"]

usr_input = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(usr)
pwd_input = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(pwd)
vcd_input = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

# click login
web.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input").click()
