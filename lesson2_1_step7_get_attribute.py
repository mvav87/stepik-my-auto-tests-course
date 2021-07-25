from selenium import webdriver
import time
import math
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver')
link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    gold_box_elt = browser.find_element_by_id("treasure")
    #узнаем значение атрибута для тега картинки
    x_elt = gold_box_elt.get_attribute("valuex")
    x = calc(int(x_elt))

    input_block = browser.find_element_by_id("answer")
    input_block.send_keys(x)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:
    time.sleep(10)
    browser.quit()