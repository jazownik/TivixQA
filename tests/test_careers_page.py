import pytest
import page
import allure

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

@allure.feature("Jobs page-longest path")
class Test_Longest_Path_to_Careers_Page(BaseTest):
    @allure.step
    @pytest.mark.parametrize("start_url", ["https://www.tivix.com/"])
    def test_main_page_is_correct(self, start_url):
        self.driver.get(start_url)
        browser = page.MainPage(self.driver)
        browser.driver.save_screenshot("main_page.png")
        allure.attach.file(source="main_page.png", name="main_page", attachment_type=allure.attachment_type.PNG)
        assert browser.is_title_matches(), "Tivix title doesn't match."
    @allure.step
    def test_about_page_is_correct_after_clicking_about_button(self):
        browser = page.MainPage(self.driver)
        browser.click_about_button()
        browser.driver.save_screenshot("about_page.png")
        allure.attach.file(source="about_page.png", name="about_page", attachment_type=allure.attachment_type.PNG)
        new_page = page.AboutPage(self.driver)
        assert new_page.is_title_matches(), "About page unreachable"
    @allure.step
    def test_careers_page_after_clicking_join_our_team_button(self):
         browser = page.AboutPage(self.driver)
         browser.click_join_button()
         browser.driver.save_screenshot("careers_page.png")
         allure.attach.file(source="careers_page.png", name="careers_page", attachment_type=allure.attachment_type.PNG)
         new_page = page.CareersPage(self.driver)
         assert new_page.is_title_matches(), "Careers page title doesn't match"
    @allure.step
    def test_job_page_after_clicking_see_current_openings_button(self):
         browser = page.CareersPage(self.driver)
         browser.click_openings_button()
         browser.driver.save_screenshot("jobs_page.png")
         allure.attach.file(source="jobs_page.png", name="jobs_page", attachment_type=allure.attachment_type.PNG)
         new_page = page.JobsPage(self.driver)
         assert new_page.is_title_matches(), "Jobs page title doesn't match"
