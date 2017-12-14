# -*- coding: UTF-8 -*-

import re

# function to check if declarations are actually correct
def validate_intent(intents):
	valid_keys	= set(['stem','clean_stem','affix','clean_affix','prefix','clean_prefix','wordclass','with','without','score','clean_score','match_stem','match_at','ignorecase'])
	valid_class = set(['noun','verb','adjective','regex','special'])
	is_regex	= set(['|','(',')','+','*','+','?','\\'])
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
				if any(test in item['stem'] for test in is_regex):
					if 'wordclass' not in item or item['wordclass']!='regex':
						print(intent,'probably has a regex "wordclass" declared otherwise in',item['stem'])
	print('Intent checked.')
	
# spell checker for most common hungarian typos
def spell_checker(text):
	# TODO: actually implement this
	return text