# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":

	user_text = '/echo "visszhang teszt"'

	###

	info = parser.Extract(user_text)  # /echo command
	commands = info.commands()
	func = commands[0]
	args = commands[1]

	if func:
		if func == 'ping':
			print('pong')
		elif func == 'echo':
			print(args)
	else:
		print('Parancs nélküli üzenet')  # nem íródik ki
