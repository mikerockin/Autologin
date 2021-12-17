from selenium import webdriver

fb = webdriver.Chrome()
fb.get('https://www.facebook.com/login')
username = fb.find_element_by_xpath('//*[@id="email"]')
username.send_keys('mrmikhail88@gmail.com')
password = fb.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('yXZbRu2aFe')
login = fb.find_element_by_xpath('//*[@id="loginbutton"]')
login.click()