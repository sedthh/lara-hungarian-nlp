# -*- coding: UTF-8 -*-

import re
import unicodedata


def strip_accents(text):
	if text:
		return str(unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore'), 'utf-8')
	return ''


def trim(text):
	if text:
		return re.sub(r'\s+', ' ', text.strip())
	return ''


def remove_line_breaks(text, replace=''):
	return re.sub(r"\r?\n", replace, text)


def remove_punctuation(text, replace=''):
	return re.sub(r'[^\w\s]', replace, text)


def remove_double_letters(text, replace=''):
	if text:
		return replace.join([text[i] for i in range(len(text) - 1) if text[i + 1] != text[i]] + [text[-1]])
	return ''


def remove_spaces_between_numbers(text, replace=''):
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


def remove_smileys(text, replace=''):
	if text:
		return re.sub(r'(?:[\:\;\=]\-*[DdXxCc\|\[\]\(\)3]+[89]*)|(?:[\(\)D\[\]\|]+\-*[\:\;\=])', replace, text)
	return ''


def vowel_harmony(word, vegyes=True):
	if word:
		mely = re.compile('[aáoóuú]', re.IGNORECASE)
		magas = re.compile('[eéiíöőüű]', re.IGNORECASE)
		mely_m = len(mely.findall(word))
		magas_m = len(magas.findall(word))
		if not magas_m and not mely_m:
			if word[-1].lower() in ('h', 'k', 'q'):
				return 'mely'
			return 'magas'
		if magas_m and mely_m:
			if vegyes:
				return 'vegyes'
			return 'magas'
		if magas_m > mely_m:
			return 'magas'
		return 'mely'
	return 'mely'


def is_vowel(letter):
	if letter:
		return (letter.lower() in ('a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű'))
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


def crop_text(text, limit=100, end='...', reverse=False):
	if text:
		n = 0
		output = ''
		cache = ''
		length = len(text)
		for i in range(length):
			if reverse:
				char = text[length - 1 - i]
			else:
				char = text[i]

			if char.isalnum():
				if reverse:
					cache = char + cache
				else:
					cache = cache + char
			else:
				if len(output) + len(cache) > limit:
					if len(output) < length:
						if output:
							if reverse:
								return end + output[1:]
							else:
								return output[:-1] + end
						return end
					else:
						return output
				else:
					if reverse:
						output = char + cache + output
					else:
						output += cache + char
					cache = ''
			n += 1
			if n > limit:
				cache = ''
				break
		if cache:
			if reverse:
				output = cache + output
			else:
				output += cache
		if len(output) < length:
			if output:
				if reverse:
					return end + output[1:]
				else:
					return output[:-1] + end
			return end
		return output
	return ''


def tokenize(text):
	if text:
		return re.findall('[\w\-_\']+', text)
	return []


def sent_tokenize(text):
	if text:
		sentences = re.findall(
			r'((?:.*?(?:(?:[dm]r|mr?s|kft|btk|ifj|özv|[ICLXV]{1,3})\.|www\.[\w\d]+\.\w{2,3}(?:[\/\\](?:[\w\d]+\??(?:[\w\d]+\=[\w\d]*)*(?:\#[\w\d]+)?)?)?)?.*?){2,}[\.\?\!\n]+?)',
			text + ".", re.IGNORECASE)
		results = []
		one = ""
		for sent in sentences:
			current = sent.strip()
			if current:
				if one:
					current = one + " " + current
					one = ""
					results.append(current)
				elif len(current) == 2 and not one:
					one = current
				else:
					results.append(current)
		if results:
			results[-1] = ''.join(results[-1][:-1])
			if not results[-1]:
				results.pop()
		return results
	return []


def number_of_words(text):
	if text:
		return len(tokenize(text))
	return 0


def number_of_sentences(text):
	if text:
		return len(sent_tokenize(text))
	return 0


def is_gibberish(text=''):
	length = float(len(text))
	if length > 6:
		if re.compile(r'\b(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})',
					  re.IGNORECASE).findall(text):
			return False
		for char in text:
			if char >= '0' and char <= '9':
				return False

		text = text.lower()
		redflags = 0
		# number of different characters
		unique = float(len(list(set(text))))
		if unique < 4 or unique / length < .33:
			redflags += 1
		# vowel ratio
		vowels = 0.0
		for char in text:
			if is_vowel(char):
				vowels += 1.0
		if vowels:
			if length / vowels < .25:
				redflags += 1
		else:
			redflags += 1
		# length of words
		if length / float(number_of_words(text)) > 9:
			redflags += 1
		# 4 consonants next to each other
		consonants = 0
		szy = 0
		for char in text:
			if is_consonant(char):
				if char in ('s', 'z', 'y'):
					szy += 1
				consonants += 1
			else:
				consonants = 0
				szy = 0
			if consonants > 4 and not szy:
				redflags += 1
				break
			elif consonants > 5:
				redflags += 1
				break

		if redflags > 1:
			return True
	return False


# based on http://snowball.tartarus.org/algorithms/hungarian/stop.txt
# prepared by Anna Tordai
def remove_stopwords(text, negation=True):
	if text:
		stopwords = ['a', 'ahogy', 'ahol', 'aki', 'akik', 'akkor', 'alatt', 'által', 'altal', 'általában', 'altalaban',
					 'amely', 'amelyek', 'amelyekben', 'amelyeket', 'amelyet', 'amelynek', 'ami', 'amit', 'amolyan',
					 'amíg', 'amig', 'amikor', 'át', 'at', 'abban', 'ahhoz', 'annak', 'arra', 'arról', 'arrol', 'az',
					 'azok', 'azon', 'azt', 'azzal', 'azért', 'azert', 'aztán', 'aztan', 'azután', 'azutan', 'azonban',
					 'bár', 'bar', 'be', 'belül', 'belul', 'benne', 'cikk', 'cikkek', 'cikkeket', 'csak', 'de', 'e',
					 'eddig', 'egész', 'egesz', 'egy', 'egyes', 'egyetlen', 'egyéb', 'egyeb', 'egyik', 'egyre', 'ekkor',
					 'el', 'elég', 'eleg', 'ellen', 'elő', 'elo', 'először', 'eloszor', 'előtt', 'elott', 'első',
					 'elso', 'én', 'en', 'éppen', 'eppen', 'ebben', 'ehhez', 'emilyen', 'ennek', 'erre', 'ez', 'ezt',
					 'ezek', 'ezen', 'ezzel', 'ezért', 'ezert', 'és', 'es', 'fel', 'felé', 'fele', 'hiszen', 'hogy',
					 'hogyan', 'igen', 'így', 'igy', 'illetve', 'ill.', 'ill', 'ilyen', 'ilyenkor', 'ison', 'ismét',
					 'ismet', 'itt', 'jó', 'jo', 'jól', 'jol', 'jobban', 'kell', 'kellett', 'keresztül', 'keresztul',
					 'keressünk', 'keressunk', 'ki', 'kívül', 'kivul', 'között', 'kozott', 'közül', 'kozul', 'legalább',
					 'legalabb', 'lehet', 'lehetett', 'legyen', 'lenne', 'lenni', 'lesz', 'lett', 'maga', 'magát',
					 'magat', 'majd', 'majd', 'már', 'mar', 'más', 'mas', 'másik', 'masik', 'meg', 'még', 'meg',
					 'mellett', 'mert', 'mely', 'melyek', 'mi', 'mit', 'míg', 'mig', 'miért', 'miert', 'milyen',
					 'mikor', 'minden', 'mindent', 'mindenki', 'mindig', 'mint', 'mintha', 'mivel', 'most', 'nagy',
					 'nagyobb', 'nagyon', 'néha', 'neha', 'nekem', 'neki', 'néhány', 'nehany', 'nélkül', 'nelkul',
					 'nincs', 'olyan', 'ott', 'össze', 'ossze', 'ő', 'o', 'ők', 'ok', 'őket', 'oket', 'pedig', 'persze',
					 'rá', 'ra', 's', 'saját', 'sajat', 'sok', 'sokat', 'sokkal', 'számára', 'szamara', 'szemben',
					 'szerint', 'szinte', 'talán', 'talan', 'tehát', 'tehat', 'teljes', 'tovább', 'tovabb', 'továbbá',
					 'tovabba', 'több', 'tobb', 'úgy', 'ugy', 'ugyanis', 'új', 'uj', 'újabb', 'ujabb', 'újra', 'ujra',
					 'után', 'utan', 'utána', 'utana', 'utolsó', 'utolso', 'vagy', 'vagyis', 'valaki', 'valami',
					 'valamint', 'való', 'valo', 'vagyok', 'van', 'vannak', 'volt', 'voltam', 'voltak', 'voltunk',
					 'vissza', 'vele', 'viszont', 'volna']
		for stopword in stopwords:
			text = re.sub(r'\b' + stopword + r'\b', '', text, flags=re.I)
		if negation:
			nowords = ['ne', 'nem', 'se', 'sem', 'semmi', 'hanem']
			for noword in nowords:
				text = re.sub(r'\b' + noword + r'\b', '', text, flags=re.I)
		return text
	return ''


# get rhythmic structure of a verse line as ['u','-',...]
def metre(text):
	result = []
	if text:
		text = re.compile('\W+').sub('', re.compile('(sz)|(cs)|(zs)|(gy)|(ly)|(ny)|(ty)').sub('x', text.lower()))

		type = 0
		cons = False
		start = False
		for char in text:
			if is_vowel(char):
				if cons and cons != '_' and start:
					result.append('u')
					start = False
				cons = False
				if char in ('a', 'e', 'i', 'o', 'ö', 'u', 'ü'):
					if start:
						result.append('u')
					start = True
				else:
					if start:
						result.append('u')
					result.append('-')
					start = False
			else:
				if start:
					if char == '_':
						start = True
					elif cons:
						result.append('-')
						start = False
						cons = False
				cons = char
		if start:
			result.append('u')
	return result


# match rhythmic structure of a verse line to given list of structure pattern ['u','-',...]
def metre_pattern(match, pattern):
	if len(pattern) == len(match):
		for i in range(len(match)):
			if pattern[i] in ('-', 'u'):
				if match[i] != pattern[i]:
					return False
		return True
	return False


def is_hexameter(pattern):
	if len(pattern) <= 12:
		return False

	ending = pattern[-5:]
	if not metre_pattern(ending, ['-', 'u', 'u', '-', 'x']):
		return False

	beginning = pattern[:-5]
	test = ''
	mora = 0
	for metre in beginning:
		if test:
			if test == '-':
				test += metre
				if test == '--':
					test = ''
					mora += 1
			elif test == '-u':
				if metre == 'u':
					test = ''
					mora += 1
				else:
					return False
			else:
				return False
		else:
			if metre == '-':
				test = '-'
			else:
				return False
	if mora != 4:
		return False
	return True


def is_pentameter(pattern):
	mora_l = 0
	mora_s = 0
	mora_cnt = 0
	test = ''
	for metre in pattern:
		test += metre
		if mora_cnt == 2 or mora_cnt == 5:
			if test == '-':
				test = ''
				mora_s += 1
				mora_cnt += 1
			else:
				return False
		else:
			if test == '--' or test == '-uu':
				test = ''
				mora_l += 1
				mora_cnt += 1
			elif test == '-u-':
				return False
	if mora_l != 4 or mora_s != 2:
		return False
	return True


# number of syllables in a word	
def number_of_syllables(word, rhyme=False):
	szotag = 0
	for char in word:
		if is_vowel(char):
			szotag += 1
	if not szotag and rhyme:
		word = re.compile('(sz)|(cs)|(zs)|(gy)|(ly)|(ny)|(ty)').sub('x', word.lower().strip())
		szotag = len(word)
	return szotag


# generates list of ngrams from list of tokens
def ngram(tokens, n=2):
	if tokens and n > 0:
		if n >= len(tokens):
			return [' '.join(tokens)]
		else:
			grams = [tokens[i:i + n] for i in range(len(tokens) - n + 1)]
			return [' '.join(item) for item in grams]
	return []


# a or az
def az(word):
	word = trim(word)
	if word:
		if vowel_beginning(word):
			return 'az'
		if word[0] == '5':
			return 'az'
		if word[0] == '1':
			number = ''
			for char in word:
				if char.isnumeric():
					number += char
				else:
					if char != ' ':
						break
			if len(number) in (1, 4, 7, 10):
				return 'az'
	return 'a'
