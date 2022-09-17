from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapper import Scrapper
import time

# Keys is used to overwrite the input value of the roll number field instead of appending
from selenium.webdriver.common.keys import Keys

chrome_driver = r'C:\Users\Sriram Kalyan\Documents\Python\csv_scrapper\driver\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(chrome_driver, options=options)


def get_student_result(regd_no, subject_list):
    driver.get('http://www.srkrexams.in/Result.aspx?Id=2402')
    time.sleep(2)

    #Input field for ROLL NUMBER
    regd_number_webElement = driver.find_element(By.NAME,'ctl00$ContentPlaceHolder1$txtRegNo')
    #GET RESULT button
    getresult_button = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_btnGetResult"]')

    # regd_number_webElement.sendKeys(Keys.chord(Keys.CONTROL, "a"), regd_no)
    regd_number_webElement.send_keys(regd_no)
    getresult_button.click()
    print('='*50)
    sc = Scrapper(driver.page_source)
    if not subject_list:
        subject_list = ['Registerd No']+[
                sc.get_subject(1),
                sc.get_subject(2),
                sc.get_subject(3),
                sc.get_subject(4),
                sc.get_subject(5),
                sc.get_subject(6),
                sc.get_subject(7),
                sc.get_subject(8),
                sc.get_subject(9),
                sc.get_subject(10)
            ]+['SGPA', 'CGPA']
    marks_list = [sc.get_subject_marks(1)]+ [sc.get_subject_marks(2)]+ [sc.get_subject_marks(3)] + \
                 [sc.get_subject_marks(4)]+ [sc.get_subject_marks(5)]+ [sc.get_subject_marks(6)]+ \
                 [sc.get_subject_marks(7)]+ [sc.get_subject_marks(8)]+ [sc.get_subject_marks(9)]+ [sc.get_subject_marks(10)]

    return subject_list, marks_list

sample_student_list = ['21b91a04q2','21b91a04q3','21b91a04q4']
subjects = []
for regd_num in sample_student_list:
    subjects, marks_list = get_student_result(regd_num, subjects)
    print(marks_list)

