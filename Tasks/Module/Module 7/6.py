cities: dict[str, str] = {}
for _ in range(int(input("Количество стран: "))):
    cities_raw = input().split()
    for city in cities_raw[1:]:
        cities[city] = cities_raw[0]
output: list[str] = []
for _ in range(int(input("Количетсво поисков: "))):
    output.append(cities.get(input(), "Не найден"))
print("\n".join(output))