nbLettres = (int)(input())

def abs(x):
    return(x if (x >= 0) else -x)


def dist(i, j, nbLettres):
    p = nbLettres
    for k in range(nbLettres):
        if (abs(i) < p - 1 and abs(j) < p - 1):
            p -= 1
    return (nbLettres - p)

for i in range(1 - nbLettres, nbLettres):
    s = ""
    for j in range(1 - nbLettres, nbLettres):
        s += (chr(97 + dist(i,j,nbLettres)))
    print (s)
