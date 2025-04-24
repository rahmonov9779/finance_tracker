def save_transaction(is_income, source, amount, data_string):
    if is_income:
        filename = "data/income.txt"
    else:
        filename = "data/expense.txt"

    line = f"{data_string} | {source} | {amount} сомон\n"

    with open (filename, "a", encoding="utf-8") as file:
        file.write(line)