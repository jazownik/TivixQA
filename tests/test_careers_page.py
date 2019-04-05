import pytest
import page

@pytest.mark.usefixtures("setup_test_page")
class Test_Longest_Path_to_Careers_Page:
    def test_main_page_is_correct(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        assert browser.is_title_matches(), "Tivix title doesn't match."
    
    def test_about_page_is_correct_after_clicking_about_button(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        browser.click_about_button()
        new_page = page.AboutPage(setup_test_page)
        assert new_page.is_title_matches(), "About page unreachable"
    
    def test_careers_page_after_clicking_join_our_team_button(self, setup_test_page):
         browser = page.AboutPage(setup_test_page)
         browser.click_join_button()
         new_page = page.CareersPage(setup_test_page)
         assert new_page.is_title_matches(), "Careers page title doesn't match"

    def test_job_page_after_clicking_see_current_openings_button(self, setup_test_page):
         browser = page.CareersPage(setup_test_page)
         browser.click_openings_button()
         new_page = page.JobsPage(setup_test_page)
         assert new_page.is_title_matches(), "Jobs page title doesn't match"
        
@pytest.mark.usefixtures("setup_test_page")
class Test_Long_Path_to_Careers_Page:
    def test_main_page_is_correct(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        assert browser.is_title_matches(), "Tivix title doesn't match."
    
    def test_about_page_is_correct_after_clicking_about_button(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        browser.click_about_button()
        new_page = page.AboutPage(setup_test_page)
        assert new_page.is_title_matches(), "About page unreachable"
    
    def test_careers_page_is_correct_after_clicking_careers_button(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        browser.click_careers_button()
        new_page = page.CareersPage(setup_test_page)
        assert new_page.is_title_matches(), "Career page unreachable"

    def test_job_page_is_correct_after_clicking_openings_button(self, setup_test_page):
         browser = page.CareersPage(setup_test_page)
         browser.click_openings_button()
         new_page = page.JobsPage(setup_test_page)
         assert new_page.is_title_matches(), "Jobs page title doesn't match"
        
@pytest.mark.usefixtures("setup_test_page")
class Test_Shortest_Path_to_Careers_Page:
    def test_main_page_is_correct(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        assert browser.is_title_matches(), "Tivix title doesn't match."
    
    def test_career_page_is_correct_after_clicking_career_button(self, setup_test_page):
        browser = page.MainPage(setup_test_page)
        browser.click_careers_button()
        new_page = page.CareersPage(setup_test_page)
        assert new_page.is_title_matches(), "Careers page unreachable"
    
    def test_job_page_after_clicking_current_openings_button(self, setup_test_page):
         browser = page.CareersPage(setup_test_page)
         browser.click_openings_button()
         new_page = page.JobsPage(setup_test_page)
         assert new_page.is_title_matches(), "Jobs page title doesn't match"
