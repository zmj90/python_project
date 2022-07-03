from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://cdn2.byhy.net/files/selenium/sample3.html")
handles1 = driver.current_window_handle
print(id(handles1), type(handles1), handles1)

element = driver.find_element(By.TAG_NAME, "a")
print(id(element), type(element), element)
element.click()

r1 = driver.title
print(id(r1), type(r1), r1)

r3 = driver.window_handles
print(id(r3), type(r3), r3)

driver.switch_to.window(r3[-1])
handles2 = driver.current_window_handle
r2 = driver.title
print(r2)
e1 = driver.find_element(By.ID, "sb_form_q")
e1.send_keys("python")

driver.switch_to.window(handles1)
element.click()
driver.switch_to.window(driver.window_handles[-1])
e2 = driver.find_element(By.ID, "sb_form_q")
e2.send_keys("docker")

driver.switch_to.window(handles2)
e1.send_keys("jenkins")








