"""
ПРАКТИЧЕСКАЯ РАБОТА: Отладка ошибок в Python

Тема:
- чтение ошибок Python;
- поиск синтаксических, runtime и логических ошибок;
- исправление кода через запуск, traceback и отладчик VS Code.

Формат работы:
1. Запустите файл:
   python practice_debugging_errors.py

2. Вы увидите список проверок:
   [OK]    — задание выполнено правильно;
   [FAIL]  — программа работает, но результат неверный;
   [ERROR] — программа упала с ошибкой.

3. Исправляйте ТОЛЬКО функции в разделе "КОД ДЛЯ ИСПРАВЛЕНИЯ".
4. Тесты ниже менять нельзя.
5. После каждого исправления снова запускайте файл.

Что тренируем:
- NameError
- TypeError
- ValueError
- ZeroDivisionError
- IndexError
- KeyError
- FileNotFoundError
- логические ошибки

Как пользоваться отладчиком VS Code:
1. Поставьте breakpoint слева от номера строки.
2. Нажмите F5 или откройте Run and Debug.
3. Смотрите значения переменных слева.
4. Используйте:
   F10 — шаг через строку;
   F11 — шаг внутрь функции;
   Shift+F11 — выйти из функции.
"""

import os


# ============================================================
# КОД ДЛЯ ИСПРАВЛЕНИЯ
# ============================================================

# ------------------------------------------------------------
# Задание 1. NameError
# ------------------------------------------------------------
# Ошибка: переменная nme не существует.
# Нужно исправить имя переменной.
#
# Ожидаемый результат:
# greet("Аня") -> "Привет, Аня!"

def greet(name):
    return "Привет, " + nme + "!"


# ------------------------------------------------------------
# Задание 2. TypeError / преобразование типов
# ------------------------------------------------------------
# Сейчас функция складывает строки, а должна складывать числа.
#
# Ожидаемый результат:
# add_price("100", "50") -> 150

def add_price(price, delivery):
    return price + delivery


# ------------------------------------------------------------
# Задание 3. ZeroDivisionError
# ------------------------------------------------------------
# Сейчас при делении на ноль программа падает.
# Нужно вернуть 0, если делитель равен 0.
#
# Ожидаемый результат:
# safe_divide(10, 2) -> 5.0
# safe_divide(10, 0) -> 0

def safe_divide(a, b):
    return a / b


# ------------------------------------------------------------
# Задание 4. IndexError
# ------------------------------------------------------------
# Сейчас функция падает, если список пустой.
# Нужно вернуть None, если список пустой.
#
# Ожидаемый результат:
# first_item(["меч", "щит"]) -> "меч"
# first_item([]) -> None

def first_item(items):
    return items[0]


# ------------------------------------------------------------
# Задание 5. KeyError
# ------------------------------------------------------------
# Сейчас функция падает, если ключа нет в словаре.
# Нужно вернуть "нет данных", если ключ не найден.
#
# Ожидаемый результат:
# get_value({"name": "Олег"}, "name") -> "Олег"
# get_value({"name": "Олег"}, "age") -> "нет данных"

def get_value(data, key):
    return data[key]


# ------------------------------------------------------------
# Задание 6. ZeroDivisionError + логика
# ------------------------------------------------------------
# Сейчас функция падает на пустом списке.
# Нужно вернуть 0, если список пустой.
#
# Ожидаемый результат:
# average([10, 20, 30]) -> 20.0
# average([]) -> 0

def average(numbers):
    return sum(numbers) / len(numbers)


# ------------------------------------------------------------
# Задание 7. Логическая ошибка
# ------------------------------------------------------------
# Счётчик начинается с 1, хотя должен начинаться с 0.
#
# Ожидаемый результат:
# count_positive([1, -2, 3, 0, 5]) -> 3
# count_positive([-1, -2, 0]) -> 0

def count_positive(numbers):
    count = 1

    for number in numbers:
        if number > 0:
            count += 1

    return count


# ------------------------------------------------------------
# Задание 8. Логическая ошибка
# ------------------------------------------------------------
# Сейчас максимальное число ищется неправильно:
# max_value = 0 не подходит для списка из отрицательных чисел.
#
# Нужно:
# - если список пустой, вернуть None;
# - иначе вернуть максимальное число.
#
# Ожидаемый результат:
# find_max([3, 7, 2]) -> 7
# find_max([-10, -9, -30]) -> -9
# find_max([]) -> None

def find_max(numbers):
    max_value = 0

    for number in numbers:
        if number > max_value:
            max_value = number

    return max_value


# ------------------------------------------------------------
# Задание 9. Ошибка обработки строки
# ------------------------------------------------------------
# Функция должна подготовить команду игрока:
# - убрать пробелы по краям;
# - перевести в нижний регистр;
# - взять только первое слово.
#
# Ожидаемый результат:
# normalize_command("  GO north  ") -> "go"
# normalize_command("ВЗЯТЬ меч") -> "взять"
# normalize_command("   ") -> ""

def normalize_command(text):
    return text.lower()


# ------------------------------------------------------------
# Задание 10. Работа с файлами: запись
# ------------------------------------------------------------
# Сейчас функция открывает файл, но ничего не записывает.
# Нужно записать text в файл.
#
# Ожидаемый результат:
# после save_text("save.txt", "hello")
# внутри файла должен быть текст "hello"

def save_text(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("")


# ------------------------------------------------------------
# Задание 11. FileNotFoundError
# ------------------------------------------------------------
# Сейчас функция падает, если файл не найден.
# Нужно вернуть default, если файла нет.
#
# Ожидаемый результат:
# load_text("exists.txt") -> содержимое файла
# load_text("missing.txt", "нет файла") -> "нет файла"

def load_text(filename, default=""):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


# ============================================================
# ТЕСТЫ. ЭТОТ РАЗДЕЛ НЕ МЕНЯТЬ.
# ============================================================

def check_greet():
    return greet("Аня")


def check_add_price():
    return add_price("100", "50")


def check_safe_divide_normal():
    return safe_divide(10, 2)


def check_safe_divide_zero():
    return safe_divide(10, 0)


def check_first_item_normal():
    return first_item(["меч", "щит"])


def check_first_item_empty():
    return first_item([])


def check_get_value_exists():
    return get_value({"name": "Олег"}, "name")


def check_get_value_missing():
    return get_value({"name": "Олег"}, "age")


def check_average_normal():
    return average([10, 20, 30])


def check_average_empty():
    return average([])


def check_count_positive():
    return count_positive([1, -2, 3, 0, 5])


def check_count_positive_zero():
    return count_positive([-1, -2, 0])


def check_find_max_normal():
    return find_max([3, 7, 2])


def check_find_max_negative():
    return find_max([-10, -9, -30])


def check_find_max_empty():
    return find_max([])


def check_normalize_command_english():
    return normalize_command("  GO north  ")


def check_normalize_command_russian():
    return normalize_command("ВЗЯТЬ меч")


def check_normalize_command_empty():
    return normalize_command("   ")


def check_file_write_and_read():
    filename = "temp_debug_practice.txt"

    try:
        save_text(filename, "hello")
        result = load_text(filename, "нет файла")
        return result
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def check_load_missing_file():
    filename = "this_file_does_not_exist_12345.txt"
    return load_text(filename, "нет файла")


TESTS = [
    ("01. greet", check_greet, "Привет, Аня!"),
    ("02. add_price", check_add_price, 150),
    ("03. safe_divide normal", check_safe_divide_normal, 5.0),
    ("04. safe_divide zero", check_safe_divide_zero, 0),
    ("05. first_item normal", check_first_item_normal, "меч"),
    ("06. first_item empty", check_first_item_empty, None),
    ("07. get_value exists", check_get_value_exists, "Олег"),
    ("08. get_value missing", check_get_value_missing, "нет данных"),
    ("09. average normal", check_average_normal, 20.0),
    ("10. average empty", check_average_empty, 0),
    ("11. count_positive", check_count_positive, 3),
    ("12. count_positive zero", check_count_positive_zero, 0),
    ("13. find_max normal", check_find_max_normal, 7),
    ("14. find_max negative", check_find_max_negative, -9),
    ("15. find_max empty", check_find_max_empty, None),
    ("16. normalize_command english", check_normalize_command_english, "go"),
    ("17. normalize_command russian", check_normalize_command_russian, "взять"),
    ("18. normalize_command empty", check_normalize_command_empty, ""),
    ("19. file write and read", check_file_write_and_read, "hello"),
    ("20. load missing file", check_load_missing_file, "нет файла"),
]


def run_tests():
    print("=" * 60)
    print("ПРАКТИКА: ОТЛАДКА ОШИБОК В PYTHON")
    print("=" * 60)
    print()

    passed = 0
    failed = 0
    errors = 0

    for name, test_function, expected in TESTS:
        try:
            result = test_function()

            if result == expected:
                print(f"[OK]    {name}")
                passed += 1
            else:
                print(f"[FAIL]  {name}")
                print(f"        Ожидали: {expected!r}")
                print(f"        Получили: {result!r}")
                failed += 1

        except Exception as error:
            print(f"[ERROR] {name}")
            print(f"        {type(error).__name__}: {error}")
            errors += 1

    print()
    print("=" * 60)
    print("ИТОГ:")
    print(f"Успешно: {passed}")
    print(f"Неверный результат: {failed}")
    print(f"Ошибки выполнения: {errors}")
    print("=" * 60)

    if passed == len(TESTS):
        print("Отлично! Все ошибки исправлены.")
    else:
        print("Исправьте функции выше и запустите файл снова.")


if __name__ == "__main__":
    run_tests()
