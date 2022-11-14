import unittest
from selenium import webdriver

from pages import login

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome("/Users/JRamirez 1/Downloads/chromedriver")
        self.driver.get('https://www.saucedemo.com/')

    def tearDown(self) -> None:
        self.driver.close()

    @unittest.skip("testSuccessfulLogin works")
    def testSuccessfulLogin(self) -> None:
        login_page = login.LoginPage(self.driver)
        login_page.login('standard_user', 'secret_sauce')

        expected_url, actual_url = 'https://www.saucedemo.com/inventory.html', self.driver.current_url
        self.assertEqual(expected_url, actual_url)

    @unittest.skip("testFailedLogin works")
    def testFailedLogin(self) -> None:
        login_page = login.LoginPage(self.driver)
        login_page.login('locked_out_user', 'secret_sauce')
        # login_page.login('standard_user', 'secret_sauce')
        expected_url, actual_url = 'https://www.saucedemo.com/', self.driver.current_url

        self.assertEqual(expected_url, actual_url)
        self.assertTrue(login_page.find_error_button())
        self.assertEqual('Epic sadface: Sorry, this user has been locked out.',
                         login_page.get_error_message())

    @unittest.skip("testUsernameExpectedBehavior works")
    def testUsernameExpectedBehavior(self) -> None:
        login_page = login.LoginPage(self.driver)
        login_page.login('', 'secret_sauce')
        self.assertEqual('Epic sadface: Username is required', login_page.get_error_message())

    @unittest.skip("testPasswordExpectedBehavior works")
    def testPasswordExpectedBehavior(self) -> None:
        login_page = login.LoginPage(self.driver)
        login_page.login('standard_user', '')
        self.assertEqual('Epic sadface: Password is required', login_page.get_error_message())

    @unittest.skip('testLockedOutUserBehavior works')
    def testLockedOutUserBehavior(self) -> None:
        login_page = login.LoginPage(self.driver)
        login_page.login('locked_out_user', 'secret_sauce')
        self.assertEqual('Epic sadface: Sorry, this user has been locked out.', login_page.get_error_message())

    @unittest.skip("testPageStatus works ")
    def testPageStatus(self) -> None:
        login_page = login.LoginPage(self.driver)
        self.assertEqual(200, login_page.get_status('https://www.saucedemo.com/'))

    # todo write a test for session management
    # todo add tests for png assets

    def testLoginBotGraphic(self)->None:
        login_page =login.LoginPage(self.driver)
        self.assertEqual(200, login_page.request_main_png_asset('https://www.saucedemo.com/static/media'
                                                                '/Login_Bot_graphic.20658452.png'))


if __name__ == '__main__':
    unittest.main()

'''
to run tests execute python3 -m unittest -v login_test.py
'''