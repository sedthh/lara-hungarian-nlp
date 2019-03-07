# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import stemmer, nlp

''' Stemmer and n-gram example '''

if __name__ == "__main__":
	query = "Toto - Afrika"

	parts = query.split('-')
	artist = stemmer.inverse(parts[0], 'től')  # "tól" and "től" are both valid
	title = stemmer.inverse(parts[1], 't')
	the = nlp.az(title)

	print('A zenelejátszó program az alábbi számot játssza:')
	print(artist, the, title)
