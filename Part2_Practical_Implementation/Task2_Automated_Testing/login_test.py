from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up ChromeDriver service
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    # ✅ Valid Login Test
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    if "Logged In Successfully" in driver.page_source:
        print("✅ Valid Login Test Passed")
    else:
        print("❌ Valid Login Test Failed")

    # ✅ Invalid Login Test
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    if "Your username is invalid!" in driver.page_source:
        print("✅ Invalid Login Test Passed")
    else:
        print("❌ Invalid Login Test Failed")

finally:
    driver.quit()
