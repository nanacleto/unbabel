from selenium.webdriver.common.action_chains import ActionChains
from locators import locators as lc





class toolpage():

    def __init__(self, driver):
        self.driver = driver

       # self.paragraph = "//div[@class='c-TranslationViewer__line'][2]/div[contains(@class, 'target')]//div[@class='c-TextBlock__main']/p"
       # self.search_error_type  =   "//input[@id='searchErrorTypes']"
       # self.set_combo_tree = "//input[@id='searchErrorTypes']/..//span[text()='Addition']"

    def select_en_text(self):

        actions = ActionChains(self.driver)

        my_paragraph = self.driver.find_element_by_xpath(lc.PARAGRAPH)

        actions.move_to_element_with_offset(my_paragraph, 10, 10)
        actions.click_and_hold(on_element=None)
        actions.move_by_offset(10, 50)
        actions.release()
        actions.perform()

    def set_error_type(self, error_type):
        self.driver.find_element_by_xpath(lc.SET_ERROR_TYPE).send_keys(error_type)

    def click_error_tree(self, tree_error):
        self.set_combo_tree = "//input[@id='searchErrorTypes']/..//span[text()='{0}']".format(tree_error)
        self.driver.find_element_by_xpath(lc.SET_TREE_ERROR).click()

    def set_error_sev(self, error_sev):
        self.driver.find_element_by_xpath("// input[@id='{0}']".format(error_sev)).click()

    def click_add_button(self):
         self.driver.find_element_by_xpath("//button[@class='c-Button c-Button--cta']").click()


    def select_any_side_bar(self, side_bar):
        self.driver.find_element_by_xpath("//div[@class='c-Sidebar__item' and contains(.,'{0}')]".format(side_bar)).click()

    def insert_comments(self, text):
        self.driver.find_element_by_xpath("//textarea[@name='comment']").clear()
        self.driver.find_element_by_xpath("//textarea[@name='comment']").send_keys(text)

    def finish_exercice(self):
        self.driver.find_element_by_xpath("//button[@class='c-Button c-Button--cta' and contains(.,'Finish')]").click()

    def finish_job(self,bool):
         self.driver.find_element_by_xpath("// div[ @ id = 'js-modal-footer']//button[@class ='c-Button' and contains(., '{0}')]".format(bool)).click()