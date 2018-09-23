"""
print(ord("a"))

print(chr(97))
"""

"""
for i in range(26):
    print(chr(97 + i))
"""

i = 1
while (i <= 15):
    word = "a" * i
    print(word)
    j = 0
    k = 0
    while(j < i):
        word = list(word)
        word[i - j - 1] = chr(ord("a") + k)
        word = ''.join(word)
        print(word)
        k += 1
        #print(k)

        if (list(word)[i - j - 1] == "z"):
            k = 0
            j += 1
    i += 1

"""
i = 0
while (i <= 3):
    word = "a" * i
    print(word)
    j = 0
    while(j <= i):
        if (word[i -j] == "z"):
            j++
        word[i - j] = chr(ord("a") + k)
        print(word)

        
        
    
    i++

for i in range(10):
    word = ' ' * i
    for j in range(i):

        for k in range():
            letter = chr(97 + k)
        word += letter
    print (word)
"""