import pytest
from selenium.webdriver.common.by import By


def test_check_add_to_basket(browser, language):
    #Checking if there is an button add to basket
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)

    result = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(result) > 0, 'Button not found'
    
