from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


import random
import string
import os

try:
    password = os.environ.get('S_PASSWORD')
    driver = webdriver.Firefox()
    # driver.get("https://bstackdemo.com/")
    # driver.get("https://cws.auburn.edu/ceps/")
    driver.get("http://debug.auburn.edu:8080/ceps")
    wait = WebDriverWait(driver, 5)  # Wait for up to 5 seconds


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

    label_with_title = driver.find_element(By.XPATH, '//input[@title="planning the event myself"]/parent::label')

    # Click the radio button associated with the located label
    radio_button = label_with_title.find_element(By.XPATH, './/input')
    radio_button.click()
    saveButton.click()

    # Your Personal Info
    # Locate the input field by its id
    input_field = label_with_title.find_element(By.XPATH, '//*[@id="SubmitterMainPhone"]')
    # Clear the current value of the input field
    input_field.clear()
    # Send the desired value to the input field
    input_field.send_keys('(333) 333-3333')
    saveButton.click()

    label_with_title = driver.find_element(By.XPATH, '//input[@title="no" and @name="CoPlannerRadio" and @value="false"]')
    label_with_title.click()
    saveButton.click()


    # Name of Event
    input_field = label_with_title.find_element(By.XPATH, '//*[@id="EventName"]')
    # Generating a random 6 digit string that can contain numbers 0-9 and any upper or lowercase letter from a-z
    # there are 56,800,235,584 possible combinations here so it will probably be unique :)
    random_string = 'Selenium_test_' + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    input_field.send_keys(random_string)
    saveButton.click()

    # How many people
    input_field = label_with_title.find_element(By.XPATH, '//input[@id="NumOfAttendees"]')
    input_field.send_keys(random.randint(1, 100))
    saveButton.click()
    
    input_field = driver.find_element(By.XPATH, '//table[@class="table-condensed"]//td[@data-date="1700956800000"]')
    input_field.click()
    
    # input_field = label_with_title.find_element(By.XPATH, '//input[@id="NumAttendees11-26-2023"]')
    # input_field.send_keys(random.randint(1, 100))
    input_field = label_with_title.find_element(By.XPATH, '//input[@id="Start11-26-2023"]')
    input_field.clear()
    input_field.send_keys('8:26 AM')
    input_field = label_with_title.find_element(By.XPATH, '//input[@id="End11-26-2023"]')
    # increases time by 1 hour
    for i in range(0, 60):
        input_field.send_keys(Keys.UP)
    saveButton.click()
    
    input_field = driver.find_elements(By.XPATH, '//*input[@id="shortNoticeAck"]')
    input_field.click()
    print("test")
    input_field= driver.find_elements(By.XPATH, '//*button[@id="alertify-ok"]')
    input_field.click()
    print("hello")

    
    
    
except Exception as e:
    print(e)
    # driver.quit()
    
    
