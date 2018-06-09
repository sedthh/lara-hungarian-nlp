# -*- coding: UTF-8 -*-

import re
import lara.nlp

# a stemmer that's slightly better than random guessing
def tippmix(text):
	if text:
		word_list	= lara.nlp.tokenize(text)
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
		elif word[-1] in ('a','e','u','ú','ű','ó','ő') and not vow:
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
					if word[-2] in ('a','á','o','u'):
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

# a stemmer for figuring out stems for words used in short questions
def just_asking(text):
	if text:
		word_list	= lara.nlp.tokenize(text.lower())
		results		= []
		for word in word_list:
			if len(word)>4:
				vh	= lara.nlp.vowel_harmony(word)
				if word[-1] in ('a','e'):
					if word[-2] in ('b','r'):
						if vh == 'magas':
							if word[-1] == 'e':
								word	= word[:-2]
						else:
							if word[-1] == 'a':
								word	= word[:-2]
				elif word[-1] == 't':
					if len(word)>4:
						if re.findall(r'(ameri[ck][aá]|eur[oó]p[aá]|eur[aá]zsi[aá]|afri[ck][aá]|[aá]zsi[aá])t', word, re.IGNORECASE):
							word	= word[:-1]
						else:							
							if vh == 'magas':
								if word[-2] in ('e','é'):
									word	= word[:-2]
								else:
									word	= word[:-1]
							else:
								if word[-2] in ('a','á','o','ó'):
									word	= word[:-2]
								else:
									word	= word[:-1]	
				elif word[-1] == 'l':
					if word[-2] in ('o','ó','ö','ő'):
						if word[-3] in ('b','r','t'):
							if word[-4]=='i':
								word	= word[:-4]
							else:
								word	= word[:-3]
					elif word[-2] in ('a','e'):
						if word[-3] =='v' or (word[-3]==word[-4] and lara.nlp.is_consonant(word[-3])):
							if vh == 'magas':
								if word[-2]=='e':
									if word[-4]=='i':
										word	= word[:-4]
									else:
										word	= word[:-3]
							else:
								if word[-2]=='a':
									if word[-4]=='i':
										word	= word[:-4]
									else:
										word	= word[:-3]
				elif word[-1] == 'n':
					if word[-3] == 'b':
						if vh == 'magas':
							if word[-2] == 'e':
								word	= word[:-3]
						else:
							if word[-2] == 'a':
								word	= word[:-3]
				if word[-1] == 'k':
					if word[-3]=='n' and word[-2] in ('a','e'):
						if vh == 'magas':
							if word[-2] == 'e':
								word	= word[:-3]
						else:
							if word[-2] == 'a':
								word	= word[:-3]
					if len(word)>4:
						if vh == 'magas':
							if word[-2] in ('e','é'):
								word	= word[:-2]
							else:
								word	= word[:-1]
						else:
							if word[-2] in ('a','á','o','ó'):
								word	= word[:-2]
							else:
								word	= word[:-1]	
				if word[-1] == 'i':
					if word != 'zokni' and word != 'hakni':
						if word[-2] == 'n':
							if vh == 'magas':
								if word[-3]=='e':
									word	= word[:-3]+'és'
								else:
									word	= word[:-2]+'és'
							else:
								if word[-3]=='a':
									word	= word[:-3]+'ás'
								else:
									word	= word[:-2]+'ás'
						else:
							word	= word[:-1]
				if len(word)>3 and word[-1] in ('á','é'):
					word	= word[:-1]+word[-1].replace('á','a').replace('é','e')
			results.append(word)
		return results	
	return []

# add affixes to words based on their vowel harmony	
def inverse(word,affix):
	word	= lara.nlp.trim(word)
	if not word:
		return ''
	vh		= lara.nlp.vowel_harmony(word.split()[-1])
	result	= word
	if not result[-1].isalnum():
		result	= result+"-"
	if affix in ('ra','re'):
		if word in ('a','az'):
			return 'arra'
		if word=='ez':
			return 'erre'
		if word[-1].lower() in ('a','e'):
			result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
		if vh == 'magas':
			return result+'re'
		else:
			return result+'ra'
	if affix in ('ba','be'):
		if word in ('a','az'):
			return 'abba'
		if word=='ez':
			return 'ebbe'
		if word[-1].lower() in ('a','e'):
			result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
		if vh == 'magas':
			return result+'be'
		else:
			return result+'ba'
	if affix in ('ban','ben'):
		if word in ('a','az'):
			return 'abban'
		if word=='ez':
			return 'ebben'
		if word[-1].lower() in ('a','e'):
			result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
		if vh == 'magas':
			return result+'ben'
		else:
			return result+'ban'
	if affix in ('k','s','t'):
		if word in ('a','az'):
			if affix=='k':
				return 'azok'
			if affix=='t':
				return 'azt'
		if word=='ez':
			if affix=='k':
				return 'ezek'
			if affix=='t':
				return 'ezt'
		if lara.nlp.is_vowel(word[-1]):
			if word[-1].lower() in ('a','e'):
				result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
			if len(result)==2:
				if word.lower()=="fű":
					return result[0]+"üve"+affix
				elif word.lower()=="tó":
					return result[0]+"ava"+affix
				elif word.lower()=="ló":
					return result[0]+"ova"+affix
			return result+affix
		test	= _inverse_only_o(result)	# exceptions
		if test:
			test2	= sum([lara.nlp.is_vowel(char) for char in result]) # more exceptions
			if test2<2:
				return result+test+affix
			return result[:-2]+result[-1]+test+affix
		if vh == 'magas':
			return result+'e'+affix
		elif vh == 'vegyes':
			return result+'o'+affix
		else:
			return result+'a'+affix
	if affix == 'i':
		if len(result)==2:
			if word.lower()=="fű":
				return result[0]+"üvi"
			elif word.lower()=="tó":
				return result[0]+"avi"
			elif word.lower()=="ló":
				return result[0]+"ovi"
		if word[-1]=='i':
			return result
		return result+'i'
	if affix in ('bol','ból','böl','ből','rol','ról','röl','ről','tol','tól','töl','től'):
		if word in ('a','az'):
			return 'a'+affix[0]+affix[0]+'ól'
		if word=='ez':
			return 'e'+affix[0]+affix[0]+'ől'
		if word[-1].lower() in ('a','e'):
			result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
		if vh == 'magas':
			return result+affix[0]+'ől'
		return result+affix[0]+'ól'
	if affix in ('nak','nek'):
		if word in ('a','az'):
			return 'annak'
		if word == 'ez':
			return 'ennek'
		if word[-1].lower() in ('a','e'):
			result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
		if vh in 'magas':
			return result+'nek'
		if result[0].lower()=='e':
			test2	= sum([lara.nlp.is_vowel(char) for char in result]) # more exceptions
			if test2<2:
				return result+'nek'
		return result+'nak'
	if affix in ('val','vel'):
		if word in ('a','az'):
			return 'azzal'
		if word == 'ez':
			return 'ezzel'
		if lara.nlp.is_vowel(word[-1]):
			if word[-1].lower() in ('a','e'):
				result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
			if vh == 'magas':
				return result+'vel'
			else:
				return result+'val'
		elif word[-1] == '-':
			if vh == 'magas':
				return result+'vel'
			else:
				return result+'val'
		else:
			if len(word)>1:
				if word[-2:].lower() in ('cs','gy','ly','ny','sz','ty','zs'):
					if word[-3].lower()!=word[-2].lower():
						result	= result[:-2]+result[-2]+result[-2]+result[-1]
					else:
						result	= result[:-2]+result[-2]+result[-1]
					if vh == 'magas':
						return result+'el'
					else:
						return result+'al'				
			if word[-2].lower()!=word[-1].lower():
				if vh == 'magas':
					return result+result[-1]+'el'
				else:
					return result+result[-1]+'al'
			else:
				if vh == 'magas':
					return result+'el'
				else:
					return result+'al'
	if affix in ('on','en','ön'):
		if word in ('a','az'):
			return 'azon'
		if word == 'ez':
			return 'ezen'
		if len(result)==2:
			if word.lower()=="fű":
				return "füvön"
			elif word.lower()=="tó":
				return "tavon"
			elif word.lower()=="ló":
				return "lovon"
		if word.lower()=="pécs":
			return "pécsett"
		elif word.lower()=="győr":
			return "győrött"
		elif word.lower()=="vác":
			return "vácott"
		if lara.nlp.is_vowel(word[-1]):
			if word[-1].lower() in ('a','e'):
				result	= result[:-1]+result[-1].replace('a','á').replace('e','é')
			return result+'n'
		test	= _inverse_only_o(result)	# exceptions
		if test:
			test2	= sum([lara.nlp.is_vowel(char) for char in result]) # more exceptions
			if test2<2:
				return result+test+'n'
			return result[:-2]+result[-1]+test+'n'
		if vh == 'magas':
			return result+'en'
		else:
			return result+'on'
			
	raise ValueError('Unsupported affix',affix)

def _inverse_only_o(word):
	vowel	= ''
	for char in word:
		if lara.nlp.is_vowel(char):
			if char not in ('o','O','ó','Ó','ö','Ö','ő','Ő'):
				return False
			else:
				vowel	= char
	return vowel.lower()
				