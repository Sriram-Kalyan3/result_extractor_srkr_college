import datetime
from number_generator import number_generate
from selenium_tut import *
import time

start = time.time()
numbers_generted_or_not = number_generate()

if numbers_generted_or_not is not None:
    result_url = input('Enter the url of the result : ').strip()
    # result_url = 'http://www.srkrexams.in/Result.aspx?Id=2402'
    initialize_result_extract(result_url)

end = time.time()
print('Completed job in ', str(
    datetime.timedelta(seconds=end-start)), '[H:M:S]')
