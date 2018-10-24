

import os

K = 10

N = 20

if (K > N):
    print("nope")
    exit()

x = [str(x) for x in range(1, K + 1)]
y = [str(y) for y in range(N - K + 1, N + 1)]

print(x, y)

print(' '.join(x))

while (x != y):

    if (int(x[K - 1]) >= N):
        j = K - 1
        
   
        while(j > 0 and int(x[j]) >= N + j - K + 1):
            j -= 1
        
        x[j] =  str(int(x[j]) + 1)
        j += 1
        
        while (j > 0 and j <= K - 1):
            x[j] = str(int(x[j - 1]) + 1)
            j += 1
        
    else:
        x[K - 1] =  str(int(x[K - 1]) + 1)
    
    print(' '.join(x))

    