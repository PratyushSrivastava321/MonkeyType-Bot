from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


driver=webdriver.Chrome("E:/chromedriver")
driver.maximize_window()
driver.get('https://www.monkeytype.com')
driver.find_element('xpath','//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()
driver.find_element('id','words')
outer_div=driver.find_element('xpath','//*[@id="words"]')
str1=outer_div.get_attribute('innerHTML')
words=[]
word=""
len1=len(str1)

for i in range(len1-10):
    if(str1[i]=='<' and str1[i+1]=='d'):
        words.append(word)
        word=""
    if(str1[i]=='r' and str1[i+1]=='>' and str1[i+3]=='<' and str1[i+4]=='/'):
        word+=str1[i+2]
for i in words:
    time.sleep(0.25)
    pyautogui.write(i+" ")
