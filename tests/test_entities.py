# -*- coding: UTF-8 -*-

import pytest
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from lara import parser, entities

def validate_intent(intents):
	valid_keys	= set(['stem','clean_stem','affix','clean_affix','prefix','clean_prefix','wordclass','with','without','score','clean_score','match_stem','match_at','ignorecase','boundary','max_words'])
	valid_class = set(['noun','verb','adjective','regex','emoji','special'])
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
				if '\b' in item['stem'] and ('boundary' not in item or item['boundary']):
					print(intent,'has bounary set but has \\b declared as regular expression')
				if any(test in item['stem'] for test in is_regex):
					if 'wordclass' not in item or item['wordclass']!='regex':
						print(intent,'probably has a regex "wordclass" declared otherwise in',item['stem'])

@pytest.mark.parametrize("entity", [
    "common","commands","counties","dow","smalltalk","popculture","emoji","disallow","tone"
])
def test_entities(entity):
	parenthesis_check = eval('parser.Intents(entities.'+entity+'()).match_set("test")')
	eval('validate_intent(entities.'+entity+'())')