# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import stemmer, nlp

''' Stemmer and n-gram example '''

if __name__ == "__main__":
	question = "Az elefántok füleiről mit lehet tudni?"

	stems = stemmer.just_asking(question)
	valid = [word for word in stems if len(word) > 3]

	search = ' '.join(valid)

	print("Keresés erre:", search)
