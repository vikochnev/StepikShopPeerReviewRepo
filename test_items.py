from selenium.webdriver.common.by import By
import time


def test_add_to_cart_button_exists(browser, language_switch):
    lang_link = language_switch
    link = f'http://selenium1py.pythonanywhere.com/{lang_link}/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed(), "Element isn't displayed"

    # time.sleep(30)  # Uncomment for manual check
