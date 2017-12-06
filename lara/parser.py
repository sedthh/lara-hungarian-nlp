# -*- coding: UTF-8 -*-

import sys
import re
import json

#if 'lara.nlp' not in sys.modules:
#	import lara.nlp
import lara.nlp

class Intents:
	
	##### CONSTRUCTOR #####
	def __init__(self, new_intents={}, is_raw=False):		
		self.intents	= {}
		if new_intents:
			if is_raw:
				self.raw(new_intents)
			else:
				self.add(new_intents)

	##### DATA MODEL #####
	def __repr__(self):
		return "<Lara Intents Parser instance at {0}>".format(hex(id(self)))
		
	def __str__(self):
		return json.dumps(self.intents)

	def __len__(self):		
		return len(self.intents.keys())
	
	def __eq__(self, other):
		if self.__class__.__name__ == other.__class__.__name__:
			return (self.intents==other.intents)
		elif isinstance(other, bool):
			return (len(self.intents)!=0)==other
		return False
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __add__(self, other):
		if other:
			tmp = Intents(self.intents)
			if self.__class__.__name__ == other.__class__.__name__:
				tmp.add(other.intents)
			elif isinstance(other,dict):
				tmp.add(other)
			return tmp
		return self
	
	##### CLASS FUNCTIONS #####
				
	# Add dict of intents
	def add(self, new_intents={}):
		for key, value in new_intents.items():
			if key not in self.intents:
				self.intents[key]	= []
			for item in new_intents[key]:
				if item not in self.intents[key]:
					item	= self._fix_intent(item)
					if item not in self.intents[key]:
						self.intents[key].append(item)
	
	# Add raw intents without further optimization
	def raw(self, new_intents):
		if new_intents:
			if isinstance(new_intents, str):
				new_intents	= json.loads(new_intents)
			elif new_intents.__class__.__name__=='Intents':
				new_intents	= json.loads(str(new_intents))
			if isinstance(new_intents,dict):
				self.intents	= new_intents.copy()
			else:
				raise ValueError('Unsupported value: %s' % (new_intents))
	
	# Add default values and fill in optional paramteres for a single intent
	def _fix_intent(self, item):
		if 'stem' not in item:
			raise KeyError('Intent declaration missing compulsory "stem" key.')
		if not item['stem'] or not isinstance(item['stem'], str):
			raise ValueError('Invalid value for "stem".')
		
		prefixes		= ("abba","alá","át","be","bele","benn","el","ellen","elő","fel","föl","hátra","hozzá","ide","ki","körül","le","meg","mellé","neki","oda","össze","rá","szét","túl","utána","vissza")
		clean_prefixes	= ("aba","ala","at","be","bele","ben","el","elen","elo","fel","fol","hatra","hoza","ide","ki","korul","le","meg","mele","neki","oda","osze","ra","szet","tul","utana","visza")
		
		if 'wordclass' not in item:
			item['wordclass']		= 'special'
		elif item['wordclass'] not in ('noun','verb','adjective','regex','special'):
			if item['wordclass']=='ADJ':
				item['wordclass']	= 'adjective'
			elif isinstance(item['wordclass'],str) and item['wordclass'].lower() in ('noun','verb'):
				item['wordclass']	= item['wordclass'].lower()
			else:
				item['wordclass']	= 'special'
		if 'clean_stem' not in item:
			if item['wordclass'] == 'regex':
				item['clean_stem']	= item['stem']
				if 'match_at' not in item:
					item['match_at']	= 'regex'
			else:
				item['clean_stem']	= lara.nlp.trim(lara.nlp.strip_accents(lara.nlp.remove_double_letters(item['stem']))) #.lower()
		
		if 'prefix' not in item:
			if item['wordclass']	== 'verb':
				item['prefix']		= r'('+('|'.join(prefixes))+')?'
				item['clean_prefix']= r'('+('|'.join(clean_prefixes))+')?'
			elif item['wordclass']	== 'adjective':
				item['prefix']		= r'(leg(esleg)?)?'
				item['clean_prefix']= r'(leg(esleg)?)?'
			else:
				item['prefix']		= r''
				item['clean_prefix']= r''
		elif not item['prefix']:
			item['prefix']		= r''
			item['clean_prefix']= r''
		else:
			#item['prefix']		=  [re.escape(prefix) for prefix in item['prefix']]
			if 'clean_prefix' not in item:
				if isinstance(item['prefix'],list):
					item['clean_prefix']= r'('+lara.nlp.strip_accents('|'.join(item['prefix']))+')?'
				else:
					item['clean_prefix']= r''+lara.nlp.strip_accents(item['prefix'])
			else:
				if isinstance(item['clean_prefix'],list):
					item['clean_prefix']=  [re.escape(prefix) for prefix in item['clean_prefix']]
					item['clean_prefix']= r'('+('|'.join(item['clean_prefix']))+')?' #prefix?
				else:
					item['clean_prefix']= r''+(item['clean_prefix'])
			if isinstance(item['prefix'],list):
				item['prefix']		= r'('+('|'.join(item['prefix']))+')?'
			else:
				item['prefix']		= r''+(item['prefix'])
		
		if 'affix' not in item or not item['affix']:
			item['affix']		= r''
			item['clean_affix']	= r''
		else:
			#item['affix']		=  [re.escape(affix) for affix in item['affix']]
			if 'clean_affix' not in item:
				if isinstance(item['affix'],list):
					item['clean_affix']	= r'('+lara.nlp.strip_accents('|'.join(item['affix']))+')?'
				else:
					item['clean_affix']	= r''+lara.nlp.strip_accents(item['affix'])
			else:
				if isinstance(item['clean_affix'],list):
					item['clean_affix']	=  [re.escape(affix) for affix in item['clean_affix']]
					item['clean_affix']	= r'('+('|'.join(item['clean_affix']))+')?'
				else:
					item['clean_affix']	= r''+(item['clean_affix'])
			if isinstance(item['affix'],list):
				item['affix']		= r'('+('|'.join(item['affix']))+')?'
			else:
				item['affix']		= r''+(item['affix'])
					
		if 'match_stem' not in item:
			item['match_stem']	= True
		if 'match_at' not in item or item['match_at'] not in ('regex','start','end','any'):
			item['match_at']	= 'any'
		
		if 'ignorecase' not in item:
			item['ignorecase']	= True
		
		if 'with' in item:
			if 'score' not in item:
				item['score']		= 0
			new_items	= []
			for sub_item in item['with']:
				sub_item	= self._fix_intent(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['with']	= new_items[:]
		else:
			item['with']	= []
			if 'score' not in item:
				item['score']		= 1
		if 'without' in item:
			new_items	= []
			for sub_item in item['without']:
				sub_item	= self._fix_intent(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['without']	= new_items[:]
		else:
			item['without']	= []		
		
		if 'clean_score' not in item:
				item['clean_score']	= item['score']
		return item
	
	# Get all matches from text
	def match(self, text=""):
		if text:
			score		= self._get_all_score(text,self.intents)
			final_score	= {}
			for key, value in score.items():
				if value:
					final_score[key]=value
			return final_score
		else:
			return {}
	
	# Get set of matches from text
	def match_as_set(self, text=""):
		if text:
			matches	= self.match(text)
			return set(list(matches.keys()))
		return set([])
	
	# Get score for intents in text
	def _get_all_score(self, text, intents):
		text		= lara.nlp.trim(text)
		clean_text	= lara.nlp.strip_accents(lara.nlp.remove_double_letters(text)) #.lower()
		score		= {}
		if text:
			for key, value in intents.items():
				for item in self.intents[key]:
					found	= False
					if 'stem' in item:
						result		= self._find_intent(text,item)
						found		= found or result[0]
						if key not in score:
							score[key]	= 0
						score[key]	+= result[1]
					if 'clean_stem' in item:
						result		= self._find_intent(clean_text,item,True)
						found		= found or result[0]
						if key not in score:
							score[key]	= 0
						score[key]	+= result[1]
					if found and 'with' in item and len(item['with']):
						for sub_item in item['with']:
							if 'stem' in sub_item:
								if key not in score:
									score[key]	= 0
								found	= self._find_intent(text,sub_item)
								if found[0]:
									score[key]	+=found[1]
							if 'clean_stem' in sub_item:
								if key not in score:
									score[key]	= 0
								found	= self._find_intent(clean_text,sub_item,True)
								if found[0]:
									score[key]	+=found[1]
					if found and 'without' in item and len(item['without']):
						if key in score and score[key]:
							for sub_item in item['without']:
								if 'stem' in sub_item:
									if self._find_intent(text,sub_item)[0]:
										score[key]	= 0
								if 'clean_stem' in sub_item:
									if self._find_intent(clean_text,sub_item,True)[0]:
										score[key]	= 0
		return score
	
	# Find an intent in text
	def _find_intent(self, text, item, is_clean=False):
		if text:		
			select		= ''
			if is_clean:
				select		= 'clean_'
			if item['wordclass'] == 'regex':
				pattern		= r'\b'+item[select+'stem']+item[select+'affix']+r'\b'
			else:
				pattern		= '('+re.escape(item[select+'stem'])+item[select+'affix']+')'
				if item['wordclass'] == 'noun':
					if is_clean:
						pattern	+= r'{1,2}a?i?n?([aeiou]?[djknmrst])?([abjhkntv]?[aeiou]?[lgkntz]?)?([ae][kt])?'
					else:
						pattern	+= r'{1,2}a?i?n?([aáeéioóöőuúü]?[djknmrst])?([abjhkntv]?[aáeéioóöőuúü]?[lgkntz]?)?([ae][kt])?'
				elif item['wordclass'] == 'adjective':
					if is_clean:
						pattern	+= r'([aeo]?s)?([ae]?b*)([ae]?k)?(([aeiou]?[dklmnt])?([aeiou]?[klnt]?)?)'
					else:
						pattern	+= r'([aeoó]?s)?([aáeé]?b*)([ae]?k)?(([aáeéioóöőuúü]?[dklmnt])?([aáeéioóöőuúü]?[klnt]?)?)'
				elif item['wordclass'] == 'verb':
					if is_clean:
						pattern	+= r'{1,2}(h[ae][st])?([eaá]?s{0,2}d?)?(([jntv]|([eo]?g[ae]t+))?(([aeiou]n?[dklmt])|(n[aei]k?)|(sz)|[ai])?(t[aeou][dkmt]?(ok)?)?)?((t[ae]t)?(h[ae]t([jnt]?[aeou]([dkm]|(t[eo]k))?)?(tt?)?)|(ni))?'
					else:
						pattern	+= r'{1,2}(h[ae][st])?([eaá]?s{0,2}d?)?(([jntv]|([eo]?g[ae]t+))?(([aeioöuü]n?[dklmt])|(n[aáeéi]k?)|(sz)|[aái])?(t[aáeéou][dkmt]?(ok)?)?)?((t[ae]t)?(h[ae]t([jnt]?[aáeéou]([dkm]|(t[eéo]k))?)?(tt?)?)|(ni))?'
			
			if item['match_at'] == 'regex':
				if item['ignorecase']:
					matches	= re.compile(r''+item[select+'prefix']+pattern,re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(r''+item[select+'prefix']+pattern).findall(text)
			elif item['match_at'] == 'start':
				if item['ignorecase']:
					matches	= re.compile(r'(^|[,.!?]|(\b[éé]s)|(\bvagy)|(\bhogy))\W?'+item[select+'prefix']+pattern+r'\b',re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(r'(^|[,.!?]|(\b[éé]s)|(\bvagy)|(\bhogy))\W?'+item[select+'prefix']+pattern+r'\b').findall(text)
			elif item['match_at'] == 'end':
				if item['ignorecase']:
					matches	= re.compile(r'\b'+item[select+'prefix']+pattern+r'((\W*$)|[,.?!]+)',re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(r'\b'+item[select+'prefix']+pattern+r'((\W*$)|[,.?!]+)').findall(text)
			else:
				if item['ignorecase']:
					matches	= re.compile(r'\b'+item[select+'prefix']+pattern+r'\b',re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(r'\b'+item[select+'prefix']+pattern+r'\b').findall(text)
			
			if matches:
				if not item['match_stem']:
					stem_matches	= re.compile(r'\b'+re.escape(item[select+'stem'])+r'\b',re.IGNORECASE).findall(text)
					if stem_matches:
						if len(matches) <= len(stem_matches):
							return (False, 0)
						return (True,(len(matches)-len(stem_matches))*item[select+'score'])
				return (True,len(matches)*item[select+'score'])
		return (False,0)
		
	# Get N best matching intents with the highest value
	def match_best(self, text, n=1):
		if text:
			score	= self.match(text)
			if score:
				best_candidates	= sorted(score, key=score.get, reverse=True)
				best_candidates	= best_candidates[:(min(len(best_candidates),n))]
				return {item:score[item] for item in best_candidates}
		return {}
			
##### FUNCTIONS OUTSIDE OF CLASS #####
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
	if 'stem' in row and 'wordclass' in row and 'intent' in row:
		if row['intent']:
			if row['intent'] not in data:
				data[row['intent']]	= []
			if str(row['wordclass']).lower() in ('noun','verb','adjective','special'):
				# check if parenthesis and other special characters add up
				if len(re.findall('\(',row['stem'])) == len(re.findall('\)',row['stem'])):
					intent	= {}
					options	= re.findall('^(\([\w\|]*\))?(\w+)(\([\w\|]*\))?$',row['stem'])
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
	