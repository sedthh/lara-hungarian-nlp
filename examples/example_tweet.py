# -*- coding: UTF-8 -*-

import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser

''' Process a Tweet easily '''

if __name__ == "__main__":
	tweet = '@sedthh ajánlj egy #nlp könyvtárat, amit 2017 februárjától kezdtek el írni ;)))9 https://github.com/sedthh/lara-hungarian-nlp'

	info = parser.Extract(tweet)

	print(tweet)
	print('Hashtags:', info.hashtags())
	print('Mentions:', info.mentions())
	print('Smileys:', info.smileys())
	print('URLs:', info.urls())
	print('Hun. date formats:', info.dates())
