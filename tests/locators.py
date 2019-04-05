from selenium.webdriver.common.by import By

class MainPageLocators:
    """A class for main page locators. All main page locators should come here"""
    CAREERS_BUTTON = (By.NAME, 'careers')
    ABOUT_BUTTON = (By.NAME, 'about')

class AboutPageLocators:
    """A class for about page locators. """
    JOIN_BUTTON = (By.NAME, 'join our team')
    CONTACT_BUTTON = (By.NAME, "let's build something great")

class CareersPageLocators:
    """A class for about page locators"""
    CURRENT_OPENINIGS_BUTTON = (By.NAME, 'SEE CURRENT OPENINGS')
    
