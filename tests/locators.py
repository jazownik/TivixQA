from selenium.webdriver.common.by import By

class MainPageLocators:
    """A class for main page locators. All main page locators should come here"""
    CAREERS_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/ul/a[6]')
    ABOUT_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/ul/a[3]')
    

class AboutPageLocators:
    """A class for about page locators. """
    JOIN_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[1]/div[2]/div/a/div/button')
    CONTACT_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[1]/div[3]/a')

class CareersPageLocators:
    """A class for about page locators"""
    CURRENT_OPENINIGS_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[1]/section/div[1]/a')
    
    
