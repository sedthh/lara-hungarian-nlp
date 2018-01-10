# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":
	
	user_text		= 'Lépj vissza a főmenübe és törölj mindent! Köszönöm.'
	
	###
	
	common			= entities.common()
	common_match	= parser.Intents(common).match_set(user_text)
	
	commands		= entities.commands()
	commands_match	= parser.Intents(commands).match_set(user_text)
	
	if 'hi' in common_match:
		print('Szia!') # nem fog kiíródni
	if 'thx' in common_match:
		print('Nagyon szívesen!') # kiíródik a 'Köszönöm' miatt
		
	if commands_match:
		print('Az alábbi feladatokat adtad ki a számomra:')
		print(commands_match)
	