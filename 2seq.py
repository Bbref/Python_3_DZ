user_input = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Определение разделителя
if ',' in user_input:
    delimiter = ','
elif ';' in user_input:
    delimiter = ';'
elif '/' in user_input:
    delimiter = '/'
else:
    print("Ошибка: допустимые разделители - запятая, точка с запятой или слэш.")
    exit()

# Проверка на смешивание разделителей
if any(d in user_input for d in [',', ';', '/']) and delimiter not in user_input:
    print("Ошибка: использование нескольких различных разделителей.")
    exit()

# Разделение строки на элементы
elements = user_input.split(delimiter)
print(elements)

# Преобразование элементов в целые числа
elements = list(map(int, elements))

# Создание списка уникальных элементов
unique_elements = [element for element in elements if elements.count(element) == 1]

# Вывод результата
print("Результат:", ", ".join(map(str, unique_elements)))
