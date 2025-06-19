from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

#Get the site
driver.get("https://sis2.pup.edu.ph/student/")
time.sleep(5)

txtStudno = driver.find_element(By.ID, "studno")
txtStudno.send_keys("2022-00121-UQ-0")
time.sleep(3)

txtSelectMonth = Select(driver.find_element(By.ID, "SelectMonth"))
txtSelectMonth.select_by_visible_text("August")

txtSelectDay = Select(driver.find_element(By.ID, "SelectDay"))
txtSelectDay.select_by_visible_text("9")

txtSelectYear = Select(driver.find_element(By.ID, "SelectYear"))
txtSelectYear.select_by_visible_text("2004")

txtPassword = driver.find_element(By.ID, "password")
txtPassword.send_keys("ZKEGQMDU")

button = driver.find_element(By.NAME, "Login")
button.click()

time.sleep(5)

driver.quit()