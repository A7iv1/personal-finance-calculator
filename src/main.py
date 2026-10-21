import json
import os
from datetime import datetime

# Имя файла для хранения данных
DATA_FILE = "data.json"

def load_data():
    """Загружает операции из файла, если он существует."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(operations):
    """Сохраняет операции в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(operations, f, ensure_ascii=False, indent=2)

def add_operation(operations):
    """Добавляет новую операцию (доход или расход)."""
    print("\n--- Добавление операции ---")
    op_type = input("Тип (доход/расход): ").strip().lower()
    
    if op_type not in ("доход", "расход"):
        print("Ошибка: введите 'доход' или 'расход'.")
        return
        
    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Ошибка: сумма должна быть числом.")
        return
        
    category = input("Категория: ").strip()
    date_str = input("Дата (ГГГГ-ММ-ДД, Enter для сегодня): ").strip()
    
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
        
    op = {"type": op_type, "amount": amount, "category": category, "date": date_str}
    operations.append(op)
    save_data(operations)
    print("Операция успешно добавлена.")

def list_operations(operations):
    """Выводит список всех операций."""
    print("\n--- Все операции ---")
    if not operations:
        print("Список операций пуст.")
        return
        
    for i, op in enumerate(operations, 1):
        sign = "+" if op["type"] == "доход" else "-"
        print(f"{i}. {op['date']} | {sign}{op['amount']:.2f} | {op['category']}")

def show_balance(operations):
    """Считает и выводит текущий баланс."""
    income = sum(op["amount"] for op in operations if op["type"] == "доход")
    expense = sum(op["amount"] for op in operations if op["type"] == "расход")
    
    print(f"\n--- Баланс ---")
    print(f"Общий доход: {income:.2f}")
    print(f"Общий расход: {expense:.2f}")
    print(f"Текущий баланс: {income - expense:.2f}")

def main():
    """Главная функция с интерактивным меню."""
    operations = load_data()
    
    while True:
        print("\n=== Калькулятор личных финансов ===")
        print("1. Добавить операцию")
        print("2. Показать все операции")
        print("3. Показать баланс")
        print("4. Выход")
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == "1":
            add_operation(operations)
        elif choice == "2":
            list_operations(operations)
        elif choice == "3":
            show_balance(operations)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")

if __name__ == "__main__":
    main()
