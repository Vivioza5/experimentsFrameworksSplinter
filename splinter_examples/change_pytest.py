import pytest
from selenium import webdriver
from splinter import Browser
link = "http://selenium1py.pythonanywhere.com/"
browser = Browser('chrome')
class TestExperimentsSplinter():
    @pytest.mark.need_review
    def test_guest_should_see_login_link(self, browser):
        browser.visit(link)
        browser.find_by_css("#login_link")


    def test_some_browser_stuff(self,browser):
        """Test using real browser."""
        url = "http://www.google.com"
        browser.visit(url)
        browser.fill('q', 'splinter - python acceptance testing for web applications')
        # Find and click the 'search' button
        button = browser.find_by_name('btnK')
        # Interact with elements
        button.click()
        assert browser.is_text_present('splinter - python acceptance testing for web applications'), "splinter.cobrateam.info wasn't found... We need to"
        ' improve our SEO techniques'