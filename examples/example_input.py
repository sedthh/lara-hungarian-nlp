# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":

	user = input('Kérlek add meg a neved: ')

	disallow = entities.disallow()
	if parser.Intents(disallow).match_set(user):
		print('Sajnálom, de ezt a nevet nem választhatod, mert obszcén kifejezést tartalmaz!')
	else:
		print('Szervusz', user)
