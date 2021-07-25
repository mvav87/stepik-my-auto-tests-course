from selenium import webdriver
import time
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver')
link = "http://suninjuly.github.io/huge_form.html"
 
try:
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for i in elements:
        i.send_keys("1")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)

    browser.quit()

