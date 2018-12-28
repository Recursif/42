import numpy as np
import tkinter as tk

from PIL import Image, ImageTk

def initArrayList():
    arrayList =[]
    for i in range(100):
        nb = str(i)
        name_image = "./bands/" + nb + ".png"
        array_image = np.array(Image.open(name_image).convert('L'))
        arrayList.append(np.flipud(array_image))
    return (arrayList)

def displayPaper(arrayList):
    window = tk.Tk()

    canvas = tk.Canvas(window, width=1000, height=1400)

    imgList = []
    for array in arrayList:
        img = Image.fromarray(array)
        imgList.append(ImageTk.PhotoImage(img))

    x = 0
    for i in range(lenList):
        canvas.create_image(x, 0, anchor="nw", image=imgList[i])
        x += 10

    canvas.pack()

    window.mainloop()


arrayList = initArrayList()

lenList = len(arrayList)

displayPaper(arrayList)

for i in range(lenList - 1):
    nextArrayList = list(arrayList)
    minimun = 1400*256
    index = - 1

    for j in range(lenList - i):
        diff = np.absolute(arrayList[i][:, -1] - arrayList[i + j][:, 0])
        diffR = np.absolute(arrayList[i][:, -1] - np.flipud(arrayList[i + j][:, 0]))

        min1 = np.sum(diff)
        min2 = np.sum(diffR)

        minima = min(min1, min2)

        if (minima < minimun):
            index = i + j
            minimun = minima


    if (i < index):
        nextArrayList = arrayList[:i + 1] + [arrayList[index]] + arrayList[i + 1: index] + arrayList[index + 1:]
        if (min1 > min2):
            print("ok")
            print(arrayList[j])
            nextArrayList[j] = np.flipud(arrayList[j])
            print(arrayList[j])
    arrayList = list(nextArrayList)

displayPaper(arrayList)
