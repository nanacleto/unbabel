import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class login(unittest.TestCase):

    @classmethod
    def setUp(self):
       self.driver = webdriver.Firefox()
       self.driver.maximize_window()

    def test_login(self):
       self.driver.get("https://staging.annotation.tools.unbabel.com")
       self.assertIn("Annotation Tool", self.driver.title)
       self.driver.find_element_by_xpath("//button[@class='btn-round btn-white-home']").click()

       self.driver.find_element_by_xpath("//input[@name='username']").send_keys("emanuel+annotator3")
       self.driver.find_element_by_xpath("//input[@name='password']").send_keys("nuno_anacleto@unbabel")

       self.driver.find_element_by_xpath("//button[@class='unbabel-btn-round unbabel-blue btn-block']").click()

   # def test_select_batch(self):
       self.driver.find_element_by_xpath("//a[contains(text(),'ES to EN')]").click()

       try:
           element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "c-Sidebar__tab")))
       except NoSuchElementException as exception:
           print "More than 10 seconds"








if __name__ == "__main__":
    unittest.main()