import requests
import json
import os
from random import randint


class Account(object):

	base_url = 'https://api.trello.com/1/'
	api_key = os.environ['API_KEY']
	token = os.environ['TOKEN']
	auth = f'?key={api_key}&token={token}'

	def __init__(self):
		self.boards = []
		self.initialised = False
		self.test = {'monday': ['did x', 'did y']}
		if self.test_auth() == 'Success':
			print('Succesfully Initialised')
			self.initialised = True
		else:
			print("Failed to intialise")

	def auth_required(function):
		def wrapper( self ) :
			if self.initialised == True:
				function( self )
			else:
				print('Auth needed')
		return wrapper

	

		
	
	def test_auth(self):
		boards_url = f'https://api.trello.com/1/members/markgray7/boards?{self.auth}'
		r = requests.get(boards_url)
		if r.status_code == 200:
			return "Success"
		else:
			return "Failure"

	@auth_required
	def get_boards(self):
		to_do_list_board = Board('SdLIdFg3')
		self.boards.append(to_do_list_board)
	
	@auth_required
	def get_lists(self):
		for board in self.boards:
			lists_url = self.base_url + 'boards/' + board.board_id + '/lists' + self.auth
			r = requests.get(lists_url)
			lists = r.json()
			for lst in lists:
				list_object = List(name=lst['name'], list_id=lst['id'])
				board.lists.append(list_object)

	@auth_required
	def get_cards(self):
		for board in self.boards:
			for lst in board.lists:
				cards_url = self.base_url + 'lists/' + lst.list_id +'/cards' + self.auth
				r = requests.get(cards_url)
				cards = r.json()
				for card in cards:
					card_object = Card(card)
					lst.cards.append(card_object)

	@auth_required
	def get_info(self):	
		self.get_boards()
		self.get_lists()
		self.get_cards()

		print("Added boards, lists and cards")

					
	def __repr__(self):
		return '<Account Object>'


class Board(object):

	def __init__(self, board_id):
		self.board_id = board_id
		self.lists = []
	
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