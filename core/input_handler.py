def get_choice():
    choice=input("Выберите действие, 1(приход)/2(расход)")
    while choice !="1" and choice !="2":
        print ("Неверный выбор!")
    return choice

def get_transaction_data(is_income):
    if is_income:
        print ("Вы выбрали приход")
        source = input("Откуда пришли деньги?")
        amount = float(input("Сколько пришли?"))
    else:
        print ("Вы выбрали расход")
        source = input("Куда ушли деньги?")
        amount = float(input("Сколько ушло?"))
    return source, amount