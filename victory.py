import random

# Список известных людей и их даты рождения
people = {
    "Альберт Эйнштейн": "14.03.1879",
    "Исаак Ньютон": "04.01.1643",
    "Галилео Галилей": "15.02.1564",
    "Михаил Ломоносов": "19.11.1711",
    "Лев Толстой": "09.09.1828",
    "Александр Пушкин": "06.06.1799",
    "Федор Достоевский": "11.11.1821",
    "Чарльз Дарвин": "12.02.1809",
    "Вольфганг Моцарт": "27.01.1756",
    "Иван Павлов": "26.09.1849"
}

correct = 0
incorrect = 0

# Выбираем 5 случайных людей из списка
quiz_people = random.sample(list(people.keys()), 5)

# Месяцы для преобразования даты
months = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
    '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа',
    '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
}

# Проходим по каждому человеку
for person in quiz_people:
    print(f"Введите дату рождения {person} (в формате 'dd.mm.yyyy'):")
    user_answer = input()

    # Проверка на правильность ответа
    if user_answer == people[person]:
        print("Правильно!")
        correct += 1
    else:
        # Преобразование даты в формат "третье января 2009 года"
        day, month, year = people[person].split('.')
        formatted_date = f"{int(day)} {months[month]} {year} года"
        print(f"Неверно! Правильный ответ: {formatted_date}")
        incorrect += 1

# Вывод результатов
print(f"\nКоличество правильных ответов: {correct}")
print(f"Количество неправильных ответов: {incorrect}")