from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


print("Enter the URL of app:\n")
webpage = input()
### example -> webpage = 'https://play.google.com/store/apps/details?id=com.whatsapp&hl=en_IN&gl=US'
webpage = webpage + '&showAllReviews=true'

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(executable_path = 'E://chromedriver_win32_86//chromedriver', options = options)#, service_args = args)

driver.get(webpage)

reviews_path = '/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[2]/div/div[1]/div[1]/div[1]/span'
reviews = driver.find_element_by_xpath(reviews_path)
reviews.click()
sleep(3)

import pyautogui as pag 
pag.press('down');sleep(2);pag.press('enter');sleep(2)


'''one_star_path = '/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[2]/div/div[1]/div[1]/div[2]'
one_star = driver.find_element_by_xpath(one_star_path)
one_star.click()
'''

'''actions = ActionChains(driver)
actions.send_keys(Keys.DOWN).perform()
sleep(1)
actions.send_keys(Keys.ENTER).perform()
'''


driver.execute_script("window.scrollTo(0,7100);")
sleep(2)
driver.execute_script("window.scrollTo(0,14200);")
sleep(2)
driver.execute_script("window.scrollTo(0,21100);")
sleep(2)

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')

reviews_one_star = soup.find_all("span", {'jsname' : 'bN97Pc'})
#print(reviews_one_star)
reviews_one_star = [r.text for r in reviews_one_star]
import pandas as pd 

df = pd.DataFrame(columns = ['Rating', 'Review'])
df['Review'] = reviews_one_star
df['Rating'] = 1
print(df.head())
df.to_csv('one_star_reviews.csv', index = False)

'''
cnt = 0
for r in reviews_one_star:
	try:
		print(r.text)
	except:
		pass
	print('-'*100)
	cnt +=1
	if cnt == 500:
		break
'''

#print(soup.prettify())



driver.execute_script("window.scrollTo(0,0);")
sleep(5)
one_star_path = '/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[2]/div/div[1]/div[1]/div[2]/span'
one_star = driver.find_element_by_xpath(one_star_path)
one_star.click()
sleep(2)


'''
for _ in range(5):
	sleep(1)
	actions.send_keys(Keys.DOWN).perform()
	#actions.send_keys(Keys.ENTER).perform()
actions.send_keys(Keys.ENTER).perform()
'''
import pyautogui as pag 
pag.press('down');sleep(2);pag.press('down');sleep(2);pag.press('down');sleep(2);pag.press('down');sleep(2);pag.press('enter');sleep(2)

sleep(3)



driver.execute_script("window.scrollTo(0,7100);")
sleep(2)
driver.execute_script("window.scrollTo(0,14200);")
sleep(2)
driver.execute_script("window.scrollTo(0,21100);")
sleep(2)

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')

reviews_one_star = soup.find_all("span", {'jsname' : 'bN97Pc'})
#print(reviews_one_star)
reviews_one_star = [r.text for r in reviews_one_star]
import pandas as pd 

df = pd.DataFrame(columns = ['Rating', 'Review'])
df['Review'] = reviews_one_star
df['Rating'] = 5
print(df.head())
df.to_csv('five_star_reviews.csv', index = False)

driver.close()
