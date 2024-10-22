# Читаем количество пар синонимов
N = int(input())

# Создаем словарь для хранения синонимов
synonym_dict = {}

# Читаем пары синонимов
for _ in range(N):
    word1, word2 = input().split()
    synonym_dict[word1] = word2
    synonym_dict[word2] = word1

# Читаем слово для поиска синонима
target_word = input().strip()

# Выводим синоним
print(synonym_dict.get(target_word, "Синоним не найден"))