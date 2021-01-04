import csv

class CSV(object):

	def __init__(self, filename, board):
		self.filename = filename
		self.board = board
		self.test_data = {'board': self.board}

	def simple_extract(self):
		with open(self.filename, 'w', newline='') as csvfile:
			lists = self.board.lists
			for l in lists
			for day_of_week in self.data:
				writer = csv.DictWriter(csvfile, fieldnames=['day', 'date', 'tasks'])
				writer.writeheader()
				for i in self.data[day_of_week]:
					writer.writerow({'day': day_of_week, 'date': str(i['day']), 'tasks': str(len(i['cards']))})

	def test_populate(self):
		with open(self.filename, 'w', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=['board'])
			writer.writeheader()
			writer.writerow(self.test_data)
