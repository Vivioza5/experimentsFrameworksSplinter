import pytest
from selenium import webdriver
from splinter import Browser
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = Browser('chrome')
    yield browser
    print("\nquit browser..")
    browser.quit()