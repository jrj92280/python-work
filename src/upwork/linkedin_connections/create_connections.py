import time
from selenium import webdriver

for count in range(1,3):
    driver = webdriver.Chrome()
    driver.get('http://www.google.com/xhtml');
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    driver.quit()
