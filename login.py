import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class login(unittest.TestCase):



    def setUp(self):
       self.driver = webdriver.Firefox()

    def test_open_page(self):
       driver = self.driver
       driver.get("https://staging.annotation.tools.unbabel.com")
       self.assertIn("Annotation Tool", driver.title)
       driver.find_element_by_xpath("//button[@class='btn-round btn-white-home']").click()

       driver.find_element_by_xpath("//input[@name='username']").send_keys("emanuel+annotator3")
       driver.find_element_by_xpath("//input[@name='password']").send_keys("nuno_anacleto@unbabel")

       driver.find_element_by_xpath("//button[@class='unbabel-btn-round unbabel-blue btn-block']").click()

if __name__ == "__main__":
    unittest.main()