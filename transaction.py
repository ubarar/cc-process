from datetime import datetime

class Transaction():
	def __init__(self, date: datetime, description: str, amount: float):
		self.date = date
		self.description = description
		self.amount = amount

	def __repr__(self):
		return f"( date={self.date} desc={self.description[:10]}) amt={self.amount} )"

	def __lt__(self, other):
	        return self.date < other.date
