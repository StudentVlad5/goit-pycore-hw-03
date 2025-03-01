'''
Завдання 1
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:
Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.

Рекомендації для виконання:
Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.

Критерії оцінювання:
Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.
'''

# As I would do on my own thinking
from datetime import datetime
import re

def get_days_from_today(date:str)->int|None:
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    today = datetime.today().date()
    if not re.fullmatch(pattern, date):
        print("Wrong date")
        return None
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        return (date_obj - today).days
    except ValueError:
        print("Wrong date")
        return None

# Роблю по інструкції
def get_days_from_today_i (date:str)->int|None:
    today = datetime.today().date()
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Wrong date")
        return None 
    return (date_obj - today).days

# Test 1
assert isinstance(get_days_from_today('2025-03-01'), int)
assert isinstance(get_days_from_today('2025-02-27'), int) 
assert isinstance(get_days_from_today('2025-02-01'), int) 
assert isinstance(get_days_from_today('2025-02-28'), int) 
assert get_days_from_today('2025-02-66') == None
assert get_days_from_today('202dfgdfg') == None
assert get_days_from_today('0') == None
assert get_days_from_today('') == None

# Test 1_1
assert isinstance(get_days_from_today_i('2025-03-01'), int)
assert isinstance(get_days_from_today_i('2025-02-27'), int) 
assert isinstance(get_days_from_today_i('2025-02-01'), int) 
assert isinstance(get_days_from_today_i('2025-02-28'), int) 
assert get_days_from_today_i('2025-02-66') == None
assert get_days_from_today_i('202dfgdfg') == None
assert get_days_from_today_i('0') == None
assert get_days_from_today_i('') == None

'''
Завдання 2

Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

Вимоги до завдання:
Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

Рекомендації для виконання:
Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.

Критерії оцінювання:
Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
Унікальність результату: усі числа у видачі повинні бути унікальними.
Відповідність вимогам: результат має бути у вигляді відсортованого списку.
Читабельність коду: код має бути чистим і добре документованим.

Приклад: Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка, де числа повинні бути у діапазоні від 1 до 49. Ви можете використати вашу функцію так:

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
'''

import random

def get_numbers_ticket(min: int = None, max: int = None, quantity: int = None) -> list[int]:
    if None in [min, max, quantity]:
        print("One of the arguments is missing")
        return [] 
    if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int):
        if 1 <= min < max <= 1000 and 1 <= quantity <= (max - min + 1):  
            try:
                win_numbers = random.sample(range(min, max + 1), quantity)
                return sorted(win_numbers)  
            except ValueError:
                print("Numbers are out of the range limits")
                return [] 
        else:
            print("Numbers are out of the range limits")
            return [] 
    else:
        print("For arguments, please use integers in the range from 1 to 1000")
        return [] 

# Test
assert get_numbers_ticket(1,49,6) 
assert get_numbers_ticket(-1,49,6) == [] 
assert get_numbers_ticket("a",49,6) == [] 
assert get_numbers_ticket(6) == [] 
assert get_numbers_ticket(1,-5) == [] 
assert get_numbers_ticket(0,0, 0) == [] 
assert get_numbers_ticket(10,1, 1) == [] 
assert get_numbers_ticket(1,50, 60) == [] 
assert get_numbers_ticket(1,5.5, 6.5) == [] 
assert get_numbers_ticket(1,5.5, 00000006.5) == [] 
assert get_numbers_ticket(1,10.5, 2) == [] 

'''
Завдання 3
У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах. Наприклад:
"    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
Ваш сервіс розсилок може ефективно відправляти повідомлення лише тоді, коли номери телефонів представлені у коректному форматі. Тому вам необхідна функція, яка автоматично нормалізує номери телефонів до потрібного формату, видаляючи всі зайві символи та додаючи міжнародний код країни, якщо потрібно.
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.

Вимоги до завдання:
Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
Функція видаляє всі символи, крім цифр та символу '+'.
Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду (додається '+38').
Функція повертає нормалізований телефонний номер у вигляді рядка.

Рекомендації для виконання:
Використовуйте модуль re для регулярних виразів для видалення непотрібних символів.
Перевірте, чи номер починається з '+', і виправте префікс згідно з вказівками.
Видаліть всі символи, крім цифр та '+', з номера телефону.
На забувайте повертати нормалізований номер телефону з функції.

Критерії оцінювання:
Коректність роботи функції: функція має правильно обробляти різні формати номерів, враховуючи наявність або відсутність міжнародного коду.
Читабельність коду: код має бути чистим, добре організованим і добре документованим.
Правильне використання регулярних виразів для видалення зайвих символів та форматування номера
'''
def normalize_phone(phone_number: str= None) ->str:
    if not phone_number:
        print("Arguments is missing")
        return ""
    pattern = r"[^\d+]"
    replacement = ""
    modified_phone_number= re.sub(pattern, replacement, str(phone_number))
    if not modified_phone_number.startswith("+"):
        if modified_phone_number.startswith("0"):  
            modified_phone_number = "+380" + modified_phone_number[1:]
        elif modified_phone_number.startswith("380"):  
            modified_phone_number = "+" + modified_phone_number
        else:
            modified_phone_number = "+380" + modified_phone_number  
    if len(modified_phone_number) == 13:
        return modified_phone_number 
    else: return ""

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    778788789,
]

# Test
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

'''
Завдання 4

У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

Вимоги до завдання:
Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').

Рекомендації для виконання:
Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
Визначте поточну дату системи за допомогою datetime.today().date().
Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.

Критерії оцінювання:
Актуальність та коректність визначення днів народження на 7 днів вперед.
Правильність обробки випадків, коли дні народження припадають на вихідні.
Читабельність та структурованість коду.

Приклад:

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Використання функції get_upcoming_birthdays:
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

Якщо сьогодні 2024.01.22 результатом може бути:
[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]
'''

from datetime import timedelta

celebrate_dates = ["2025.01.01", "2025.03.08", "2025.05.01", "2025.05.08", 
                   "2025.06.28", "2025.07.15", "2025.08.24", "2025.10.01", 
                   "2025.12.25", "2025.04.20", "2025.06.08"]

def is_weekend(date: datetime) -> bool:
    return date.weekday() >= 5

def get_next_working_day(date: datetime) -> datetime:
    while is_weekend(date):
        date += timedelta(days=1)
    return date

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    search_period = 7
    upcoming_birthdays = []

    if not isinstance(users, list) or len(users) <= 0:
        print("Please provide a valid list of users.")
        return upcoming_birthdays
    
    celebrate_month_day = [datetime.strptime(date, "%Y.%m.%d").strftime("%m-%d") for date in celebrate_dates]

    for user in users:
        try:
            date_obj = datetime.strptime(user["birthday"], "%Y.%m.%d")
        except ValueError:
            print(f"Please check the birthday format for user: {user["name"]} with birthday: {user["birthday"]}")
            continue
        if date_obj.month == 2 and date_obj.day == 29:
            try:
                date_obj = datetime.strptime(f"{today.year}.02.29", "%Y.%m.%d")
            except ValueError:
                date_obj = datetime.strptime(f"{date_obj.year}.03.01", "%Y.%m.%d")

        for delta in range(search_period + 1):
            check_date = today + timedelta(days=delta)
            if date_obj.month == check_date.month and date_obj.day == check_date.day:
                if date_obj.strftime("%m-%d") in celebrate_month_day or is_weekend(date_obj):
                    date_obj = get_next_working_day(date_obj)
                if (datetime.strptime(f"{today.year}-{date_obj.month}-{date_obj.day}", "%Y-%m-%d").date() - today).days <=7:
                    upcoming_birthdays.append({
                        "name": user["name"],
                        "congratulation_date": datetime.strptime(f"{today.year}-{date_obj.month}-{date_obj.day}", "%Y-%m-%d").strftime("%d.%m.%Y")
                    })
                break
    sorted_upcoming_birthdays = sorted(upcoming_birthdays, key=lambda x: datetime.strptime(x["congratulation_date"], "%d.%m.%Y"))
    return sorted_upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.04"},
    {"name": "Jane Doe", "birthday": "2000.02.29"},
    {"name": "Jane Doe", "birthday": "2000.08.24"},
    {"name": "Jane Doe", "birthday": "2000.03.08"},
    {"name": "Jane Doe", "birthday": "2000.03.09"},
    {"name": "Jane Doe", "birthday": "2000.03.07"},
    {"name": "Jane Smith", "birthday": "1990.03.a"},
    {"name": "Jane Smith", "birthday": "1990.04.12"},
    {"name": "Jane Barba", "birthday": ""},
    {"name": "Jane Barba", "birthday": "-45.45,54"},
]

# Test
upcoming_birthdays = get_upcoming_birthdays(users)
for birthday in upcoming_birthdays:
    print(birthday)