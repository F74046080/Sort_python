n = int(input("Please input how many numbers you want to sort: "))
unsort = []

for i in range(n):
    print(i+1," number is", ": ", sep='', end='')
    unsort.append(int(input()))

sort = []
minimum = unsort[0]
for i in range(n):
    sort.append(unsort.pop(0))
    if i > 0:
        if sort[i] < sort[i-1]:
            for j in range(i, 0, -1):
                if sort[j] < sort[j-1]:
                    sort[j], sort[j-1] = sort[j-1], sort[j]
print("The sorted list is: ", sort)
