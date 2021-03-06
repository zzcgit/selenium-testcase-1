# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner

class SampLoginSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://159.226.97.194:8080"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_samp_login_search(self):
        driver = self.driver
        driver.get(self.base_url + "/sams/index.jsp")
        driver.find_element_by_link_text(u"您好，请登录").click()
        driver.find_element_by_id("login_admin").clear()
        driver.find_element_by_id("login_admin").send_keys("ibpcp")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("111")
        driver.find_element_by_id("login_Btn").click()
        driver.find_element_by_id("searchCondition").clear()
        driver.find_element_by_id("searchCondition").send_keys(u"蛋白纯化系统")
        driver.find_element_by_css_selector("button.search-btn.fl").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()
    testunit=unittest.TestSuite()
    testunit.addTest(SampLoginSearch("test_samp_login_search"))
    now=time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"test result",description=u"The result about testcase")
    runner.run(testunit)
    fp.close()
