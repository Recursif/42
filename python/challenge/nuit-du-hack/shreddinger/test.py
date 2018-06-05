import numpy as np
import tkinter as tk

from PIL import Image, ImageTk

def initArrayList():
    arrayList =[]
    for i in range(100):
        nb = str(i)
        name_image = "./bands/" + nb + ".png"
        array_image = np.array(Image.open(name_image).convert('L'))
        mat = 255* np.ones((array_image.shape[0],array_image.shape[1]))
        array = array_image

        arrayList.append(array)

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

def find_minimum_index(i , arrayList):
    rotate = 0
    minimum = 1400*256
    index = 0
    for j in range(i + 1, len(arrayList)):

        Vdiff1 = np.absolute(arrayList[i][:,:2] - arrayList[j][:, -2:])
        Vdiff2 = np.absolute(arrayList[i][:,:2] - np.fliplr(np.flipud(arrayList[j][:, -2:])))

        S1 = np.sum(Vdiff1)
        S2 = np.sum(Vdiff2)
        if (min(S1, S2) < minimum):
            minimum = min(S1, S2)
            index = j
    if (minimum == S2):
        rotate = 1
    return (index, rotate)




arrayList = initArrayList()

lenList = len(arrayList)

#displayPaper(arrayList)

i = 0
while (i < lenList - 2):

    index, rotate = find_minimum_index(i, arrayList)

    if (index > i):
        tmp = arrayList[index]
        arrayList[index] = arrayList[i]
        arrayList[i] = tmp;
        print(arrayList[i])

    if (rotate == 1):
         arrayList[index + 1] = np.fliplr(np.flipud(arrayList[index + 1]))
    i += 1

displayPaper(arrayList)
