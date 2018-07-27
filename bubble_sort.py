n = int(input("Please input how many numbers you want to sort: "))
unsort = []

for i in range(n):
    print(i+1," number is", ": ", sep='', end='')
    unsort.append(int(input()))

sort = unsort.copy()
minimum = unsort[0]
min_index = 0
for i in range(n):
    for j in range(1, n-i):
        if sort[j-1] > sort[j]:
            sort[j-1], sort[j] = sort[j], sort[j-1]
print("The sorted list is: ", sort)
