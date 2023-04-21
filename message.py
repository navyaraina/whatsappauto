# from tkinter import BROWSE
import pywhatkit as pwk
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
import time
import pandas
import openpyxl as excel
import urllib.parse

def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    secondCol = sheet['B']
    driver  = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')
    time.sleep(20)

    for cell in range(len(firstCol)):
        contact = str(firstCol[cell].value)
        message = str(secondCol[cell].value)
        print(contact)
        print(message)
        link = "https://web.whatsapp.com/send?phone="+contact+"&amp;text="+urllib.parse.quote_plus(message)+"&amp;source=&amp;data="
        #link = "https://wa.me/"+contact+"?text="+message  
        driver.get(link)
        time.sleep(4)
        print("Sending message to", contact)

        try:
            time.sleep(7)
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            for ch in message:
                if ch == "\n":
                    ActionChains(BROWSE).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    input_box.send_keys(ch)
            input_box.send_keys(Keys.ENTER)
            print("Message sent successfuly")
        except NoSuchElementException:
            print("Failed to send message")

    driver.quit()

targets = readContacts("dataset.xlsx")