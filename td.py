import csv
from transaction import Transaction
from datetime import datetime

def getRows(path: str) -> list[str]:
    rows = []
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows


def csv2transactions(path: str) -> list[Transaction]:
    transactions = []

    for row in getRows(path):
        description = row[1]
        date = datetime.strptime(row[0], "%m/%d/%Y")
        amount = float(row[2]) if row[2] else float(row[3])

        transactions.append(Transaction(date, description, amount))

    return transactions
