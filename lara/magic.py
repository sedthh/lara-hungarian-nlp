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
	
# generate intents from CSV rows
def row_as_intent(row,data={}):
	if isinstance(row, list):
		if len(row)>2:
			row={
				'stem':			row[0],
				'wordclass':	row[1],
				'intent':		row[2]
			}
		else:
			raise KeyError('Rows provided as lists should at least be 3 long.')
	row['intent']	= row['intent'].strip()
	if 'stem' in row and 'wordclass' in row and 'intent' in row:
		if row['intent']:
			if row['intent'] not in data:
				data[row['intent']]	= []
			if str(row['wordclass']).lower() in ('noun','verb','adjective','special'):
				# check if parenthesis and other special characters add up
				if len(re.findall('\(',row['stem'])) == len(re.findall('\)',row['stem'])):
					intent	= {}
					options	= re.findall('^(\([\w\|]*\))?([\w\s\-\.]+)(\([\w\|]*\))?$',row['stem'])
					if options:				
						if options[0][1]:
							if options[0][0]:
								prefix	= options[0][0].replace('(','').replace(')','').split('|')
								if prefix:
									intent['prefix']	= []
									for item in prefix:
										if item:
											intent['prefix'].append(item)
							if options[0][2]:
								affix	= options[0][2].replace('(','').replace(')','').split('|')
								if affix:
									intent['affix']		= []
									for item in affix:
										if item:
											intent['affix'].append(item)
							intent['stem']	= options[0][1]
							intent['wordclass']	= row['wordclass'].lower()
							data[row['intent']].append(intent)
						else:
							raise ValueError('No stem declared in "'+str(row['stem']+'"'))			
					else:
						raise ValueError('Missing stem declaration in "'+str(row['stem']+'"'))			
				else:
					raise ValueError('Invalid stem declaration in "'+str(row['stem'])+'"')
			else:
				raise ValueError('Accepted values for wordclass are: noun, verb, adjective or special.')
		else:
			raise ValueError('No intent was defined.')
	else:
		raise KeyError('Rows are required to have stem, wordclass and intent columns.')
	return data
	
# spell checker for most common hungarian typos
def spell_checker(text):
	# TODO: actually implement this
	return text