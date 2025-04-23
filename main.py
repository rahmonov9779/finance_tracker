from datetime import datetime
from core.input_handler import get_choice, get_transaction_data
from core.logger import save_transaction

def main():
    choice = get_choice()
    is_income = choice == "1"
    
    source, amount = get_transaction_data(is_income)
    date_string = datetime.now().strftime("%Y-%m-%d %H:%M")

    save_transaction(is_income, source, amount, date_string)
    print("Данные успешно сохранены!")
    

if __name__ == "__main__":
    main()