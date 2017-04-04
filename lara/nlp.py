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
			exclude		= re.compile(r'\b((a(z|rra)?)|(azok(ra)?)|([io]lyan?(oka?)?t?)|(am(elyik(ek)?|i)?ben?)|(a?mi(kor)?)|(a?hol)|(hogy)|(van(nak)?)|([mk]i(vel|nek))|(mi?[eé]rt)|(r[aá])|(egy)|(mi(t|k(et)?)?)|(meg)|(be)|(az(oka)?t)|(kell(ene)?)|(k[eé]ne)|(szeretn[eé][km])|(k[eé]rn?(([eé][km])|i)?))\b', re.IGNORECASE)
			text		= exclude.sub('',text)
		if including:
			text		= re.compile(r''+including, re.IGNORECASE).sub('',text)
	return trim(remove_punctuation(text))

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
