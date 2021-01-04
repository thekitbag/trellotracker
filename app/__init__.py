from app.cli import Question, Statement
from app.models import Account
from app.csvexport import CSV


welcome_message = Statement("Welcome to Trello Tracker, let's get started")
a = Account()
a.get_info()
Statement('Added boards: ' + str(a.boards))

def test_f1():
	"""this will be replaced by a class method"""
	print("printing lists in board")



csv = CSV(filename='tracker.csv', board=a.boards[0])
q1 = Question('What would you like to do next?', { 1: ('View Lists in Board', test_f1),
											2: ('Download to CSV', csv.simple_extract)

	})

q1.ask()





