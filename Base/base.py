from selenium.webdriver.support.wait import WebDriverWait


class Base(object):

    def __init__(self,driver):
        self.driver = driver

    # 查找元素方法封装
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素方法封装
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 输入方法封装
    def base_input(self,loc,text):
        self.base_find_element(loc).clear().send_keys(text)

