# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities, nlp

''' Basic chatbot that just prints out replies '''

if __name__ == "__main__":
	
	user_text		= 'Keress rá arra, hogy a dolmányos gödlicét mivel kell etetni!'
	
	###
	
	common			= entities.common()
	common_match	= parser.Intents(common).match_set(user_text)
	
	commands		= entities.commands()
	commands_match	= parser.Intents(commands).match_set(user_text)
	
	if 'hi' in common_match:
		print('Szia!') # nem fog kiíródni
	if 'thx' in common_match:
		print('Nagyon szívesen!') # nem fog kiíródni
		
	if 'search' in commands_match:
		print('Keressek rá erre?') 
		
		keywords		= nlp.strip_context(user_text,"search")
		print('"',keywords,'"')
	