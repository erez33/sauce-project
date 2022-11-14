import unittest
from selenium import webdriver

from pages import inventory
from pages import login


class InventoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/Users/JRamirez 1/Downloads/chromedriver')
        self.driver.get('https://www.saucedemo.com')

        log = login.LoginPage(self.driver)
        log.login('standard_user', 'secret_sauce')

    def tearDown(self) -> None:
        self.driver.close()

    def testProductLabelTitle(self) -> None:
        """Test procedure:
        1. Initialize inventory page
        2. Get title of page
        Assert:
        Title of the page is 'Products'

        """
        inventory_page_test = inventory.InventoryTestPage(self.driver)
        title = inventory_page_test.get_product_label_name()
        self.assertEqual('PRODUCTS', title)