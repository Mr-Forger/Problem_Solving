list = [1,4,7,13,26,64,125,260,550]
k = 85
sum = []
i = len(list) - 1
while k > 0:
    if list[i] <= k:
        sum.append(list[i])
        k -= list[i]
    i -= 1
print(sum)
