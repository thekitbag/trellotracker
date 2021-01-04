
class Question(object):

	def __init__(self, text, options):
		self.text = text
		self.options = options
		self.body = ""

		for i in self.options:
			self.body += str(i) + ": " + self.options[i][0] + '\n'
		self.body += '\n'
	
	def ask(self):
		print(self.text)
		print("")
		a = int(input(self.body))
		action = self.options[a][1]
		action()


class Statement(object):

	def __init__(self, text):
		self.text = text

	def state(self):
		print(" ")
		print(self.text)
		print(" ")




		

	




