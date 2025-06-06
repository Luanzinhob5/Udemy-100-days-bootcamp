from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_name = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
event_date = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')

# event_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# event_date = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

# event_list = [t.text for t in event_name]
# event_date_list = [f"2025-{d.text}" for d in event_date]

events = {n: {"time": event_date[n].text,"name": event_name[n].text,} for n in range(len(event_date))}

# for n in range(len(event_date)):
#     eventos[n] = {
#         "time": event_date[n].text,
#         "name": event_name[n].text,
#     }

print(events)



