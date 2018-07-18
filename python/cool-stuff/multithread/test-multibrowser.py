

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

import os.path

import random
import queue 
import threading 
import time 

class myThread (threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def run(self):
        print ("Starting thread: " + str(self.threadID))
        get_urls(self.threadID, self.q)
        print ("Exiting thread: " + str(self.threadID))


def get_urls(threadID, q):
    while not exitFlag:
        
        

        queueLock.acquire()

        if not workQueue.empty():
            # Get remove and return an element from the queue work
           
            url = q.get()

            queueLock.release()
            browser = webdriver.Chrome()

            browser.get(url)

            time.sleep(10)

            browser.quit()
            
            queueLock.acquire()
            print ("thread %s processing %s" % (threadID, url))
            queueLock.release()
        else:
            queueLock.release()
            time.sleep(1)


date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

exitFlag = 0

urls = [
    "https://www.google.fr/search?q=Qui+%C3%A9tait+Georges+Lema%C3%AEtre+?&oi=ddle&ct=georges-lemaitres-124th-birthday-6611482312704000-law&hl=fr&kgmid=/m/01gr0d&source=doodle-ntp",
    "https://docs.python.org/3/library/xml.dom.html",
    "https://www.google.fr/search?ei=T8FMW62jO4emwQL2nY2oDQ&q=merch+trad&oq=merch+trad&gs_l=psy-ab.3..0j0i203k1l8j0.5956.6679.0.6852.5.5.0.0.0.0.108.447.4j1.5.0....0...1c.1.64.psy-ab..0.5.433...0i67k1.0.6D0P2TKVlfQ",
    "https://www.google.fr/search?q=stallman&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjSoJa2gaTcAhXEEVAKHUv2AMAQ_AUICigB&biw=835&bih=813#imgrc=yNMnLPtg3BDJjM:"
    "https://www.intelligenteconomist.com/url-shortener-services/",
    "https://www.ubuntu.com/",
    "https://fr.wikipedia.org/wiki/Preuve_%C3%A0_divulgation_nulle_de_connaissance",
    "https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_nombres",
    "https://cryptozombies.io/",
    "https://github.com/Recursif",
]

queueLock = threading.Lock()
workQueue = queue.Queue()

nbBrowsers = 10

threads = []
threadID = 1



# Create new threads 
for i in range(nbBrowsers):
    thread = myThread(threadID, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue 


queueLock.acquire()

for url in urls:
    workQueue.put(url)

queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete 
for t in threads:
    t.join()
print ("Exiting Main Thread")
