import os,sys
sys.path.append(os.getcwd())
import pytest

from Base.get_driver import get_driver
from Page.page_login import PageLogin


class TestLogin():
    def setup_class(self):
        self.login = PageLogin(get_driver())
    def teardown_class(self):
        self.login.driver.quit()

    def test_login(self,usename="12334556633",pwd="123123"):
        self.login.page_input_uername(usename)
        self.login.page_input_pwd(pwd)
        self.login.page_login_btn()
if __name__ == '__main__':
    pytest.main("-s test_login.py")