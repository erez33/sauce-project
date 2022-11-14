from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class InventoryTestPage(BasePage):

    # product_label = (By.XPATH, '//*[@id="inventory_filter_container"]/div')

    def get_product_label_name(self):
        """Objective: return the title of page
        """
        text = self.driver.find_element_by_xpath('//*[@id="header_container"]/div[2]/span')
        return text.text

    def open_menu_bar(self):
        """Objective: Finds the menu icon
        and clicks the menu icon, thus opening the menu
        """
        menu_icon = self.driver.find_element_by_xpath('//*[@id="menu_button_container"]/div/div[3]/div/button')
        menu_icon.click()

    def click_logout(self):
        """Objective: Finds the logout icon
        and clicks the icon, logging out the user
        """
        logout_icon = self.driver.find_element_by_xpath('//*[@id="logout_sidebar_link"]')
        logout_icon.click()

    def close_menu_bar(self):
        """Objective: closes menu bar
        by clicking on the icon
        """
        close_menu_icon = self.driver.find_element_by_xpath(
            '//*[@id="menu_button_container"]/div/div[2]/div[2]/div/button')
        close_menu_icon.click()

    def sort(self, param):
        """
        """
        pass

    def find_inventory_container(self, inventory_container_id):
        """ Objectve: Find inventory container
        """
        ## //*[@id="inventory_container"]/div/div[1]
        ## //*[@id="inventory_container"]/div/div[2]
        ## //*[@id="inventory_container"]/div/div[3]
        ## //*[@id="inventory_container"]/div/div[4]
        ## //*[@id="inventory_container"]/div/div[5]
        ## //*[@id="inventory_container"]/div/div[6]
        inventory_container = self.driver.find_element_by_xpath('//*[@id="inventory_container"]/div/div[' +
                                                                str(inventory_container_id) + ']')
        return inventory_container

    def find_all_inventory_container(self, array_inventory_container_id):
        """ Objective:
        """
        list_of_inventory_container = []
        for x in array_inventory_container_id:
            xpath = '//*[@id="inventory_container"]/div/div[{0}]'.format(str(x))
            list_of_inventory_container.append(self.driver.find_element_by_xpath(xpath))
        return len(list_of_inventory_container)

    def add_to_cart(self, inventory_id):
        button = self.find_inventory_container(inventory_id)
        button.click()

    ## //*[@id="inventory_container"]/div/div[1]/div[3]/button
    ## //*[@id="inventory_container"]/div/div[2]/div[3]/button

    def sort_products(self, option_id):
        """"""
        dropdown = self.driver.find_element_by_xpath('//*[@id="inventory_filter_container"]/select')
        dropdown.click()
        xpath = '//*[@id="inventory_filter_container"]/select/option[{0}]'.format(str(option_id))
        option = self.driver.find_element_by_xpath(xpath)
        option.click()

        ## //*[@id="inventory_filter_container"]/select/option[1]
        ## //*[@id="inventory_filter_container"]/select/option[2]
        ## //*[@id="inventory_filter_container"]/select/option[3]
        ## //*[@id="inventory_filter_container"]/select/option[4]

    def get_list_of_title_after_sort(self):
        """"""
        list_of_titles = []
        list_of_item = self.driver.find_elements_by_class_name('inventory_item_name')
        for x in list_of_item:
            list_of_titles.append(x.text)
        return list_of_titles

        ## //*[@id="item_5_title_link"]/div
        ## //*[@id="item_4_title_link"]/div
        # list_of_item_titles, known_ids = [], [0, 1, 2, 3, 4, 5]
        # for x in known_ids:
        #     xpath = '//*[@id="item_{0}_title_link"]/div'.format(str(x))
        #     list_of_item_titles.append(self.driver.find_element_by_xpath(xpath).text)

    def get_list_prices_after_sort(self):
        list_of_prices = []
        list_of_inventory_item_price = self.driver.find_elements_by_class_name('inventory_item_price')
        for x in list_of_inventory_item_price:
            list_of_prices.append(float(x.text.replace("$", "")))
        return list_of_prices

    ## todo move to different file - wrapper function
    def format_xpath(self, xpath: str, ID):
        """formats xpath"""
        pass

    ## todo move to a different file - wrapper function, might be delete
    def find_by_xpath(self):
        """"""
        pass
