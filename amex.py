import xlrd
from datetime import datetime
from transaction import Transaction

# convert an xls to a matrix - a rows of rows of string
def xls2mat(path : str) -> list[list[str]]:
	wb = xlrd.open_workbook(path)
	sh = wb.sheet_by_index(0)

	mat = []
	for rownum in range(sh.nrows):
		mat.append(sh.row_values(rownum))

	return mat

def parse_amount(amt : str) -> float:
	return float(amt.replace("$", "").replace(",", ""))

def parse_date(dat : str) -> datetime:
	return datetime.strptime(dat, "%d %b %Y")


# take a matrix, and just give me the rows of transactions
def mat2trans(mat: list[list[str]]) -> list[Transaction]:
	headers = ['Date', 'Description', 'Amount']
	i = 0	
	while i < len(mat) and len(set(headers).intersection(set(mat[i]))) != len(headers):
		i += 1

	cols = { h : mat[i].index(h) for h in headers} 

	rows = []
	for r in mat[i+1:]:
		description = r[cols['Description']]
		amount = parse_amount(r[cols['Amount']])
		date = parse_date(r[cols['Date']])

		# special parsing for date
		rows.append(Transaction(date, description, amount))

	return rows

def xls2transactions(path: str) -> list[Transaction]:
	return mat2trans(xls2mat(path))