from selenium import webdriver
from Question3 import TestCases
from configparser import ConfigParser

#loading the Account data
TestAccount = ConfigParser()
TestAccount.read('Config.ini')
user = TestAccount.get(str('Your Testing Gmail Account'),str('Account'))
pwd = TestAccount.get(str('YOur Testing Gmail Password'),str('Password'))
receiver = TestAccount.get(str('Email Receiver'),str('Receiver'))
title = TestAccount.get(str('Email Title'), str('Title'))
content = TestAccount.get(str('Email Content'),str('Content'))




class GMail():


    def Test_Scripts(self):

        URL = 'https://mail.google.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(URL)


        #Step2-Step10
        HW = TestCases(driver)
        HW.Step2(user)
        HW.Step3(pwd)
        HW.Step4()
        HW.Step5(receiver,title,content)
        HW.Step6()
        HW.Step7()
        HW.Step8()
        HW.Step9()
        HW.Step10()

        driver.quit()

LoginAccount = GMail().Test_Scripts()
