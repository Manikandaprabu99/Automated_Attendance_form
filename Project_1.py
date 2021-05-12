import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.select import Select


def form():
    web = webdriver.Chrome()
    web.get('https://accounts.google.com/signin/v2/identifier?continue='+'https://docs.google.com/forms/d/e/1FAIpQLScJF2S_qShA-3lSc03aSfix__8mitR9Jk7hDZl0zS62T7Z73w/viewform')
    web.implicitly_wait(15)
    email = web.find_element_by_xpath('//*[@id="identifierId"]')
    mail = '18e218@kce.ac.in'
    email.send_keys(mail)
    nextButton = web.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    nextButton.click()
    password='XXXXXXXX'
    pswd=web.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pswd.send_keys(password)
    login=web.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    login.click()

    time.sleep(10)

    today = date.today()
    str_time = date.strftime(today, '%d%m20%y')
    dates=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    dates.send_keys(str_time)

    Name = "Manikandaprabu D"
    name = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(Name)

    time.sleep(5)

    drop = web.find_element_by_class_name("quantumWizMenuPaperselectOptionList").click()
    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[6]/span').click()

    time.sleep(5)

    Regno = "18E218"
    reg = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    reg.send_keys(Regno)

    time.sleep(2)

    web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()

    time.sleep(2)

if __name__ == '__main__':
    form()
