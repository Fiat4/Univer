num = [int(x) for x in input().split()]
count = len(num)
for i in range(0, count - 1, 2):
    print(num[i + 1], num[i], end=" ")
if count % 2 != 0:
    print(num[count - 1])