import time
from selenium import webdriver

# Optional argument, if not specified will search path.
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://127.0.0.1:8000')

assert 'Django Girls blog' in driver.title
