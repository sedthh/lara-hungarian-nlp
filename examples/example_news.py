# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

''' Find important keywords in a Hungarian news article '''

if __name__ == "__main__":
	article = 'Végre megnyerték az ötös lottó főnyereményét! A nyertes szelvényt a VII. kerületben adhatták fel!'

	###

	important = {
		"lottery": [{"stem": "lottó", "wordclass": "noun"}],
		"winning": [{"stem": "nyer", "wordclass": "verb"}, {"stem": "nyertes", "wordclass": "noun"}],
		"losing": [{"stem": "veszt", "wordclass": "verb"}, {"stem": "veszít", "wordclass": "verb"},
				   {"stem": "vesztes", "wordclass": "noun"}],
	}
	important_match = parser.Intents(important).match(article)

	location = entities.counties()
	locaiton_match = parser.Intents(location).match(article)

	print('Megtalált utalások a cikkben:')
	print(important_match)
	print(locaiton_match)

# A kapott pontok azért duplák, mert mind a helyes,
# mind a lehetséges "elgépelt" formákat megtalálta a szövegben az Intents()
# Ennek működéséről a dokumentációban olvashatsz többet.
