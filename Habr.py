from selenium import webdriver

hb =  webdriver.Chrome()
hb.get('https://account.habr.com/login/')
username = hb.find_element_by_xpath('//*[@id="email_field"]')
username.send_keys('mrmikhail88@gmail.com')
password = hb.find_element_by_xpath('//*[@id="password_field"]')
password.send_keys('yXZbRu2aFe')
login = hb.find_element_by_xpath('//*[@id="login_form"]/fieldset/div[4]/button')
login.click()
