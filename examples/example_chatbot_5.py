# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Basic Chatbot that just prints out replies '''

if __name__ == "__main__":

	user_text = 'Már órák óta várok! Kérem adjon információt arról, hogy mennyi az egyenlegem. Köszönöm.'

	###

	tone = entities.tone()
	tone_match = parser.Intents(tone).match_best(user_text, 1)  # match_best
	common = entities.common()
	common_match = parser.Intents(common).match_set(user_text)

	if 'formal' in tone_match:
		if 'profanity' in common_match:
			print('Elnézését kérem a kellemetlenségét, de nem szükséges káromkodnia.')  # nem fogja kiírni
		print('Kérése feldolgozása folyamatban van.')
	elif 'informal' in tone_match:
		if 'profanity' in common_match:
			print('Sajnálom, hogy hibáztam, de azért nem kell így beszélni.')  # nem fogja kiírni
		print('Kérésedet elkezdtük feldolgozni.')  # nem fogja kiírni
	else:  # nem eldönthető
		if 'profanity' in common_match:
			print('Elnézést kérünk a kellemetlenségért.')  # nem fogja kiírni
		print('Kérés feldolgozása...')  # nem fogja kiírni
