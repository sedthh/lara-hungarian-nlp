# -*- coding: UTF-8 -*-

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import tippmix, nlp

''' Stemmer and n-gram example '''

if __name__ == "__main__":
	text 	= '''
		A szövegbányászat a strukturálatlan vagy kis mértékben strukturált 
		szöveges állományokból történő ismeret kinyerésének tudománya; 
		olyan különböző dokumentumforrásokból származó szöveges ismeretek
		és információk gépi intelligenciával történő kigyűjtése és 
		reprezentációja, amely a feldolgozás előtt rejtve és feltáratlanul 
		maradt az elemző előtt. 
	'''
	
	# Generate bigrams from words in text
	tokens	= nlp.tokenizer(text)
	bigrams = nlp.ngram(tokens,2)
	print(bigrams)
	
	# Stem words and generate bigrams
	stems	= tippmix.stemmer(text)
	bigrams = nlp.ngram(stems,2)
	print(bigrams)
	
	# Generates bigrams from text after stopwords are removed
	text	= nlp.remove_stopwords(text)
	tokens	= nlp.tokenizer(text)
	bigrams = nlp.ngram(tokens,2)
	print(bigrams)
	
	# Stems remaining words and generates bigrams
	stems	= tippmix.stemmer(text)
	bigrams = nlp.ngram(stems,2)
	print(bigrams)
