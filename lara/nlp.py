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

def remove_line_breaks(text,replace=''):
	return re.sub(r"\r?\n", replace, text)
	
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
		return re.compile(r'\b(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})', re.IGNORECASE).findall(text)
	return []
	
def find_smileys(text):
	if text:
		return re.compile(r'([:;]-?[Dd\(\)3]+)\b').findall(text)
	return []

def find_dates(text):
	results	= []
	if text:		
		matches	= re.compile(r'\b((\d{2})?((\d{2}[\\\/\.\-]){1,2})(\d{2}\b))([aáeéo]n)?\b', re.IGNORECASE).findall(text)
		for item in matches:
			results.append(item[0])
		matches	= re.compile(r'\b((\d{2}(\d{2})?\W{0,2})?(jan|feb|m[aá]r|[aá]pr|m[aá]j|j[uú][nl]|aug|sz?ep|okt|nov|dec)\w{0,7}(\W{1,2}\d{1,2}))\b', re.IGNORECASE).findall(text)
		for item in matches:
			results.append(item[0])
	return results
	
def find_currencies(text):
	if text:
		return [item[0] for item in re.compile(r'(((\$|€|£|￥)\s?(\d([\s\.,]\d)?)+)|((\d([\s\.,]\d)?)+\s?(\.\-|\$|€|£|￥|huf\b|ft\b|forint\w*|doll[aá]r\w*|eur[oó]\w*)))', re.IGNORECASE).findall(text)]
	return []
	
def find_commands(text):
	if text and text[0] == '/':
		commands				= (trim(str(text[1:]))).split(" ")
		if len(commands)>1:
			return (commands[0],commands[1:])
		else:
			return (commands[0],[])
	return ('',[])

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
		return is_vowel(word[0])
	return False

def consonant_beginning(word):
	if word:
		return is_consonant(word[0])
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
			exclude		= re.compile(r'\b([ae](z([eo]k)?|([eo]k)?r+[ea])?|milyen|mennyi|mikor|hol|merre|hova|[mk]i(vel|nek|t|k(et)?)?|mi?[eé]rt|r[aá]|egy|meg|[bk]e|nekem|hogy(an)?|(sz[oó])?cikk\w*|oldal\w*|[ií]r\w*|kapcsolat(os(an)?|ban)|sz[oó]l[oó]?|keres\w*|n[eé]z[zd]|mutas(s[aá]?[dl]?)|alapj[aá]n|mond[dj]?|t[oö]ltse?d?|hoz([zd]|z[aá][dl])|nyis(s[aá]?[dls])|megnyit\w*|(el)?olvas\w*|szeretn[eé]\w*|k[eé]r(ni|l?e[km])|(meg)?n[eé]z\w*|k[oö]z[oö]?t+|k[oö]s+z(i|[oö]n[oö]m)?|fel|[eé]?s|vala[km]i(lyen|t[oöő]?l?|nek|[kv]el|[eé]rt?)?|olya[nt](okat)?|van|volt|lett|lesz?)\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		elif context=='request':
			exclude		= re.compile(r'\b([ae](z([eo]k)?a?t?|([eo]k)r+[ae])?|a?m?[ieo]ly[ae]\w+|a?mi(kor)?|a?hol|hogy|van(nak)?|[mk]i(vel|nek|[eé]rt|t|k(et)?)?|r[aá]|egy|meg|be|kell(ene)?|k[eé]ne|szeretn[eé][km]|k[eé]rn?([eé][km]|i)?|ad[dj]([aá][dl])?|nekem|van|csak|k[uü]ld[dj]?[eé]?[dl]?|mond\w*|[ae]bb[ae]n?|l[eé]gy([eé]l)?\s?sz[ií](ves)?|l[eé]cci|azt[aá]n|vagy|m[aá]sik(at)?|lesz|legyen|[bl]enne|vala[km]i(lyen|t[oöő]?l?|nek|[kv]el|[eé]rt?)?|sz[uü]ks[eé]g(em)?|ink[aá]bb|akkor|volt|amiben?|keres\w+|[eé]?s|[ae]rr[ae]|is)\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		elif context=='mail':
			exclude		= re.compile(r'\b(szia|szervusz|[uü]dv([oö]zö?l(et(tel|em)?|[oö]m)?)?|(sz[eé]p\s?)?(j[oó]\s?)?(reggelt|napot|est[eé]t)|k[ií]v[aá]nok|nevem|h[ií]vnak|vagy(ok|unk)?|szeret(n[eé][km]|t[uü]n?k|n[eé]nk|tem)|(meg)?k[eé]r(dez(ni)?|n[eéi]m?)|k[eé]rd[eé]s(t|ei[km]?|sel|e[km]+el)?|[eé]rdekl[oöő]d(ni|[oö][km]|n[eé]k)|[eé]rdekel(ne)?|v[aá]r(o[mk]|unk|juk)?|tisztelt|kedves|v[aá]lasz(ol(ni|t|tak)?|uk(at)?|t)?|[ae]z([eé]rt)?|[ae]zz[ae]l|[ae]bb[ae]n|(a)?miatt|abb[oó]l|[io]lyan(kor)?|le(het)?(n+e)?|lesz|tenni|teend[oő](m|nk)?|te(het|gy)(n?[eé]n?k|[uü]nk)|mert|(a)?hogy(an)?|[uü]gyben|kapcsolat(ban|os|osan)|(meg)?tudn[aái][kl]?(nak)?|tan[aá]cs(uk)?(ra|[aáo]t)|k[oö]sz(i|n[oö]m|nj[uü]k|nettel)?|volt|[ae]kkor|ink[aá]bb|[ae]rr[ae]|l[eé]gy(en)|sz[ií]ves(en)?|l[eé]cci|azt[aá]n|vala[km]ik?(lyen|t[oöő]?l?|nek|[kv]el|[eé]rt?)?|valahogy(an)?|sz[uü]ks[eé]g(e[ms?])?|(meg|el)?mond(ja|an[aá]|ani)?|probl[eé]m[aá](m|val)?|teend[oöő](m|nk)?|sajnos|seg[ií]t(s[eé]g([eé]?re)?|en[ei])?|a?mik?([kv]el|ben|t[oöő]l|nek|[eé]rt)|van|[ae]z?|[ae]zt|meg|[ií]gy|mit?|volna|[eé]?s|egy|[io]tt|olya[nt](okat)?|is|lehet(s[eé]ges|[oöő]leg|ne)?|[eé]rt(ek|em|eni|i|ik))\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		if including:
			exclude		= re.compile(r'\b('+including+r')\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		text	= remove_punctuation(text)
		leftover= [r'a',r'az',r'egy',r'es',r'és',r's',r'hogy']
		for twice in range(2):
			for item in leftover:
				text	= re.compile(r'\b'+item+r'\s+'+item+r'\b', re.IGNORECASE).sub(item, text)
	return trim(text)
	
# based on http://snowball.tartarus.org/algorithms/hungarian/stop.txt 
# prepared by Anna Tordai
def remove_stopwords(text,negation=True):
	if text:
		stopwords	= ['a', 'ahogy', 'ahol', 'aki', 'akik', 'akkor', 'alatt', 'által', 'altal', 'általában', 'altalaban', 'amely', 'amelyek', 'amelyekben', 'amelyeket', 'amelyet', 'amelynek', 'ami', 'amit', 'amolyan', 'amíg', 'amig', 'amikor', 'át', 'at', 'abban', 'ahhoz', 'annak', 'arra', 'arról', 'arrol', 'az', 'azok', 'azon', 'azt', 'azzal', 'azért', 'azert', 'aztán', 'aztan', 'azután', 'azutan', 'azonban', 'bár', 'bar', 'be', 'belül', 'belul', 'benne', 'cikk', 'cikkek', 'cikkeket', 'csak', 'de', 'e', 'eddig', 'egész', 'egesz', 'egy', 'egyes', 'egyetlen', 'egyéb', 'egyeb', 'egyik', 'egyre', 'ekkor', 'el', 'elég', 'eleg', 'ellen', 'elő', 'elo', 'először', 'eloszor', 'előtt', 'elott', 'első', 'elso', 'én', 'en', 'éppen', 'eppen', 'ebben', 'ehhez', 'emilyen', 'ennek', 'erre', 'ez', 'ezt', 'ezek', 'ezen', 'ezzel', 'ezért', 'ezert', 'és', 'es', 'fel', 'felé', 'fele', 'hiszen', 'hogy', 'hogyan', 'igen', 'így', 'igy', 'illetve', 'ill.', 'ill', 'ilyen', 'ilyenkor', 'ison', 'ismét', 'ismet', 'itt', 'jó', 'jo', 'jól', 'jol', 'jobban', 'kell', 'kellett', 'keresztül', 'keresztul', 'keressünk', 'keressunk', 'ki', 'kívül', 'kivul', 'között', 'kozott', 'közül', 'kozul', 'legalább', 'legalabb', 'lehet', 'lehetett', 'legyen', 'lenne', 'lenni', 'lesz', 'lett', 'maga', 'magát', 'magat', 'majd', 'majd', 'már', 'mar', 'más', 'mas', 'másik', 'masik', 'meg', 'még', 'meg', 'mellett', 'mert', 'mely', 'melyek', 'mi', 'mit', 'míg', 'mig', 'miért', 'miert', 'milyen', 'mikor', 'minden', 'mindent', 'mindenki', 'mindig', 'mint', 'mintha', 'mivel', 'most', 'nagy', 'nagyobb', 'nagyon', 'néha', 'neha', 'nekem', 'neki', 'néhány', 'nehany', 'nélkül', 'nelkul', 'nincs', 'olyan', 'ott', 'össze', 'ossze', 'ő', 'o', 'ők', 'ok', 'őket', 'oket', 'pedig', 'persze', 'rá', 'ra', 's', 'saját', 'sajat', 'sok', 'sokat', 'sokkal', 'számára', 'szamara', 'szemben', 'szerint', 'szinte', 'talán', 'talan', 'tehát', 'tehat', 'teljes', 'tovább', 'tovabb', 'továbbá', 'tovabba', 'több', 'tobb', 'úgy', 'ugy', 'ugyanis', 'új', 'uj', 'újabb', 'ujabb', 'újra', 'ujra', 'után', 'utan', 'utána', 'utana', 'utolsó', 'utolso', 'vagy', 'vagyis', 'valaki', 'valami', 'valamint', 'való', 'valo', 'vagyok', 'van', 'vannak', 'volt', 'voltam', 'voltak', 'voltunk', 'vissza', 'vele', 'viszont', 'volna']
		for stopword in stopwords:
			text	= re.compile(r'\b'+stopword+'\b', re.IGNORECASE).sub('', text)
		if negation:
			nowords		= ['ne','nem','se','sem','semmi','hanem']
			for noword in nowords:
				text	= re.compile(r'\b'+noword+'\b', re.IGNORECASE).sub('', text)
		return text
	return ''

#get rhythmic structure of a verse line as ['u','-',...]
def metre(text):
	result	= []
	if text:
		text	= re.compile('\W+').sub('',re.compile('(sz)|(cs)|(zs)|(gy)|(ly)|(ny)|(ty)').sub('x',text.lower()))

		type	= 0
		cons	= False
		start	= False
		for char in text:
			if is_vowel(char):
				if cons and cons!='_' and start:
					result.append('u')
					start	= False
				cons	= False
				if char in ('a','e','i','o','ö','u','ü'):
					if start:
						result.append('u')
					start	= True
				else:
					if start:
						result.append('u')
					result.append('-')
					start	= False
			else:
				if start:
					if char=='_':
						start	= True			
					elif cons:
						result.append('-')
						start	= False
						cons	= False
				cons	= char
		if start:
			result.append('u')
	return result

# match rhythmic structure of a verse line to given list of structure pattern ['u','-',...] 
def metre_pattern(match,pattern):
	if len(pattern) == len(match):
		for i in range(len(match)):
			if pattern[i] in ('-','u'):
				if match[i]!=pattern[i]:
					return False
		return True
	return False
	
def is_hexameter(pattern):
	if len(pattern)<=12:
		return False

	ending		= pattern[-5:]
	if not metre_pattern(ending,['-','u','u','-','x']):
		return False

	beginning	= pattern[:-5]
	test		= ''
	mora		= 0
	for metre in beginning:
		if test:
			if test == '-':
				test	+= metre
				if test == '--':
					test	= ''
					mora	+=1
			elif test == '-u':
				if metre == 'u':
					test	= ''
					mora	+= 1
				else:
					return False
			else:
				return False
		else:
			if metre == '-':
				test	= '-'
			else:
				return False
	if mora!=4:
		return False
	return True	

def is_pentameter(pattern):
	mora_l	= 0
	mora_s	= 0
	mora_cnt= 0
	test	= ''
	for metre in pattern:
		test	+= metre
		if mora_cnt == 2 or mora_cnt == 5:
			if test == '-':
				test	= ''
				mora_s	+=1
				mora_cnt+=1
			else:
				return False
		else:
			if test == '--' or test == '-uu':
				test	= ''
				mora_l	+=1
				mora_cnt+=1
			elif test == '-u-':
				return False
	if mora_l != 4 or mora_s != 2:
		return False
	return True
	
# number of syllables in a word	
def number_of_syllables(word,rhyme=False):
	szotag	= 0
	for char in word:
		if is_vowel(char):
			szotag	+= 1
	if not szotag and rhyme:
		word	= re.compile('(sz)|(cs)|(zs)|(gy)|(ly)|(ny)|(ty)').sub('x',word.lower().strip())
		szotag	= len(word)
	return szotag

# True if word has a digit in it	
def hasDigits(text):
	return any(char.isdigit() for char in text)	

# generates list of ngrams from list of tokens
def ngram(tokens,n=2):
	if tokens and n>0:
		if n>=len(tokens):
			return [' '.join(tokens)]
		else:
			grams	= [tokens[i:i+n] for i in range(len(tokens)-n+1)]
			return [' '.join(item) for item in grams]
	return []
