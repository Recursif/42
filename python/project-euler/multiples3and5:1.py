
sum = 0

print("entrez le nombres limit")
limit = int(input())

for i in range(3, limit):
    sum += i if (i % 5 == 0 or i % 3 == 0) else 0

print(sum)