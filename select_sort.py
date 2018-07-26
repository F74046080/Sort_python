n = int(input("Please input how many numbers you want to sort: "))
unsort = []

for i in range(n):
    print(i+1," number is", ": ", sep='', end='')
    unsort.append(int(input()))

sort = []
minimum = unsort[0]
min_index = 0
for i in range(n):
    for j in range(len(unsort)):
        if minimum > unsort[j]:
            min_index = j
            minimum = unsort[j]
    sort.append(unsort.pop(min_index))
    min_index = 0
    minimum = float("inf")

print("The sorted list is: ", sort)
