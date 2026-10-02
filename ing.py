import csv
from transaction import Transaction
from datetime import datetime

rate = 1.00

def getRows(path: str) -> list[str]:
    rows = []
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows


def ing_csv_to_transactions(path: str) -> list[Transaction]:
    transactions = []

    for row in getRows(path)[1:]:
        description = row[1]
        date = datetime.strptime(row[0], "%Y%m%d")
        amount = float(row[6].replace(',', '.'))
        if row[5] == "Credit":
            amount *= -1

        amount = amount*rate

        transactions.append(Transaction(date, description, amount))

    return transactions
