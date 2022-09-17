from bs4 import BeautifulSoup

class Scrapper():
    def __init__(self,pagesource):
        self.soup = BeautifulSoup(pagesource,features="html.parser")

    def student_reg_num(self):
        # Getting the title tag
        print(self.soup.title.text.strip())
        s = self.soup.find('input', id= 'ContentPlaceHolder1_txtRegNo')
        return s['value']

    def get_subject(self, subject_num='1'):
        s = self.soup.find('span', id= 'ContentPlaceHolder1_dgvStudentHistory_lblPName_{}'.format(subject_num))
        if s is None:
            return s
        return s.text

    def get_subject_marks(self,marks_num='1'):
        s = self.soup.find('span', id= 'ContentPlaceHolder1_dgvStudentHistory_lblGrade_{}'.format(marks_num))
        if s is None:
            return s
        return s.text
    
