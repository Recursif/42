

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


import os.path

from datetime import datetime


date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

url = "https://www.google.fr/search?q=Qui+%C3%A9tait+Georges+Lema%C3%AEtre+?&oi=ddle&ct=georges-lemaitres-124th-birthday-6611482312704000-law&hl=fr&kgmid=/m/01gr0d&source=doodle-ntp"


for i in range(3):
    browser = webdriver.Chrome()

    browser.get(url)

    time.sleep(10)