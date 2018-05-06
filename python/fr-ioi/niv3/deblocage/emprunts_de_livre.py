nbLivres, nbjours = map(int, input().split())

listeDispo = []
for i in range(nbLivres):
    listeDispo.append(1)


for i in range(nbjours):
    nbClients = (int)(input())
    for j in range(nbClients):
        livre, duree = map(int, input().split())
        if (listeDispo[livre] > 1):
            print (0)
        else:
            listeDispo[livre] += duree
            print (1)

    for x in range(nbLivres):
        if (listeDispo[x] > 1):
            listeDispo[x] -= 1
