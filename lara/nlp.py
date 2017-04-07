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
	
def vowel_ending(word):
	if word:
		return (word[-1].lower() in ('a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű'))
	return False

#TODO: more contexts
def strip_context(text, context="search", including=None):
	if text:
		if context=='search':
			exclude		= re.compile(r'\b((a(z|rra)?)|(azok(ra)?)|(milyen)|(mennyi)|(mikor)|(hol)|(merre)|(hova)|([mk]i(vel|nek))|(mi?[eé]rt)|(r[aá])|(egy)|(mi(t|k(et)?)?)|(meg)|(be)|(nekem)|(hogy(an)?)|((sz[oó])?cikk\w*)|(oldal\w*)|([ií]r\w*)|(kapcsolat(os(an)?|ban))|(sz[oó]l[oó]?)|(keres\w*)|(n[eé]z[zd])|(mutas(s[aá][dl]|[sd]))|(alapj[aá]n)|(mond[dj]?)|(t[oö]ltse?d?)|(hoz([zd]|z[aá][dl]))|(nyis([ds]|s[aá][dl]))|(megnyit\w*)|((el)?olvas\w*)|(szeretn[eé]\w*)|(k[eé]r(ni|l?e[km]))|(megn[eé]z\w*)|(k[oö]z[oö]tt))\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		elif context=='request':
			exclude		= re.compile(r'\b((a(z|rra)?)|(azok(ra)?)|([io]lya[a-z]*)|(am(elyik(ek)?|i)?ben?)|(a?mi(kor)?)|(a?hol)|(hogy)|(van(nak)?)|([mk]i(vel|nek))|(mi?[eé]rt)|(r[aá])|(egy)|(mi(t|k(et)?)?)|(meg)|(be)|(az(oka)?t)|(kell(ene)?)|(k[eé]ne)|(szeretn[eé][km])|(k[eé]rn?(([eé][km])|i)?)|(ad[dj]([aá][dl])?)|(nekem)|(van)|(k[uü]ld[dj]?[eé]?[dl]?))\b', re.IGNORECASE)
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
	
def extract_message(text):
	extraction	= {
		"command"	: None,
		"arguments"	: [],
		"hashtags"	: [],
		"mentions"	: [],
		"urls"		: [],
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
	return extraction
