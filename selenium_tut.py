from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver = r'C:\Users\Sriram Kalyan\Documents\Python\csv_scrapper\driver\chromedriver.exe'

driver = webdriver.Chrome(chrome_driver)
driver.get('http://www.srkrexams.in/Result.aspx?Id=2402')
time.sleep(2)

regd_number = driver.find_element(By.NAME,'ctl00$ContentPlaceHolder1$txtRegNo')
getresult_button = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_btnGetResult"]')

regd_number.send_keys('21b91a04q2')
getresult_button.click()
print('#'*30)
