nbMesures = (int)(input())
diffMax = (float)(input())
list_mesures = [float(input()) for i in range(nbMesures)]

def abs(x):
    return (x if (x >= 0) else -x)

def computeLissage(list_moyenne):
    L = list(list_moyenne)
    for i in range(1,len(L) - 1):
        L[i] = (list_moyenne[i-1] + list_moyenne[i+1])/2
    return (L)

def lisse(list_moyenne, diffMax):
    for i in range(1, len(list_moyenne)):
        if (abs(list_moyenne[i] - list_moyenne[i-1]) > diffMax):
            return (False)
    return (True)

nbLissage = 0
while (not lisse(list_mesures, diffMax)):
    nbLissage += 1
    list_mesures = list(computeLissage(list_mesures))
print(nbLissage)
