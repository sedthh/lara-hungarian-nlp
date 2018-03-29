# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":
	
	user_text		= 'Szia! Nem akarok rendelni semmit, csak érdekel, hogy hogy vagy!'
	
	###
	
	order			= {
		"pizza"			: [{"stem":"pizza","wordclass":"noun"}],
		"cheese"		: [{"stem":"sajt","wordclass":"noun"}],
		"pepperoni"	: [{"stem":"szalámi","wordclass":"noun"}],
		"pineapple"	: [{"stem":"ananász","wordclass":"noun"}],
	}
	order_match		= parser.Intents(order).match_set(user_text)
	
	common			= entities.common()
	common_match	= parser.Intents(common).match_set(user_text)
	
	smalltalk		= entities.smalltalk()
	smalltalk_match	= parser.Intents(smalltalk).match_set(user_text)
	
	if 'hi' in common_match:
		print('Szia!') # kiíródik a 'Szia' miatt
	if 'thx' in common_match:
		print('Nagyon szívesen!') # nem fog kiíródni
		
	if 'pizza' in order_match:
		print('Ha jól értem egy pizzát szeretnél rendelni:') # nem fog kiíródni
		if 'cheese' in order_match:
			print('sajttal') # nem fog kiíródni
		if 'pepperoni' in order_match:
			print('szalámival') # nem fog kiíródni
		if 'pineapple' in order_match:
			print('ananásszal') # nem fog kiíródni
	elif smalltalk_match:
		# nem valódi rendelés, csak beszélgetni akar az user
		if 'are_you_hungry' in smalltalk_match:
			print('Én éhes vagyok, ha te is az vagy, tudsz tőlem pizzát rendelni!') # nem fog kiíródni
		elif 'how_are_you' in smalltalk_match:
			print('Egész jól, annak ellenére, hogy egy Chatbot AI vagyok!')
