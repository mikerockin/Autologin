from selenium import webdriver

vk = webdriver.Chrome()
vk.get('https://vk.com/')
username = vk.find_element_by_xpath('//*[@id="index_email"]')
username.send_keys('')#Ввести логин в ''
password = vk.find_element_by_xpath('//*[@id="index_pass"]')
password.send_keys('') #Ввести пароль в ''
login = vk.find_element_by_xpath('//*[@id="index_login_button"]')
login.click()
