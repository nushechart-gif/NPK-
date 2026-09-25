# ============================================================
# КВЕСТ 3. С ФУНКЦИЯМИ
# Темы: функции, return, инвентарь (списки)
# Собирается после лекций 7-10
# ============================================================

# ---------- ФУНКЦИИ ----------

def show_menu():
    print("\n1 - Идти вперёд")
    print("2 - Отдохнуть")
    print("3 - Освоить местность")
    print("4 - Инвентарь")
    print("выход - Завершить игру")

def show_status(health, turns, money, inventory):
    print("\nЗдоровье:", health, "| Монеты:", money, "| Ход:", turns)
    print("Инвентарь:", inventory)

def apply_damage(health, damage):
    print("Ты получаешь урон", damage, "!")
    return health - damage

def heal(health, amount):
    print("Ты восстанавливаешь", amount, "здоровья.")
    return health + amount

def add_money(money, amount):
    return money + amount

def process_turn(choice, health, money, inventory):
    if choice == "1":
        money = add_money(money, 30)
        print("Ты нашёл монеты!")
    elif choice == "2":
        health = heal(health, 20)
    elif choice == "3":
        print("Ты нашла кафе.")
        action = input("Хочешь зайти? ").lower().strip()
        if action == "зайти":
            money = money - 1
            health = heal(health, 40)
        elif action == "пройти мимо":
            print("Ты ничего не нашла.")
        else:
            print("Я тебя не понял.")
    elif choice == "4":
        print("\nВ твоём рюкзаке:")
        for item in inventory:
            print("-", item)
    return health, money

# ---------- ОСНОВНАЯ ПРОГРАММА ----------

health = 100
turns = 0
money = 0
inventory = ["хлеб"]

print("Ты зашла в город.")

while True:
    show_status(health, turns, money, inventory)
    show_menu()

    choice = input("Твой выбор: ").lower().strip()

    if choice == "выход":
        print("Ты решила покинуть город.")
        break

    health, money = process_turn(choice, health, money, inventory)

    if health > 100:
        health = 100
    if money < 0:
        money = 0

    turns = turns + 1

print("Игра завершена. Ходов:", turns)
