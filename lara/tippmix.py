# -*- coding: UTF-8 -*-

import sys

#if 'lara.nlp' not in sys.modules:
#	import lara.nlp
import lara.nlp


# a stemmer that's slightly better than random guessing
def stemmer(text):
	if text:
		word_list	= lara.nlp.tokenizer(text)
		if word_list:
			results		= []
			for word in word_list:
				fix		= _tippmix_stemmer_get_prefix(_tippmix_stemmer_get_affix(word))
				results	+= fix
				
			return results		
	return []

def _tippmix_stemmer_accents(word):
	return word.replace('á','a').replace('é','e')
	
def _tippmix_stemmer_get_prefix(word):
	length			= len(word)
	if length<=3:
		return (word,)
	prefixes		= ("abba","alá","bele","benn","ellen","elő","fel","föl","hátra","hozzá","ide","körül","meg","mellé","neki","oda","össze","szét","túl","utána","vissza")
	strip_prefixes	= ("ala","elo","fol","hatra","hozza","korul","melle","ossze","szet","tul","utana")

	for item in prefixes:
		if len(item)+3<=length:
			if word.startswith(item):
				return (item,word[len(item):])
	for item in strip_prefixes:
		if len(item)+3<=length:
			if word.startswith(item):
				return (item,word[len(item):])
	return (word,)
	
def _tippmix_stemmer_get_affix(word):
	word= word.lower()
	if len(word)<=3:
		return word
		
	cnt	= 4
	vow= False
	if len(word)>11 and word.startswith('legesleg'):
		word	= word[8:]
	elif len(word)>6 and word.startswith('leg'):
		word	= word[3:]
	
	while len(word)>3 and cnt:
		cnt	-= 1
		vh	= lara.nlp.vowel_harmony(word)
		if word[-1] == word[-2]:
			word	= word[:-1]
		elif word[-1] in ('i','j'):
			if word[-1]	== 'i':
				vow	= False
			else:
				vow	= True
			word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
		elif word[-1] in ('a','e','u','ú','ű') and not vow:
			if word[-2] in ('b','n','r','t','v'):
				word	= word[:-2]
			else:
				if len(word)>3:
					word	= word[:-1]
				else:
					break
		elif word[-1] in ('d','m','s'):
			vow		= lara.nlp.is_vowel(word[-2])
			if vh=='mely' or vh=='vegyes':
				if word[-2] in ('a','á','o'):
					word	= word[:-2]
				else:
					break
			elif vh=='magas':
				if word[-2] in ('e'):
					word	= word[:-2]
				else:
					break
			else:
				break
		elif word[-1] in ('k'):
			if word[-3] in ('j','n','t'):
				vow		= lara.nlp.is_vowel(word[-2])
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('a','á','é','u','ü'):
						if word[-2] == 'a':
							vow	= False
						word	= word[:-3]
					else:
						if word[-2] in ('o','u','ü'):
							word	= word[:-2]
						else:
							word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				elif vh=='magas':
					if word[-2] in ('e','u','ü'):
						word	= word[:-3]
					else:
						if word[-2] in ('e','é'):
							word	= word[:-2]
						else:
							word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				else:
					break				
			else:
				vow		= lara.nlp.is_vowel(word[-2])
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('o','u','ü'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				elif vh=='magas':
					if word[-2] in ('e','é','u','ü'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				else:
					break
		elif word[-1] in ('g'):
			if word[-2] in ('i'):
				vow		= True
				word	= word[:-2]
			else:
				break;
		elif word[-1] in ('l'):
			if word[-3] in ('r','b'):
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('o','ó'):
						word	= word[:-3]
				elif vh=='magas':
					if word[-2] in ('o','ö','ő'):
						word	= word[:-3]
				break
			elif word[-3] in ('v'):
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('a'):
						word	= word[:-3]
				elif vh=='magas':
					if word[-2] in ('e'):
						word	= word[:-3]
				break
			else:
				vow		= lara.nlp.is_vowel(word[-2])
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('a','á','o'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				elif vh=='magas':
					if word[-2] in ('e','é','ü'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				else:
					break
		elif word[-1] in ('n'):
			if word[-3] in ('r','b'):
				vow		= False
				word	= word[:-3]
			else:
				vow		= lara.nlp.is_vowel(word[-2])
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('a','á','o','u','ü'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				elif vh=='magas':
					if word[-2] in ('e','é','u','ü'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				else:
					break		
		elif word[-1] in ('t'):
			if word[-3] in ('g','h'):
				vow		= False
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('a'):
						word	= word[:-3]
					else:
						break
				elif vh=='magas':
					if word[-2] in ('e'):
						word	= word[:-3]
					else:
						break
			else:
				vow		= lara.nlp.is_vowel(word[-2])
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('o','a','á'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				elif vh=='magas':
					if word[-2] in ('e','é'):
						word	= word[:-2]
					else:
						word	= word[:-2]+_tippmix_stemmer_accents(word[-2])
				else:
					break
		elif word[-1] in ('b'):
			if vh=='mely' or vh=='vegyes':
				if word[-2] in ('a','o'):
						word	= word[:-2]
				elif vh=='magas':
					if word[-2] in ('e'):
						word	= word[:-2]
			break
		elif word[-1] in ('z'):
			if word[-3] in ('h'):
				if vh=='mely' or vh=='vegyes':
					if word[-2] in ('o'):
						vow		= False
						word	= word[:-3]
					else:
						break
				elif vh=='magas':
					if word[-2] in ('e'):
						vow		= False
						word	= word[:-3]
					else:
						break
				else:
					break
			else:
				break
		else:
			break

	word	= word[:-1]+_tippmix_stemmer_accents(word[-1])
	
	return word
