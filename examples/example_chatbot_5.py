# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":
	
	user_text		= 'Hasta la vista baby!'
	
	###
	
	references		= entities.popculture()
	references_match= parser.Intents(references).match_set(user_text)
	
	if references_match:
		print('Értem, egy másik AI-ra utaltál az üzenetedben.')
		if 'terminator' in references_match:
			print('Visszatérek!')
	else:
		print('Ez egy valós üzenetnek tűnik!') # nem fogja kiírni