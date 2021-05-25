import coach.constants as const
import os
from selenium import webdriver
#from coach.coach import coach
from selenium.webdriver.common.keys import Keys



class Coach(webdriver.Chrome):

    def __init__(self, driver_path = r":/Users/mehakgupta4691/Desktop/SeleniumDrivers",teardown                 =False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        

        super(Coach, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    
    def __exit__(self, exc_type, exc_val, exc_tb):
         if self.teardown:
             self.quit()

    
    def land_first_page(self):
        self.get(const.BASE_URL)
        no_press = self.find_element_by_css_selector('button[data-click="close"]')
        if no_press:
            no_press.click()
        else:
            print('did not find any element by this ID')
    def category(self):
        new_items = self.find_element_by_css_selector('li[tabindex="-1"]')
        if new_items:
            new_items.click()
        else:
            print('not able to find new items with class name')
    #def discount(self):
    #   continue_to_site = self.find_element_by_css_selector('button[data-attn-element-id="dvPn"]')
    #    if continue_to_site:
    #        continue_to_site.click()
    #    else:
    #        print('no discount coupon')
    def sort_price_lowest_first(self):
         element = self.find_element_by_css_selector(
             'li[data-id="price-low-to-high"]'
         )
         element.click() 
    


