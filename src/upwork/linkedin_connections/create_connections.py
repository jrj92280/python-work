import os

username = os.environ.get("USERNAME")
password = os.environ.get('PASSWORD')

if not username or not password:
    raise RuntimeError('USERNAME & PASSWORD are required environment variables.')

# from selenium import webdriver

# driver = webdriver.Chrome()
#
#
# driver.get('http://www.google.com/xhtml')
#
#
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# driver.quit()


"""
1. go to: www.linkedin.com
2. enter: user name, password, and sign in
3. click: My Network
4. click: Connect for "People you my know"
"""
