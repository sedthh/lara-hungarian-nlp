# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import nlp

''' Process a Tweet easly '''

if __name__ == "__main__":
	
	tweet	= '@sedthh ajánlj egy #nlp könyvtárat, amit 2017 februárjától kezdtek el írni :) https://github.com/sedthh/lara-hungarian-nlp'
	
	print(tweet)
	print('Hashtags:',			nlp.find_hashtags(tweet))
	print('Mentions:',			nlp.find_mentions(tweet))
	print('Smileys:',			nlp.find_smileys(tweet))
	print('URLs:',				nlp.find_urls(tweet))
	print('Hun. date formats:',	nlp.find_dates(tweet))
	