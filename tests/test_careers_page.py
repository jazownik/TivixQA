import pytest
import page

@pytest.mark.usefixtures("setup_test_page")
class Test_Shortest_Path_to_Careers_Page:
    def test_main_page_is_correct(self, setup_test_page):
        test_page = setup_test_page
        browser = page.MainPage(test_page)
        assert browser.is_title_matches(), "Tivix title doesn't match."
    
    def test_about_page_is_correct(self, setup_test_page):
        test_page = setup_test_page
        browser = page.MainPage(test_page)
        browser.click_about_button()
        new_page = page.AboutPage(test_page)
        assert new_page.is_title_matches(), "About page unreachable"
        

