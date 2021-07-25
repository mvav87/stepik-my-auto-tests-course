from selenium import webdriver
import time
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver')
link = "http://suninjuly.github.io/registration1.html"

try:
    browser.get(link)
    first_name = browser.find_element_by_css_selector("input.form-control.first[placeholder='Input your first name']")
    last_name = browser.find_element_by_css_selector("input.form-control.second[placeholder='Input your last name']")
    email = browser.find_element_by_css_selector("input.form-control.third[placeholder='Input your email']")

    first_name.send_keys("Ivan")
    last_name.send_keys("Ivanov")
    email.send_keys("ivan@mail.ru")

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    time.sleep(5)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

