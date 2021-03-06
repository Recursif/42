
import queue 
import threading 
import time 

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("Starting " + self.name)
        process_data(self.name, self.q)
        print ("Exiting " + self.name)

def process_data(threadName, q):
    """
    Cette boucle tourne tant que la queue n'est pas vide
    """
    while not exitFlag:
        
        queueLock.acquire()
        print(queueLock)
        print(workQueue.qsize())
        if not workQueue.empty():
            # Get remove and return an element from the queue work
            data = q.get()
            
            queueLock.release()
            time.sleep(2)
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
#print(workQueue.qsize())
threads = []
threadID = 1

queueLock.acquire()
# Create new threads 
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue 



for word in nameList:
    workQueue.put(word)
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



