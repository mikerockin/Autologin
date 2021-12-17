from selenium import webdriver

dr = webdriver.Chrome()
dr.get('https://my.drom.ru/sign?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1639714709')
username = dr.find_element_by_xpath('//*[@id="sign"]')
username.send_keys('') #Ввести логин в ''
password = dr.find_element_by_xpath('//*[@id="password"]')
password.send_keys('') #Ввести пароль в ''
login = dr.find_element_by_xpath('//*[@id="signbutton"]')
login.click()
