import requests
import json
import datetime
import csv
from random import randint
#import matplotlib.pyplot as plt


base_url = 'https://api.trello.com/1/'
auth = f'?key={key}&token={token}'
to_do_list_board = 'SdLIdFg3'

class Account(object):

	base_url = 'https://api.trello.com/1/'

	def __init__(self, token, key):
		self.token = token
		self.key = key
		self.auth = f'?key={self.key}&token={self.token}'
		self.boards = []
		self.get_boards()
		self.get_lists()
		self.get_cards()

	def get_boards(self):
		to_do_list_board = Board('SdLIdFg3')
		self.boards.append(to_do_list_board)
	
	def get_lists(self):
		for board in self.boards:
			lists_url = self.base_url + 'boards/' + board.board_id + '/lists' + self.auth
			r = requests.get(lists_url)
			lists = r.json()
			for lst in lists:
				list_object = List(name=lst['name'], list_id=lst['id'])
				board.lists.append(list_object)

	def get_cards(self):
		for board in self.boards:
			for lst in board.lists:
				cards_url = self.base_url + 'lists/' + lst.list_id +'/cards' + self.auth
				r = requests.get(cards_url)
				cards = r.json()
				for card in cards:
					card_object = Card(card)
					lst.cards.append(card_object)
					
	def __repr__(self):
		return '<Account Object>'


class Board(object):

	def __init__(self, board_id):
		self.board_id = board_id
		self.lists = []

	def populate_lists(self):
		for i in self.lists:
			pass
	
	def __repr__(self):
		return f"<Board {self.board_id}>"


class List(object):

	def __init__(self, name, list_id):
		self.name = name
		self.cards = []
		self.list_id = list_id

	def __repr__(self):
		return f"<List {self.name}>"


class Card(object):

	def __init__(self, data):
		self.card_id = data['id']
		self.title = data['name']
		self.last_activity = data['dateLastActivity']
		self.labels = data['labels']

	def __repr__(self):
		return f"<Card: {self.card_id}>"


account = Account(token='a', 
					key='b')

for i in account.boards[0].lists[8].cards:
	print(i.__dict__)








"""
lists_and_cards = {}

def getLists():
	lists_url = base_url + 'boards/' + to_do_list_board + '/lists' + auth
	r = requests.get(lists_url)
	lists = r.json()
	return lists

def getCards(list_id):
	cards_url = base_url + 'lists/' + list_id +'/cards' + auth
	r = requests.get(cards_url)
	cards = r.json()
	return cards


def create_lists_and_cards():
	lists = getLists()
	for lst in lists[-5:]:
		cards = getCards(lst['id'])
		card_names = []
		for card in cards:
				card_names.append(card['name'])
		lists_and_cards[lst['name']] = card_names


def strip(card):
	takes a date card and gets rid of all the fluff
	#'*****----------20/04/2020----------'
	fluff = ['-', '*', '#']
	ok_characters = [x for x in card if x not in fluff]
	formatted_date = "".join(ok_characters)
	date_obj = datetime.datetime.strptime(formatted_date, "%d/%m/%Y").date()
	return date_obj


def splitLists(lists):
	weekdays = {}
	a = lists.items()
	for k,v in a:
		count = -1
		days = []	
		for card in v:
			if card[-1] == '-':
				#days[count]['count'] = len(days[count]['cards'])
				stripped_card = strip(card)
				days.append({'day': stripped_card, 'cards': []})
				count += 1
			else:
				days[count]['cards'].append(card)
		weekdays[k] = days
	return weekdays



create_lists_and_cards()
formatted_lists = splitLists(lists_and_cards)


def create_date_tasks_csv():
	with open('tracker.csv', 'w', newline='') as csvfile:
		for day_of_week in formatted_lists:
			writer = csv.DictWriter(csvfile, fieldnames=['day', 'date', 'tasks'])
			writer.writeheader()
			for i in formatted_lists[day_of_week]:
				writer.writerow({'day': day_of_week, 'date': str(i['day']), 'tasks': str(len(i['cards']))})

create_date_tasks_csv()







This is the code for plotting tasks using matplotlib, currently commented out becuase of pip issues installing numpy


stats = {}
for day_of_week in formatted_lists:
	stats[day_of_week] = []
	day = 1
	for date_info in formatted_lists[day_of_week]:
		stats[day_of_week].append({
			'date': day,
			'tasks': len(date_info['cards'])
			})
		day += 1

print(stats['Done Tuesday'])
plt.plot([i['date'] for i in stats['Done Wednesday']], [i['tasks'] for i in stats['Done Wednesday']])
plt.show()

"""




