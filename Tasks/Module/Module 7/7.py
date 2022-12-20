ct = int(input())
w: dict[str, int] = {}
for _ in range(ct):
    for word in input("").split():
        w[word] = w.get(word, 0) + 1
for key in sorted(words, key=words.get, reverse=True):  # type: ignore
    print(key, w[key])