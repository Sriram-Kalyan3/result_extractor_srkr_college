import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from scrapper import Scrapper
import time


def get_student_result(driver, regd_no, result_url):
    driver.get(result_url)
    time.sleep(1.2)

    # Input field for ROLL NUMBER
    regd_number_webElement = driver.find_element(
        By.NAME, 'ctl00$ContentPlaceHolder1$txtRegNo')
    # GET RESULT button
    getresult_button = driver.find_element(
        By.XPATH, '//*[@id="ContentPlaceHolder1_btnGetResult"]')

    # regd_number_webElement.sendKeys(Keys.chord(Keys.CONTROL, "a"), regd_no)
    regd_number_webElement.send_keys(regd_no)
    getresult_button.click()
    print('='*100)
    sc = Scrapper(driver.page_source)

    subject_list = ['Registerd No']+sc.get_subject(1)+sc.get_subject(2)+sc.get_subject(3) + \
        sc.get_subject(4)+sc.get_subject(5)+sc.get_subject(6) + sc.get_subject(7) + \
        sc.get_subject(8)+sc.get_subject(9) + \
        sc.get_subject(10)+['SGPA', 'CGPA']

    marks_list = sc.student_reg_num() + sc.get_subject_marks(1) + sc.get_subject_marks(2) + \
        sc.get_subject_marks(3) + sc.get_subject_marks(4) + sc.get_subject_marks(5) + \
        sc.get_subject_marks(6) + sc.get_subject_marks(7) + sc.get_subject_marks(8) + sc.get_subject_marks(9) + \
        sc.get_subject_marks(10) + sc.get_sgpa() + sc.get_cgpa()

    single_person_result_dict = {}
    for (subject, marks) in zip(subject_list, marks_list):
        single_person_result_dict[subject] = marks

    return (subject_list, marks_list, single_person_result_dict)


def merge_subjects(merge_into_list, merge_from_list):
    for from_item in merge_from_list:
        if from_item not in merge_into_list:
            merge_into_list.insert(-2, from_item)


def initialize_result_extract(result_url):

    output_csv_filename = input('Enter the output csv filename : ') + '.csv'

    chrome_driver = r'./driver/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    # options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_driver, options=options)

    with open('students_list.txt', 'r') as input_file:
        # output_csv_filename = 'output.csv'
        subjects = ['Registerd No', 'SGPA', 'CGPA']
        all_students_results_dict_list = []

        for regd_num in input_file.readlines():
            temp_subjects, marks_list, single_person_result_dict = get_student_result(
                driver, regd_num.rstrip(), result_url)
            merge_subjects(subjects, temp_subjects)
            all_students_results_dict_list.append(single_person_result_dict)
            print(single_person_result_dict)
        subjects[1:-2] = sorted(subjects[1:-2])
        with open(output_csv_filename, 'w', newline='', encoding='utf-8') as output_file:
            csv_writer = csv.DictWriter(output_file, fieldnames=subjects)
            csv_writer.writeheader()
            csv_writer.writerows(all_students_results_dict_list)
