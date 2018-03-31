import numpy as np
import tkinter as tk

from PIL import Image

photos = []


for i in range(100):
    nb = str(i)
    name_image = "./bands/" + nb + ".png"
    array_image = np.array(Image.open(name_image).convert('L'))
    firstL = array_image[:, 0]
    lastL = array_image[:, -1]
    print (firstL, lastL)
    photos.append([name_image, firstL, lastL])

len = len(photos)
window1 = tk.Tk()

canvas1 = tk.Canvas(window1, width=1000, height=1400)

i = 0
plomb = []
for photo in photos:
    plomb.append(tk.PhotoImage(file=photo[0]))

for j in range(len):
    canvas1.create_image(i,0, anchor="nw", image=plomb[j])
    i += 10
canvas1.pack()

window1.mainloop()



i = 0
while (i < len - 1):
    nextPhotos = list(photos)
    min = 1400*255
    index = i
    for j in range(len - i):
        moy = nextPhotos[i + j][1]
        for l in range(1,len(moy) - 1):
            moy[l]= nextPhotos[i + j][1]
        
        diff = nextPhotos[i][2] -
        res = np.absolute(diff)
        testMin = sum(res)
        print (testMin)
        if (testMin < min):
            print (testMin, "ok")
            index = i + j
            min = testMin
    if (i < index):
        nextPhotos = nextPhotos[:i + 1] + [nextPhotos[index]] + nextPhotos[i + 1: index] + nextPhotos[index + 1:]
    photos = list(nextPhotos)
    i += 1

"""
nextPhotos = list(photos)
min = 1500*255
index = i
j = 0
for j in range(len - i):
    diff = nextPhotos[i][1] - nextPhotos[i + j][2]
    res = np.absolute(diff)
    testMin = sum(res)
    if (testMin < min):
        index = i + j
        print(index)
        min = testMin
if (i < index):

photos = list(nextPhotos)

for k in range(5):
    for i in range(len - 1):
            nextPhotos = list(photos)
            min = 1400*255
            index = i
            for j in range(len - i):
                diff = nextPhotos[i][2] - nextPhotos[i + j][1]
                res = np.absolute(diff)
                testMin = sum(res)
                print (testMin)
                if (testMin < min):
                    print (testMin, "ok")
                    index = i + j
                    min = testMin
            if (i < index):
                nextPhotos = photos[:i - 1] + [photos[index]] + photos[i: index] + photos[index + 1:]

"""



window = tk.Tk()

canvas = tk.Canvas(window, width=1000, height=1400)

i = 0
plomb = []
for photo in photos:
    plomb.append(tk.PhotoImage(file=photo[0]))

for j in range(len):
    canvas.create_image(i,0, anchor="nw", image=plomb[j])
    i += 10
canvas.pack()

window.mainloop()
