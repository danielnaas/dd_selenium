from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import random
import time

# browse to form
driver = webdriver.Chrome()
driver.get("https://naas.createuky.net/eluna/dd/feedback.html")
time.sleep(2)

# answer first question
first_time = driver.find_element(By.ID, 'attending-yes')
time.sleep(2)
first_time.click()

# answer second question
quality_five = driver.find_element(By.ID, 'quality-5')
time.sleep(2)
quality_five.click()

# answer third question
just_right = driver.find_element(By.ID, 'volume-2')
time.sleep(2)
just_right.click()

# find fourth question
any_comments = driver.find_element(By.ID, 'free_text')
time.sleep(2)
any_comments.click()

# build the feedback message and post it
good_adjective = ['great', 'fun', 'worthwhile', 'educational', 'outstanding']
feedback_text = "The event was " + random.choice(good_adjective) + "!"
any_comments.send_keys(feedback_text)
time.sleep(5)

# submit the form
submit_form = driver.find_element(By.ID, 'submit_form')
submit_form.click()
time.sleep(10)

# close the browser
driver.quit()
print("STATUS: Job done!")
