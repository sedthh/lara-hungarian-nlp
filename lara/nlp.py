# -*- coding: UTF-8 -*-

import re
import unicodedata

def strip_accents(text):
	if text:
		return str(unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore'),'utf-8')
	return ''
	
def trim(text):
	if text:
		return re.sub(r'\s+',' ',text.strip())
	return ''
	
def remove_punctuation(text, replace=''):
	return re.sub(r'[^\w\s]', replace, text)
	
def remove_double_letters(text, replace=''):
	if text:
		return replace.join([text[i] for i in range(len(text)-1) if text[i+1]!= text[i]]+[text[-1]])
	return ''

def remove_space_between_numbers(text, replace=''):
	if text:
		return re.sub(r'(?<=\d)[\s\\\-/]+(?=\d)', replace, text)
	return ''
		
def remove_urls(text, replace=''):
	if text:
		return re.sub(r'(((https?://)|(www))([-\w\.]+[-\w])+(:\d+)?(/([\w/_\.#-]*(\?\S+)?[^\.\s])?)?)', replace, text)
	return ''
		
def remove_email_addresses(text, replace=''):
	if text:
		return re.sub(r'[^@\s]*@[^@\s]*\.[^@\s]*', replace, text)
	return ''
		
def remove_html_tags(text, replace=''):
	if text:
		return re.sub(r'(<!--.*?-->|<[^>]*>)', replace, text)
	return ''

def remove_smileys(text,replace=''):
	if text:
		return re.sub(r'([:;]-?[Dd\(\)3]+)\b', replace, text)
	return ''

def find_hashtags(text):
	if text:
		return ['#{0}'.format(hashtag) for hashtag in re.compile(r'\B#([\w0-9_\-\']+)\b').findall(text)]
	return []
	
def find_mentions(text):
	if text:
		return ['@{0}'.format(mention) for mention in re.compile(r'\B@([\w0-9_\-\'\.]+)\b').findall(text)]
	return []
	
def find_urls(text):
	if text:
		return re.compile(r'\b(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})').findall(text)
	return []
	
def find_smileys(text):
	if text:
		return re.compile(r'([:;]-?[Dd\(\)3]+)\b').findall(text)
	return []
	
def vowel_harmony(word, vegyes=True):
	if word:
		mely	= re.compile('[aáoóuú]', re.IGNORECASE)
		magas	= re.compile('[eéiíöőüű]', re.IGNORECASE)
		mely_m	= len(mely.findall(word))
		magas_m	= len(magas.findall(word))
		if magas_m and mely_m:
			if vegyes:
				return 'vegyes'
			return 'magas'
		if magas_m>mely_m:
			return 'magas'
		return 'mely'
	return 'hiba'

def is_vowel(letter):
	if letter:
		return (letter.lower() in ('a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű'))
	return False

def is_consonant(letter):
	if letter.isalpha():
		return (not is_vowel(letter))
	return False
	
def vowel_ending(word):
	if word:
		return is_vowel(word[-1])
	return False

def consonant_ending(word):
	if word:
		return is_consonant(word[-1])
	return False

def vowel_beginning(word):
	if word:
		return is_vowel(word[1])
	return False

def consonant_beginning(word):
	if word:
		return is_consonant(word[1])
	return False	
	
def crop_text(text,limit=100,end='...',reverse=False):
	if text:
		n		= 0
		output	= ''
		cache	= ''
		length	= len(text)
		for i in range(length):
			if reverse:
				char	= text[length-1-i]
			else:
				char	= text[i]
				
			if char.isalnum():
				if reverse:
					cache	= char+cache
				else:
					cache	= cache+char
			else:
				if len(output)+len(cache)>limit:
					if len(output)<length:
						if output:
							if reverse:
								return end+output[1:]
							else:
								return output[:-1]+end
						return end
					else:
						return output
				else:
					if reverse:
						output	= char+cache+output
					else:
						output	+= cache+char
					cache	= ''
			n	+= 1
			if n>limit:
				cache	= ''
				break
		if cache:
			if reverse:
				output	= cache+output
			else:
				output	+= cache
		if len(output)<length:
			if output:
				if reverse:
					return end+output[1:]
				else:
					return output[:-1]+end
			return end
		return output			
	return ''
	
def number_of_words(text):
	if text:
		return len(tokenizer(text))
	return 0

def tokenizer(text):
	if text:
		return re.findall('[\w\-_\']+', text)
	return []
	
def is_gibberish(text=''):
	length	= float(len(text))
	if length>6:
		if find_urls(text):
			return False
		for char in text:
			if char>='0' and char<='9':
				return False
				
		text		= text.lower()
		redflags	= 0
		# number of different characters
		unique		= float(len(list(set(text))))
		if unique<4 or unique/length<.33:
			redflags	+= 1
		# vowel ratio
		vowels		= 0.0
		for char in text:
			if is_vowel(char):
				vowels	+= 1.0
		if vowels:
			if length/vowels<.25:
				redflags	+= 1
		else:
			redflags	+= 1
		# length of words
		if length/float(number_of_words(text))>9:
			redflags	+= 1
		# 4 consonants next to each other
		consonants	= 0
		szy			= 0
		for char in text:
			if is_consonant(char):
				if char in ('s','z','y'):
					szy			+= 1
				consonants	+= 1
			else:
				consonants	= 0
				szy			= 0
			if consonants>4 and not szy:
				redflags	+= 1
				break
			elif consonants>5:
				redflags	+= 1
				break
			
		if redflags>1:
			return True
	return False
	
#TODO: more contexts
def strip_context(text, context="search", including=None):
	if text:
		if context=='search':
			exclude		= re.compile(r'\b((a(z|rra)?)|(azok(ra)?)|(milyen)|(mennyi)|(mikor)|(hol)|(merre)|(hova)|([mk]i(vel|nek))|(mi?[eé]rt)|(r[aá])|(egy)|(mi(t|k(et)?)?)|(meg)|(be)|(nekem)|(hogy(an)?)|((sz[oó])?cikk\w*)|(oldal\w*)|([ií]r\w*)|(kapcsolat(os(an)?|ban))|(sz[oó]l[oó]?)|(keres\w*)|(n[eé]z[zd])|(mutas(s[aá][dl]|[sd]))|(alapj[aá]n)|(mond[dj]?)|(t[oö]ltse?d?)|(hoz([zd]|z[aá][dl]))|(nyis([ds]|s[aá][dl]))|(megnyit\w*)|((el)?olvas\w*)|(szeretn[eé]\w*)|(k[eé]r(ni|l?e[km]))|(megn[eé]z\w*)|(k[oö]z[oö]tt))\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		elif context=='request':
			exclude		= re.compile(r'\b((a(z|rra)?)|(azok(ra)?)|([io]lya[a-z]*)|(a?m(elyik(ek)?|i)?ben?)|(a?mi(kor)?)|(a?hol)|(hogy)|(van(nak)?)|([mk]i(vel|nek))|(mi?[eé]rt)|(r[aá])|(egy)|(mi(t|k(et)?)?)|(meg)|(be)|(az(oka)?t)|(kell(ene)?)|(k[eé]ne)|(szeretn[eé][km])|(k[eé]rn?(([eé][km])|i)?)|(ad[dj]([aá][dl])?)|(nekem)|(van)|(nincs)|(csak)|(k[uü]ld[dj]?[eé]?[dl]?)|(mond[a-z]+)|([ae]bb[ae]n?))\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		if including:
			exclude		= re.compile(r''+including, re.IGNORECASE)
			text		= exclude.sub('',text)
	return trim(remove_punctuation(text))

# based on http://snowball.tartarus.org/algorithms/hungarian/stop.txt 
# prepared by Anna Tordai
def remove_stopwords(text):
	if text:
		stopwords	= ['a', 'ahogy', 'ahol', 'aki', 'akik', 'akkor', 'alatt', 'által', 'altal', 'általában', 'altalaban', 'amely', 'amelyek', 'amelyekben', 'amelyeket', 'amelyet', 'amelynek', 'ami', 'amit', 'amolyan', 'amíg', 'amig', 'amikor', 'át', 'at', 'abban', 'ahhoz', 'annak', 'arra', 'arról', 'arrol', 'az', 'azok', 'azon', 'azt', 'azzal', 'azért', 'azert', 'aztán', 'aztan', 'azután', 'azutan', 'azonban', 'bár', 'bar', 'be', 'belül', 'belul', 'benne', 'cikk', 'cikkek', 'cikkeket', 'csak', 'de', 'e', 'eddig', 'egész', 'egesz', 'egy', 'egyes', 'egyetlen', 'egyéb', 'egyeb', 'egyik', 'egyre', 'ekkor', 'el', 'elég', 'eleg', 'ellen', 'elő', 'elo', 'először', 'eloszor', 'előtt', 'elott', 'első', 'elso', 'én', 'en', 'éppen', 'eppen', 'ebben', 'ehhez', 'emilyen', 'ennek', 'erre', 'ez', 'ezt', 'ezek', 'ezen', 'ezzel', 'ezért', 'ezert', 'és', 'es', 'fel', 'felé', 'fele', 'hanem', 'hiszen', 'hogy', 'hogyan', 'igen', 'így', 'igy', 'illetve', 'ill.', 'ill', 'ilyen', 'ilyenkor', 'ison', 'ismét', 'ismet', 'itt', 'jó', 'jo', 'jól', 'jol', 'jobban', 'kell', 'kellett', 'keresztül', 'keresztul', 'keressünk', 'keressunk', 'ki', 'kívül', 'kivul', 'között', 'kozott', 'közül', 'kozul', 'legalább', 'legalabb', 'lehet', 'lehetett', 'legyen', 'lenne', 'lenni', 'lesz', 'lett', 'maga', 'magát', 'magat', 'majd', 'majd', 'már', 'mar', 'más', 'mas', 'másik', 'masik', 'meg', 'még', 'meg', 'mellett', 'mert', 'mely', 'melyek', 'mi', 'mit', 'míg', 'mig', 'miért', 'miert', 'milyen', 'mikor', 'minden', 'mindent', 'mindenki', 'mindig', 'mint', 'mintha', 'mivel', 'most', 'nagy', 'nagyobb', 'nagyon', 'ne', 'néha', 'neha', 'nekem', 'neki', 'nem', 'néhány', 'nehany', 'nélkül', 'nelkul', 'nincs', 'olyan', 'ott', 'össze', 'ossze', 'ő', 'o', 'ők', 'ok', 'őket', 'oket', 'pedig', 'persze', 'rá', 'ra', 's', 'saját', 'sajat', 'sem', 'semmi', 'sok', 'sokat', 'sokkal', 'számára', 'szamara', 'szemben', 'szerint', 'szinte', 'talán', 'talan', 'tehát', 'tehat', 'teljes', 'tovább', 'tovabb', 'továbbá', 'tovabba', 'több', 'tobb', 'úgy', 'ugy', 'ugyanis', 'új', 'uj', 'újabb', 'ujabb', 'újra', 'ujra', 'után', 'utan', 'utána', 'utana', 'utolsó', 'utolso', 'vagy', 'vagyis', 'valaki', 'valami', 'valamint', 'való', 'valo', 'vagyok', 'van', 'vannak', 'volt', 'voltam', 'voltak', 'voltunk', 'vissza', 'vele', 'viszont', 'volna']
		for stopword in stopwords:
			text	= re.compile(r'\b'+stopword+'\b', re.IGNORECASE).sub('', text)
		return text
	return ''


# a stemmer that's slightly better than guessing
def tippmix_stemmer(text):
	if text:
		word_list	= tokenizer(text)
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
		vh	= vowel_harmony(word)
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
			vow		= is_vowel(word[-2])
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
				vow		= is_vowel(word[-2])
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
				vow		= is_vowel(word[-2])
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
				vow		= is_vowel(word[-2])
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
				vow		= is_vowel(word[-2])
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
				vow		= is_vowel(word[-2])
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

def extract_message(text):
	extraction	= {
		"command"	: None,
		"arguments"	: [],
		"hashtags"	: [],
		"mentions"	: [],
		"urls"		: [],
		"smileys"	: []
	}
	if isinstance(text, str) and trim(text):
		if text[0] == '/':
			commands				= (str(text[1:]).strip()).split(" ")
			extraction['command']	= commands[0]
			if len(commands)>1:
				extraction['arguments']	= commands[1:]			
		extraction['hashtags']	= find_hashtags(text)
		extraction['mentions']	= find_mentions(text)
		extraction['urls']		= find_urls(text)
		extraction['smileys']	= find_smileys(text)
	return extraction
