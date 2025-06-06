from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

firstName = driver.find_element(By.NAME, "fName")
firstName.send_keys("Louan")

lastName = driver.find_element(By.NAME, "lName")
lastName.send_keys("Da BS")

email = driver.find_element(By.NAME, "email")
email.send_keys("dabs2020@gmail.com")

signUp = driver.find_element(By.CSS_SELECTOR, "form button")
signUp.click()