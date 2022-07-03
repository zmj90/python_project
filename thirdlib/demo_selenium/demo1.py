from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://cdn2.byhy.net/files/selenium/sample2.html")
driver.switch_to.frame("frame1")
element = driver.find_element(By.CSS_SELECTOR, ".plant")
print(id(element), type(element), element)
r1 = element.get_attribute("outerHTML")
print(id(r1), type(r1), r1)
driver.switch_to.default_content()
driver.find_element(By.ID, "outerbutton").click()







