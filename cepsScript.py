from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
password = os.environ.get('S_PASSWORD')
if password:
    print("Password retrieved!")
else:
    print("man")
    
driver = webdriver.Firefox()
# driver.get("https://bstackdemo.com/")
# driver.get("https://cws.auburn.edu/ceps/")
driver.get("http://debug.auburn.edu:8080/ceps")
print(password)
wait = WebDriverWait(driver, 5)  # Wait for up to 5 seconds
importPassword = password
print(importPassword)
# Wait until the element with the class "btn btn-default" is present
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn")))

element.click()

# Fill in login info
username_element = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_element = wait.until(EC.presence_of_element_located((By.ID, "password")))
username_element.send_keys("ldb0046")  # Replace 'YourDesiredTextHere' with the text you want to enter
password_element.send_keys(password)  # Replace 'YourDesiredTextHere' with the text you want to enter


element = wait.until(EC.presence_of_element_located((By.NAME, "submit")))
element.click()

# Find the link by its text and click on it
link_element = driver.find_element(By.XPATH, '//a[text()="Request an Event"]')
link_element.click()

# Enter form
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn")))
element.click()

labels_with_no = driver.find_elements(By.XPATH, '//label[contains(text(), "No")]')
# Click the radio button associated with the first label
first_radio_button = labels_with_no[0].find_element(By.XPATH, './/input')
first_radio_button.click()

# Click the radio button associated with the second label
second_radio_button = labels_with_no[1].find_element(By.XPATH, './/input')
second_radio_button.click()

saveButton = driver.find_element(By.XPATH, '//button[text()="Save and Continue"]')


# Find the button with the text "Save and Continue" and click on it
saveButton.click()

# Locate the label that contains the text "other dignitaries no" using its title attribute
label_with_no = driver.find_element(By.XPATH, '//input[@title="other dignitaries no"]/parent::label')
# Click the radio button associated with the located label
radio_button = label_with_no.find_element(By.XPATH, './/input')
radio_button.click()

saveButton.click()

# Locate the label associated with the radio button using its title attribute
label_with_title = driver.find_element(By.XPATH, '//input[@title="event sponsor organization"]/parent::label')

# Click the radio button associated with the located label
radio_button = label_with_title.find_element(By.XPATH, './/input')
radio_button.click()
saveButton.click()