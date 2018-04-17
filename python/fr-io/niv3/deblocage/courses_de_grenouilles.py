nbGrenouilles = (int)(input())
nbTours = (int)(input())
list_distances = [0 for i in range(nbGrenouilles)]
list_scores = [0 for i in range(nbGrenouilles)]


def findIndexMax(L):
    max = 0
    index_max = 0
    for i in range(len(L)):
        if (L[i] > max):
            max = L[i]
            index_max = i
    return (index_max)

def update(L, G):
    max = 0
    pmax = 0
    index_max = 0
    for i in range(len(L)):
        if (L[i] >= max):
            pmax = max
            max = L[i]
            index_max = i
    if (max > pmax):
        L[index_max] += 1
    return (L)

for i in range(nbTours - 1):
    numGrenouille, distance = map(int, input().split())
    list_distances[numGrenouille - 1] += distance
    list_scores = update(list_scores, list_distances)

first = findIndexMax(list_scores) + 1

print (first)
