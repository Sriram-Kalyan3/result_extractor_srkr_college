import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('http://www.srkrexams.in/Result.aspx?Id=2402')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
print(soup.title.text.strip())

print(soup)

'''
ContentPlaceHolder1_txtRegNo
'''
s = soup.find('input', id= 'ContentPlaceHolder1_txtRegNo')
print(s)