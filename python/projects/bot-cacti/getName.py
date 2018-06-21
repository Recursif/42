from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://fr.fakenamegenerator.com/gen-random-fr-fr.php')


while True:
    elem = browser.find_element_by_class_name("address")
    elem2 = elem.find_element_by_tag_name("h3")
    button = browser.find_element_by_id("genbtn")
    print(elem2.text)

    with open("namebis.txt", "a") as myfile:
        myfile.write(elem2.text + '/n')

    button.click()


#wait = WebDriverWait(browser, 1)

browser.quit()
