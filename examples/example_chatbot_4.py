# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import nlp

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":
	
	user_text		= 'SDFSDFSDFSDFSDFSDFSDFSDsdfsdfsdfdsf'
	
	###
	
	if nlp.is_gibberish(user_text):
		print('Szerintem csak szórakozol velem.')
	else:
		print('Ez egy valós üzenetnek tűnik!') # nem fogja kiírni