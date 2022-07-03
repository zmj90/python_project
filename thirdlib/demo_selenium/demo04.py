import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# Navigate to url
driver.get("https://www.baidu.com")
print(driver.title)

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(value="kw").send_keys("webdriver" + Keys.ENTER)

time.sleep(6)
driver.quit()
