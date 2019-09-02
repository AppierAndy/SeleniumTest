
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from configparser import ConfigParser


#loading the Account data
TestAccount = ConfigParser()
TestAccount.read('Config.ini')
title = TestAccount.get(str('Email Title'), str('Title'))
content = TestAccount.get(str('Email Content'),str('Content'))



class Gmail_Task(object):

    def __init__(self,driver):
        self.driver = driver

    #XPath Locators
    _EmailAccount = "//*[@id='identifierId']"
    _AccountContinue = "//*[@id='identifierNext']/span/span"
    _GmailLogo = "//a[@title='Gmail']//img[contains(@class,'gb_pa')]"
    _EmailPassword = "//*[@id='password']/div[1]/div/div[1]/input"
    _PWDContinue = "//*[@id='passwordNext']/span/span"
    _Compose = "/html/body[@class='aAU']/div[7]/div[@class='nH']/div[@class='nH']//div[@class='aj9 pp']/div[@class='oo']//div[@class='aic']//div[@role='button']"
    _MailTitle = "//*//form[@accept-charset='utf-8']//input[@placeholder='Subject']"
    _MailContent= "//div[@style='display: block;']//div[contains(@role,'textbox')]"
    _InboxMailTitle = "//span[@class='bog']//span[contains(text(),'Hello')]"
    _InboxMailContent = "//span[contains(text(),'Word')]"
    _MovetoReceiveMail = "//div[@class='xT']"
    _DeleteIcon = "//td[@class='bq4 xY']//li[contains(@data-tooltip,'Delete')]"
    _MoreIcon = "//span[@class='CJ']"
    _TrashIcon = "//div[@class='aio UKr6le']//a[contains(@href, 'trash')]"
    _TrashMailTitle = "//span[@class='bqe']"
    _TrashMailContent = "//span[@class='y2']"
    _TrashMailReceiver = "//span[@class='zF']"


    #CSS Locators
    _To = "[name='to']"
    _SentButton = ".dC [role='button']:nth-of-type(1)"



    #Position and Action-----------------------------------------------


    def getUserAccount(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self._EmailAccount)))


    def enterUserAccount(self,user):
        return self.getUserAccount().send_keys(user)




    def getContinue(self):
        return self.driver.find_element(By.XPATH,self._AccountContinue)

    def clickContinueLink(self):
        self.getContinue().click()


    def getGmailLogo(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._GmailLogo)))



    def getEmailPassword(self):
        return self.driver.find_element(By.XPATH, self._EmailPassword)

    def enterEmailPassword(self,pwd):
        time.sleep(1)
        return self.getEmailPassword().send_keys(pwd)




    def getPwdContinue(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._PWDContinue)))

    def clickPWDContinueLink(self):
        self.getPwdContinue().click()



    def getCompose(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self._Compose)))


    def clickCompose(self):
        self.getCompose().click()



    def getTo(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._To)

    def enterReceiver(self,receiver):
        return self.getTo().send_keys(receiver)



    def getMailTitle(self):
        return self.driver.find_element(By.XPATH, self._MailTitle)

    def enterMailTitle(self,title):
        return self.getMailTitle().send_keys(title)



    def getMailContent(self):
        return self.driver.find_element(By.XPATH, self._MailContent)

    def enterMailContent(self,content):
        return self.getMailContent().send_keys(content)



    def getSentButton(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._SentButton)

    def clickSentButton(self):
        self.getSentButton().click()



    def ChecktheEmail(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self._InboxMailTitle)))
        get_Subject = self.driver.find_element(By.XPATH, self._InboxMailTitle).get_attribute("innerHTML").split('</span>')[-1]
        get_Content = self.driver.find_element(By.XPATH, self._InboxMailContent).get_attribute("innerHTML").split('</span>')[-1]
        return get_Subject, get_Content




    def MovetoHoverBar(self):
        return ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH,self._MovetoReceiveMail)).perform()


    def getDeleteIcon(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self._DeleteIcon)))


    def clickDeleteIcon(self):
        self.MovetoHoverBar()
        self.getDeleteIcon().click()
        time.sleep(1)




    def getMoreIcon(self):
        return self.driver.find_element(By.XPATH, self._MoreIcon)


    def clickMoreIcon(self):
        time.sleep(1)
        self.getMoreIcon().click()



    def getTrashIcon(self):
        return self.driver.find_element(By.XPATH,self._TrashIcon)

    def clickTrashIcon(self):
        self.getTrashIcon().click()



    def checkTheTrashEmail(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self._TrashMailTitle)))
        #get_TrashMail_Receiver = self.driver.find_element(By.XPATH, self._TrashMailReceiver).get_attribute("innerHTML").split('</span>')[-1]
        get_TrashMail_Subject = self.driver.find_element(By.XPATH, self._TrashMailTitle).get_attribute("innerHTML").split('</span>')[-1]
        get_TrashMail_Content = self.driver.find_element(By.XPATH, self._TrashMailContent).get_attribute("innerHTML").split('</span>')[-1]
        check_TrashMail = get_TrashMail_Subject, get_TrashMail_Content
        return check_TrashMail




    #Step Scripts----------------------------------------------------------
class TestCases(Gmail_Task):
    #Step2:  Input your account & click Continue.
    def Step2(self,user):
        try:
            self.enterUserAccount(user)
            self.clickContinueLink()

            print("Step2: The account has been successfully entered.")
            return 'OK'
        except:
            self.driver.quit()
            print("Step2: Account entered fail")
            return 'Fail'

    #Step3: Input your password & click Continue.
    def Step3(self,pwd):
        try:
            self.enterEmailPassword(pwd)
            self.clickPWDContinueLink()
            self.getGmailLogo()
            print("Step3:Login Success")
            return 'OK'
        except:
            self.driver.quit()
            print("Step3: Login Fail")
            return 'Fail'



    #Step4:  Click Compose
    def Step4(self):
        try:
            self.clickCompose()
            print("Step4: Compose success")
            return 'OK'
        except:
            self.driver.quit()
            print("Step4: Compose fail")
            return 'Fail'



    #Step5:  Input “your email” in To, input “Hello” in Subject, input “Word” in Mail Body & click Send.
    def Step5(self, receiver,title,content):
        try:
            self.enterReceiver(receiver)
            self.enterMailTitle(title)
            self.enterMailContent(content)
            self.clickSentButton()
            print("Step5: The email has been sent.")
            return 'OK'
        except:
            self.driver.quit()
            print("Step5: The email was not sent.")
            return 'Fail'



    #Step6: Ensure your email exist in Inbox.
    def Step6(self):
        try:
            if self.ChecktheEmail() == (title,content):
                print('Step6: The sent email exist in Inbox')
            return 'OK'
        except:
            self.driver.quit()
            print('Step6: The sent email does not exist in Inbox')
            return 'Fail'


    #Step7: Click delete to move your email in trash.
    def Step7(self):
        try:
            self.clickDeleteIcon()
            print('Step7: The email has been deleted.')
            return 'OK'
        except:
            self.driver.quit()
            print('Step7: Delete the email failed.')
            return 'Fail'

    #Step8: Click More
    def Step8(self):
        try:
            self.clickMoreIcon()
            print('Step8: Click More success')
            return 'OK'
        except:
            self.driver.quit()
            print('Step8: Click More fail')
            return 'Fail'


    #Step9: Click Trash
    def Step9(self):
        try:
            self.clickTrashIcon()
            print('Step9: The email has been move to trash')
            return 'OK'
        except:
            self.driver.quit()
            print('Step9: The email does not move to trash')
            return 'Fail'


    #Step10: Check your email exist in trash.
    def Step10(self):
        try:
            if self.checkTheTrashEmail() == (title, content):
                print('Step10: The mail has been moved to the trash.')
            else:
                raise AssertionError
            return 'OK'
        except AssertionError:
            self.driver.quit()
            print('Step10: Cannot find the email in the trash.')
            return 'Fail'





