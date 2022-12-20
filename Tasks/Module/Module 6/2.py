num = [int(x) for x in input().split()]
for index, value in enumerate(num[1:]):
    if value > num[index]:
        print(value, end=" ")