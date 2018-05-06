partition = (str)(input())

i = 1

while (i < len(partition)):
    if (partition[i] == partition[i - 1]):
        partition = partition[:i - 1] + partition[i + 1:]
        i = 0
    i += 1

print (partition)
    
