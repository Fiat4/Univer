str = input()
length = len(str)
print(str[length // 2 + length % 2 :], str[: length // 2 + length % 2], sep="")