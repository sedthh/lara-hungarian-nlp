# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":
	
	user_text		= 'Szia! Szeretnék rendelni egy sajtos pizzát szalámival!'
	
	###
	
	order			= {
		"pizza"			: [{"stem":"pizza","wordclass":"noun"}],
		"cheese"		: [{"stem":"sajt","wordclass":"noun"}],
		"pepperoni"		: [{"stem":"szalámi","wordclass":"noun"}],
		"pineapple"		: [{"stem":"ananász","wordclass":"noun"}],
	}
	order_match		= parser.Intents(order).match_set(user_text)
	
	common			= entities.common()
	common_match	= parser.Intents(common).match_set(user_text)
	
	if 'hi' in common_match:
		print('Szia!') # kiíródik a 'Szia' miatt
	if 'thx' in common_match:
		print('Nagyon szívesen!') # nem fog kiíródni
		
	if 'pizza' in order_match:
		print('Ha jól értem egy pizzát szeretnél rendelni:') # kiíródik a 'pizzát' miatt
		if 'cheese' in order_match:
			print('sajttal') # kiíródik a 'sajtos' miatt
		if 'pepperoni' in order_match:
			print('szalámival') # kiíródik a 'szalámival' miatt
		if 'pineapple' in order_match:
			print('ananásszal') # nem íródik ki, mert bűncselekmény volna
	
	