from .logger import save_transaction
from datetime import datetime

def get_choice():
    choice = input("Выберите действие: 1 (приход), 2 (расход), q (выход): ").strip()
    return choice
date_string = datetime.now().strftime("%Y-%m-%d %H:%M")

def get_transaction_data(is_income):
    if is_income:
        print("Вы выбрали приход")
    else:
        print("Вы выбрали расход")
    
    while True:
        source = input("Откуда пришли деньги? (или q для выхода): " if is_income else "Куда ушли деньги? (или q для выхода): ")
        if source.lower() == "q":
            break
        amount_input = input("Сколько? (или q для выхода): ")
        if amount_input.lower() == "q":
            break
        try:
            amount = float(amount_input)
        except ValueError:
            print("Ошибка: введите число.")
            continue
        print(f"Сохраняем: {source} | {amount} | {date_string}")
       
    save_transaction(is_income, source, amount, date_string)
    print("Данные успешно сохранены!")