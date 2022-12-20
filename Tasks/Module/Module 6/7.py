num = [int(x) for x in input().split()]
seen = set()
for number in num:
    if number in seen:
        print("Yes")
    else:
        print("No")
        seen.add(number)