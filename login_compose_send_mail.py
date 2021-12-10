from selenium import webdriver
import pytest
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get('https://mail.google.com/')
driver.maximize_window()

# for sicurity reason - Turn off less secure, two step Verification also should be off. 

#enter email
enter_email_loactor=By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
email=driver.find_element(*enter_email_loactor)
email.send_keys("jignesh10102019@gmail.com")
time.sleep(3)

#click on next button
next_loactor=By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"
next=driver.find_element(*next_loactor).click()
time.sleep(3)

#enter password
password_loactor=By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
password=driver.find_element(*password_loactor)
password.send_keys("Shrey@1010")
time.sleep(3)

#next button
next1_loactor=By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"
next1=driver.find_element(*next1_loactor).click()
time.sleep(3)

#enter compose 
compose_loactor=By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div"
compose=driver.find_element(*compose_loactor).click()
time.sleep(3)

# enter to address
to_locator=By.XPATH,"/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input"
to=driver.find_element(*to_locator)
to.send_keys("jigneshpatel.ec.er@gmail.com")
time.sleep(3)

#enter subject
subject_locator=By.XPATH,"/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div[3]/input"
subject=driver.find_element(*subject_locator).send_keys("Test mail ")
time.sleep(3)

#enter body massage
body_locator=By.XPATH,"/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div"
body=driver.find_element(*body_locator).send_keys("Hi this is test mail for selenium webdriver.")
time.sleep(3)

#finally click on send button
send_loactor=By.XPATH,"/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]"
send=driver.find_element(*send_loactor).click()
time.sleep(3)






