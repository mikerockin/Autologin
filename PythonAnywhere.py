from selenium import webdriver

pt = webdriver.Chrome()
pt.get('https://www.pythonanywhere.com/login/')
username = pt.find_element_by_xpath('//*[@id="id_auth-username"]')
username.send_keys('MikeRockIn')
password = pt.find_element_by_xpath('//*[@id="id_auth-password"]')
password.send_keys('yXZbRu2aFe')
login = pt.find_element_by_xpath('//*[@id="id_next"]')
login.click()