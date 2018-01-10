# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import nlp

''' Rhythmic structure example '''

if __name__ == "__main__":
	huszt	= [
		'Bús düledékeiden, Husztnak romvára megállék;',
		'Csend vala, felleg alól szállt fel az éjjeli hold.',
		'Szél kele most, mint sír szele kél; s a csarnok elontott',
		'Oszlopi közt lebegő rémalak inte felém.',
		'És mond: Honfi, mit ér epedő kebel e romok ormán?',
		'Régi kor árnya felé visszamerengni mit ér?',
		'Messze jövendővel komolyan vess öszve jelenkort;',
		'Hass, alkoss, gyarapíts: s a haza fényre derűl! '
	]
	
	for line in huszt:
		metre	= nlp.metre(line)
		if nlp.is_hexameter(metre):
			print('hexameter\t(', 	nlp.number_of_syllables(line), ')\t',' '.join(metre))
		elif nlp.is_pentameter(metre):
			print('pentameter\t(', 	nlp.number_of_syllables(line), ')\t',' '.join(metre))
		else:
			print('invalid \t(', 	nlp.number_of_syllables(line), ')\t',' '.join(metre))

		