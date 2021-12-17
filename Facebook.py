from selenium import webdriver

fb = webdriver.Chrome()
fb.get('https://www.facebook.com/login')
username = fb.find_element_by_xpath('//*[@id="email"]')
username.send_keys('') #Ввести логин в ''
password = fb.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('') #Ввести пароль в ''
login = fb.find_element_by_xpath('//*[@id="loginbutton"]')
login.click()
