import xlrd
from datetime import datetime
from amex import amex_xls_to_transactions
from td import td_csv_to_transactions
from ing import ing_csv_to_transactions
import sys

from transaction import Transaction

def transactions2csv(transactions : list[Transaction]):
	for t in transactions:
		print(f"{t.date.strftime('%-d %b %Y')},{t.description.replace(',','_')},{t.amount:.2f}")

def main():
	transactions = []

	for file in sys.argv[1:]:
		if "NL" in file and "ING" in file:
			transactions += ing_csv_to_transactions(file)
		elif file.endswith("xls"):
			transactions += amex_xls_to_transactions(file)
		else:
			transactions += td_csv_to_transactions(file)
	transactions.sort()

	transactions2csv(transactions)

if __name__ == "__main__":
	main()