from locators import locators as lc


class loginPage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_in     = lc.SIGN_IN
        self.user_name_textbox = lc.USER_NAME_TBOX
        self.password_textbox  = lc.PASSWORD_TBOX
        self.login_button      = lc.LOGIN_BUTTON
        self.go_to_tool        = lc.TOOL_HOME


    def go_to_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in).click()


    def set_username (self, username):
        self.driver.find_element_by_xpath(self.user_name_textbox).clear()
        self.driver.find_element_by_xpath(self.user_name_textbox).send_keys(username)


    def set_password (self, password):
        self.driver.find_element_by_xpath(self.password_textbox).clear()
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)


    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def open_tool(self):
        self.driver.find_element_by_xpath(self.go_to_tool).click()

