import unittest
from selenium import webdriver
from Appier.Question3 import TestCases
from Appier.Question3 import Gmail_Task





class Test_Case(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        URL = 'https://mail.google.com'
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(URL)


    def Test_Step2(self):
        driver = Gmail_Task(self.driver)
        Result = TestCases.Step2(user= 'orwellclosed@gmail.com')

        if Result == 'OK':
            pass
        else:
            self.driver.quit()
            assert 'Fail_Reason' == Result






    def tearDown(self):
        self.driver.quit()






if __name__ == '__main__':
    unittest.main()
