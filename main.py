from core.input_handler import get_choice, get_transaction_data
import os

def main():
    while True:
        choice = get_choice()
        if choice == "q":
            print("Выход из программы.")
            break
        elif choice == "1":
            get_transaction_data(is_income=True)
        elif choice == "2":
            get_transaction_data(is_income=False)
        else:
            print("Неверный выбор.")
    
if __name__ == "__main__":
    main()