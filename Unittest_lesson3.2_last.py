import unittest
from selenium import webdriver
import time
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver')
link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

#Создаем свой класс и наследуем его от класса TestCase.
#переписали функции в методы, добавив ссылку на экземпляр класса self, в качестве первого аргумента.
class MyUnit(unittest.TestCase):
    def test_registrations_ok(self):
        browser.get(link)
        first_name = browser.find_element_by_css_selector(
            "input.form-control.first[placeholder='Input your first name']")
        last_name = browser.find_element_by_css_selector(
            "input.form-control.second[placeholder='Input your last name']")
        email = browser.find_element_by_css_selector("input.form-control.third[placeholder='Input your email']")

        first_name.send_keys("Ivan")
        last_name.send_keys("Ivanov")
        email.send_keys("ivan@mail.ru")

        button = browser.find_element_by_css_selector(".btn.btn-default")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
#Переписали простой ассерт, на тот который используется в юнит тестах (другой синтаксис).
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Тест не прошел")

        time.sleep(5)
        browser.quit()

    def test_registrations_NOK(self):
        browser.get(link2)
        first_name = browser.find_element_by_css_selector(
            "input.form-control.first[placeholder='Input your first name']")
        last_name = browser.find_element_by_css_selector(
            "input.form-control.second[placeholder='Input your last name']")
        email = browser.find_element_by_css_selector("input.form-control.third[placeholder='Input your email']")

        first_name.send_keys("Ivan")
        last_name.send_keys("Ivanov")
        email.send_keys("ivan@mail.ru")

        button = browser.find_element_by_css_selector(".btn.btn-default")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, f"тест не прошел")

        time.sleep(5)
        browser.quit()

#Не вдаваясь в подробности, скажем только, что конструкция if __name__ == "__main__"
# служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля.
#ТУТ обязательно ИЗУЧИТЬ ПОДРОБНЕЕ урок 3.2 - 10 там есть ссылка на видео
if __name__ == "__main__":
    unittest.main()
