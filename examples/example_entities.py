# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import nlp, parser, entities

''' Remove previous matches from text '''

if __name__ == "__main__":

	user_text = 'Szia, köszönöm szépen a pizzát!'

	###

	match_common = parser.Intents(entities.common()).match_set(user_text)
	print(match_common)

	if match_common:
		# vegyük ki a már megtalált részeket
		clean_user_text = parser.Intents(entities.common()).clean(user_text)
		print(' '.join(nlp.tokenize(clean_user_text)))  # maradék szöveg
	else:
		print(user_text)  # nem fogja kiírni
