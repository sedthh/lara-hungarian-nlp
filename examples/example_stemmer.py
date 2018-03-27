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
	
	# A szöveg szavaiból bigramokat generál
	tokens	= nlp.tokenize(text)
	bigrams = nlp.ngram(tokens,2)
	print(bigrams)
	
	# A szöveg szavait stemmeli és ezekből bigramokat generál
	stems	= tippmix.stemmer(text)
	bigrams = nlp.ngram(stems,2)
	print(bigrams)
	
	# A szöveg szavaiból bigramokat generál, miután eltávolította a stopszavakat
	text	= nlp.remove_stopwords(text)
	tokens	= nlp.tokenize(text)
	bigrams = nlp.ngram(tokens,2)
	print(bigrams)
	
	# A stopszavak eltávolítása után megmaradt szavakat stemmeli és ezekből generál bigramokat
	stems	= tippmix.stemmer(text)
	bigrams = nlp.ngram(stems,2)
	print(bigrams)
