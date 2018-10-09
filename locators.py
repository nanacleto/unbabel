class locators():


    #### TO LOGIN    ************
    SIGN_IN           = "//button[@class='btn-round btn-white-home']"
    USER_NAME_TBOX = "//input[@name='username']"
    PASSWORD_TBOX  = "//input[@name='password']"
    LOGIN_BUTTON      = "//button[@class='unbabel-btn-round unbabel-blue btn-block']"
    TOOL_HOME        = "//a[contains(text(),'ES to EN')]"

    #### TO TOOL     ************

    PARAGRAPH = "//div[@class='c-TranslationViewer__line'][2]/div[contains(@class, 'target')]//div[@class='c-TextBlock__main']/p"
    SET_ERROR_TYPE  =   "//input[@id='searchErrorTypes']"
    SET_TREE_ERROR = "//input[@id='searchErrorTypes']/..//span[text()='Addition']"


