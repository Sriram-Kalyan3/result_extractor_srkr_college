import imp
from number_generator import number_generate
from selenium_tut import *

numbers_generted_or_not = number_generate()

if numbers_generted_or_not is not None:
    initialize_result_extract()