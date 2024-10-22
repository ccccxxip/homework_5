# Читаем количество стран
N = int(input())

# Создаем словарь для хранения стран и их городов
country_city_map = {}

# Читаем данные о странах и городах
for _ in range(N):
    data = input().split()
    country = data[0]
    cities = data[1:]

    # Заполняем словарь
    for city in cities:
        country_city_map[city] = country

# Читаем количество запросов
M = int(input())

# Обрабатываем запросы
for _ in range(M):
    city_query = input().strip()
    # Находим страну по запросу и выводим её
    print(country_city_map.get(city_query, "Город не найден"))