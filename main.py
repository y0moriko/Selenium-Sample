from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Get the site
driver.get("https://asoftmurmur.com/")
driver.fullscreen_window()
time.sleep(10)

# Signing in
loginBtn = driver.find_element(By.XPATH, '//*[@id="App"]/header/div/nav/button[2]')
loginBtn.click()
time.sleep(3)

txtEmail = driver.find_element(By.ID, 'upgradeEmail')
txtEmail.send_keys("minettejoylorzano@gmail.com")

continueBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[8]/div[2]/div/div/button[2]')
continueBtn.click()
time.sleep(10)

closeBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[8]/div[2]/div/div/button[2]')
closeBtn.click()
time.sleep(5)

# Check Button Functionalities
muteBtn = driver.find_element(By.XPATH, '//*[@id="App"]/header/div/div/button')
muteBtn.click()
time.sleep(5)

unmuteBtn = driver.find_element(By.XPATH, '//*[@id="App"]/header/div/div/button')
unmuteBtn.click()
time.sleep(5)

# Creating Random Mix
mixedBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[1]/button[2]')
mixedBtn.click()
time.sleep(3)
for i in range(3):
    randomGenerateBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div[3]/button[2]')
    randomGenerateBtn.click()
    time.sleep(3)

    saveBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div[1]/button')
    saveBtn.click()
    time.sleep(3)

closeMixBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div[3]/button[1]')
closeMixBtn.click()
time.sleep(3)

stopBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[3]/button[2]')
stopBtn.click()
time.sleep(3)

resetBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[3]/button[3]')
resetBtn.click()
time.sleep(3)

restoreBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[3]/button[3]')
restoreBtn.click()
time.sleep(3)

timerBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[1]/button[1]')
timerBtn.click()
time.sleep(3)

startBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div/div[4]/button[2]')
startBtn.click()
time.sleep(5)

stopTimerBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div/div[2]/button[2]')
stopTimerBtn.click()
time.sleep(2)

startTimerBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div/div[1]/button[2]')
startTimerBtn.click()
time.sleep(2)

fadeBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div/div[1]/button[3]')
fadeBtn.click()
time.sleep(2)

startFade = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div/div[4]/button[2]')
startFade.click()
time.sleep(3)

stopFade = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div/div[2]/button[2]')
stopFade.click()
time.sleep(3)

shareBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[1]/button[3]')
shareBtn.click()
time.sleep(2)

copyBtn = driver.find_element(By.XPATH, '//*[@id="App"]/div[4]/div[2]/div/div/div[1]/div[2]/div[3]/button')
copyBtn.click()
time.sleep(5)

stopBtn.click()
time.sleep(2)

# Check Navigation Buttons
blogBtn = driver.find_element(By.XPATH, '//*[@id="App"]/header/div/nav/a[1]')
blogBtn.click()
driver.fullscreen_window()
time.sleep(3)

aboutBtn = driver.find_element(By.XPATH, '/html/body/header/nav/span/a[2]')
aboutBtn.click()
driver.fullscreen_window()
time.sleep(3)

driver.quit()
