import unittest
from selenium import webdriver
from login_and_go_tool import loginPage
import time
import datetime
from handle_tool import toolpage
import Variables as VARS

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



TODAY = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")

class login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Firefox()
       cls.driver.maximize_window()
       print " ************   START TEST   *******************"

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(5)
        cls.driver.close()

        print " ************   END TEST   *******************"



    def test_login(self):
       driver = self.driver

       self.driver.get("https://staging.annotation.tools.unbabel.com")
       self.assertIn("Annotation Tool", self.driver.title)

       login = loginPage(driver)
       login.go_to_sign_in()
       login.set_username("emanuel+annotator3")
       login.set_password("nuno_anacleto@unbabel")
       login.click_login()
       login.open_tool()

       time.sleep(5)  #  !!!!!!!!  hardcoded, not good !!!!!!!!!!!!


       tool = toolpage(driver)
       tool.select_en_text()
       tool.set_error_type(VARS.ERROR_ADITION)
       tool.click_error_tree("Addition")

       #tool.set_error_sev("minorSeverity")
       tool.set_error_sev(VARS.SEVERITY_MINOR)
       tool.click_add_button()
       tool.select_any_side_bar(VARS.SIDEBAR_FINISH_REPORT)
       tool.insert_comments("This comment was added at {0}, by Nuno Anacleto".format(TODAY))
       tool.finish_exercice()
       tool.finish_job(VARS.FINISH_JOB_NO)




if __name__ == "__main__":
    unittest.main()