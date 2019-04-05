from element import BasePageElement
from locators import MainPageLocators, AboutPageLocators, CareersPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Tivix" in self.driver.title

    def click_about_button(self):
        """Triggers about page"""
        element = self.driver.find_element(*MainPageLocators.ABOUT_BUTTON)
        element.click()
    
    def click_careers_button(self):
        """triggers careers page"""
        element = self.driver.find_element(*MainPageLocators.CAREERS_BUTTON)
        element.click()


class AboutPage(BasePage):
    """Search results page action methods come here"""
    def is_title_matches(self):
        """Verifies that the hardcoded text "About" appears in page title"""
        return "About" in self.driver.title

    def click_join_button(self):
        element = self.driver.find_element(*AboutPageLocators.JOIN_BUTTON)
        element.click()
    
    def click_contact_button(self):
        element = self.driver.find_element(*AboutPageLocators.CONTACT_BUTTON)
        element.click()

class CareersPage(BasePage):
    def is_title_matches(self):
        """Verifies that the hardcoded text "Careers" appears in page title"""
        return "Careers" in self.driver.title
    
    def click_openings_button(self):
        element = self.driver.find_element(*CareersPageLocators.CURRENT_OPENINIGS_BUTTON)
        element.click()

class JobsPage(BasePage):
    def is_title_matches(self):
        return "Tivix" in self.driver.title