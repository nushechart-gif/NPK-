# 🛡️ Шпаргалка: Обработка исключений (`try / except`)

**Исключение (Exception)** — это ошибка, которая возникает во время выполнения программы и останавливает её работу. Наша задача — не дать программе "упасть", а мягко обработать ошибку.

> 💡 **Главное правило:** предвидь, где пользователь может ввести что-то не то, и защити программу заранее.

---

## 📌 Зачем это нужно?

Без обработки исключений любая ошибка ломает программу:

```python
age = int(input("Введите возраст: "))  # Пользователь ввёл "двадцать"
# ❌ ValueError: invalid literal for int()
# Программа упала, игрок потерял прогресс!
```

С обработкой — программа продолжает работать:

```python
try:
    age = int(input("Введите возраст: "))
except ValueError:
    print("Ошибка: введите число!")
# ✅ Программа не упала, можно запросить ввод снова
```

---

## 🔧 Базовый синтаксис

```python
try:
    # Код, который может вызвать ошибку
    result = 10 / 0
except ZeroDivisionError:
    # Код, который выполнится, если произошла эта ошибка
    print("На ноль делить нельзя!")
```

---

## 🎯 Обработка нескольких типов ошибок

```python
try:
    age = int(input("Введите возраст: "))
    result = 100 / age
except ValueError:
    print("❌ Ошибка: нужно ввести число!")
except ZeroDivisionError:
    print("❌ Ошибка: возраст не может быть нулём!")
except Exception as e:
    # Ловит любую другую непредвиденную ошибку
    print(f"❌ Неизвестная ошибка: {e}")
```

> ⚠️ **Важно:** порядок `except` имеет значение! Более специфичные ошибки должны идти первыми.

---

## 🧩 Блоки `else` и `finally`

| Блок | Когда выполняется | Зачем нужен |
|------|-------------------|-------------|
| `try` | Всегда | Код, который может вызвать ошибку |
| `except` | Если произошла ошибка | Обработка ошибки |
| `else` | Если ошибки **не было** | Действия при успехе |
| `finally` | **Всегда**, независимо от ошибок | Закрытие файлов, освобождение ресурсов |

### Пример:

```python
try:
    file = open("save.txt", "r", encoding="utf-8")
    data = file.read()
except FileNotFoundError:
    print("❌ Файл сохранения не найден. Новая игра.")
    data = "start"
else:
    print("✅ Сохранение успешно загружено!")
finally:
    print("🔄 Операция завершена.")
```

---

## 📋 Основные типы исключений

| Исключение | Когда возникает | Пример |
|------------|-----------------|--------|
| `ValueError` | Неверное значение (нельзя преобразовать) | `int("abc")` |
| `TypeError` | Неверный тип операции | `"2" + 2` |
| `ZeroDivisionError` | Деление на ноль | `10 / 0` |
| `FileNotFoundError` | Файл не найден | `open("no.txt")` |
| `IndexError` | Индекс вне диапазона списка | `lst[100]` |
| `KeyError` | Ключа нет в словаре | `d["no_key"]` |
| `AttributeError` | Нет такого атрибута/метода | `"hi".no_method()` |
| `NameError` | Переменная не определена | `print(x)` |
| `Exception` | Базовый класс — ловит всё | Использовать осторожно |

📚 **Полный список:** [Built-in Exceptions — Python Docs](https://docs.python.org/3/library/exceptions.html)

---

## 🎮 Применение в текстовом квесте

### 1. Защита ввода HP игрока

```python
def get_player_hp():
    while True:
        try:
            hp = int(input("Введите здоровье игрока: "))
            if hp < 0:
                print("❌ Здоровье не может быть отрицательным!")
                continue
            return hp
        except ValueError:
            print("❌ Введите целое число!")
```

### 2. Безопасный расчёт среднего урона

```python
def calc_average_damage(damage_list):
    try:
        return sum(damage_list) / len(damage_list)
    except ZeroDivisionError:
        print("⚠️ Пока не было нанесённого урона.")
        return 0
```

### 3. Загрузка сохранения

```python
import json

def load_game(filename="save.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("✅ Сохранение загружено.")
        return data
    except FileNotFoundError:
        print("⚠️ Сохранение не найдено. Новая игра.")
        return {"hp": 100, "inventory": []}
    except json.JSONDecodeError:
        print("❌ Файл сохранения повреждён.")
        return {"hp": 100, "inventory": []}
```

---

## ❌ Частые ошибки новичков

### Ошибка 1: Пустой `except`

```python
# ❌ Плохо — ловит ВСЁ, включая Ctrl+C
try:
    do_something()
except:
    pass
```

```python
# ✅ Хорошо — ловим конкретную ошибку
try:
    do_something()
except ValueError as e:
    print(f"Ошибка: {e}")
```

### Ошибка 2: `except Exception` в начале

```python
# ❌ Плохо — остальные except никогда не сработают
try:
    ...
except Exception:
    ...
except ValueError:  # Недостижимый код!
    ...
```

### Ошибка 3: Забыли `return` в функции

```python
# ❌ Плохо — если ошибка, функция вернёт None
def get_number():
    try:
        return int(input("Число: "))
    except ValueError:
        print("Не число!")
        # Нет return!
```

---

## 🔄 Цикл `while True` + `try/except` — идеальная пара

Этот паттерн используется везде, где нужен надёжный ввод:

```python
def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value  # Выход из цикла при успехе
        except ValueError:
            print("❌ Пожалуйста, введите число.")
```

---

## 🎯 Практическое задание

Создайте файл `exceptions_practice.py` и выполните:

- [ ] **Задание 1:** Функция `get_player_hp()` с защитой от `ValueError` и отрицательных чисел
- [ ] **Задание 2:** Функция `calc_average_damage(damage_list)` с защитой от пустого списка
- [ ] **Задание 3:** Функция `load_game(filename)` с `try/except/else/finally`
- [ ] **Задание 4 (бонус):** Интегрировать эти функции в свой текстовый квест

---

## 📚 Полезные ссылки

- [Официальная документация: Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python Errors and Exceptions — GeeksforGeeks](https://www.geeksforgeeks.org/python-exception-handling/)
- [Real Python: Exceptions](https://realpython.com/python-exceptions/)
- 📖 **Книга:** *Грокаем алгоритмы*, А. Бхаргава — глава про обработку ошибок

---

## 💡 Шпаргалка-памятка

```python
try:
    # Пробуем сделать
    ...
except SpecificError:
    # Если конкретная ошибка
    ...
except AnotherError:
    # Если другая ошибка
    ...
except Exception as e:
    # Если что-то непредвиденное
    ...
else:
    # Если всё прошло успешно
    ...
finally:
    # Всегда (закрыть файл, освободить ресурс)
    ...
```

---

*Гр. 542 | Леонтьева Т.В. | Ноябрь 2026*  
*Тема 36-37: Обработка исключительных ситуаций*
