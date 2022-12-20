ct = int(input())
s: dict[str, str] = dict([input().split() for _ in range(ct)])
query = input("Ключ:")
for key, value in s.items():
    if query == key:
        print(value)
    elif query == value:
        print(key)
    else:
        continue
    break