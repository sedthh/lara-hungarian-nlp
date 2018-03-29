# -*- coding: UTF-8 -*-

import pytest
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

def validate_intent(intents):
	valid_keys	= set(['stem','clean_stem','affix','clean_affix','prefix','clean_prefix','wordclass','inc','exc','score','clean_score','match_stem','ignorecase','boundary','max_words'])
	valid_class = set(['noun','verb','adjective','regex','emoji','special'])
	is_regex	= set(['|','(',')','+','*','+','?','\\','[',']','{','}'])
	for intent,declaration in intents.items():
		for item in declaration:
			for key,value in item.items():
				if key not in valid_keys:
					print(intent,'has unknown key:',key)
			if 'wordclass' in item:
				if item['wordclass'] not in valid_class:
					print(intent,'has invalid "wordclass" declared')
			if 'stem' not in item:
				print(intent,'missing "stem" key')
			else:
				if '\b' in item['stem'] and ('boundary' not in item or item['boundary']):
					print(intent,'has bounary set but has \\b declared as regular expression')
				if 'wordclass' in item and item['wordclass']=='regex':
					switch	= False
					last		= ''
					for char in item['stem']:
						if char=='[':
							switch	= True
						elif char==']':
							switch	= False
						elif char in ('á','Á','é','É','í','Í','ü','Ü','ű','Ű','ú','Ú','ö','Ö','ő','Ő','ó','Ó'):
							if not switch:
								print(intent,'has accents declared in regular expression without counterparts:',item['stem'])
								break
						elif char.isalpha() and char==last:
								print(intent,'has double letters in regular expression:',item['stem'])
								break
						if last=='\\':
							last	= last+char
						else:
							last	= char
				if any(test in item['stem'] for test in is_regex):
					if 'wordclass' not in item or item['wordclass']!='regex':
						print(intent,'probably has a regex "wordclass" declared otherwise in',item['stem'])

@pytest.mark.parametrize("entity", [
    "common","commands","counties","dow","smalltalk","cocktail","popculture","emoji","disallow","tone"
])
def test_entities(entity):
	parenthesis_check = eval('parser.Intents(entities.'+entity+'()).match_set("test")')
	eval('validate_intent(entities.'+entity+'())')