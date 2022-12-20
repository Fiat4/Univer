count = int(input())
words: dict[str, int] = {}
for _ in range(count):
    for word in input("").split():
        words[word] = words.get(word, 0) + 1
max = 0
mwords = []
for key, value in words.items():
    if value > max:
        max = value
        mwords = [key]
    elif value == max:
        mwords.append(key)
print(sorted(mwords)[0])