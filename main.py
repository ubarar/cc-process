import xlrd
from datetime import datetime
from amex import xls2transactions
from td import csv2transactions
import sys

from transaction import Transaction

def transactions2csv(transactions : list[Transaction]):
	for t in transactions:
		print(f"{t.date.strftime('%-d %b %Y')},{t.description.replace(',','_')},{t.amount}")

def main():
	transactions = []

	for file in sys.argv[1:]:
		if file.endswith("xls"):
			transactions += xls2transactions(file)
		else:
			transactions += csv2transactions(file)
	transactions.sort()

	transactions2csv(transactions)

if __name__ == "__main__":
	main()