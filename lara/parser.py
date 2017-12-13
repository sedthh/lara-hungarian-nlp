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
		elif item['wordclass'] not in ('noun','verb','adjective','regex','special','emoji'):
			if item['wordclass']=='ADJ':
				item['wordclass']	= 'adjective'
			elif isinstance(item['wordclass'],str) and item['wordclass'].lower() in ('noun','verb'):
				item['wordclass']	= item['wordclass'].lower()
			else:
				item['wordclass']	= 'special'		
		if 'clean_stem' not in item:
			if item['wordclass'] in ('regex','emoji'):
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
		if 'boundary' not in item:
			if item['wordclass']=='emoji':
				item['boundary']	= False
			else:
				item['boundary']	= True
		
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
			item['clean_score']= item['score']
		
		# cache pattern
		if item['wordclass'] in ('regex','emoji'):
			item['pattern']			= r''+item['stem']+item['affix']
			item['clean_pattern']	= r''+item['clean_stem']+item['clean_affix']
		else:
			item['pattern']			= '('+re.escape(item['stem'])+item['affix']+')'
			item['clean_pattern']	= '('+re.escape(item['clean_stem'])+item['clean_affix']+')'
			if item['wordclass'] == 'noun':
				item['pattern']			+= r'{1,2}a?i?n?([aáeéioóöőuúü]?[djknmrst])?([abjhkntv]?[aáeéioóöőuúü]?[lgkntz]?)?([ae][kt])?'
				item['clean_pattern']	+= r'{1,2}a?i?n?([aeiou]?[djknmrst])?([abjhkntv]?[aeiou]?[lgkntz]?)?([ae][kt])?'
			elif item['wordclass'] == 'adjective':
				item['pattern']			+= r'([aeoó]?s)?([aáeé]?b*)([ae]?k)?(([aáeéioóöőuúü]?[dklmnt])?([aáeéioóöőuúü]?[klnt]?)?)'
				item['clean_pattern']	+= r'([aeo]?s)?([ae]?b*)([ae]?k)?(([aeiou]?[dklmnt])?([aeiou]?[klnt]?)?)'
			elif item['wordclass'] == 'verb':
				item['pattern']			+= r'{1,2}(h[ae][st])?([eaá]?s{0,2}d?)?(([jntv]|([eo]?g[ae]t+))?(([aeioöuü]n?[dklmt])|(n[aáeéi]k?)|(sz)|[aái])?(t[aáeéou][dkmt]?(ok)?)?)?((t[ae]t)?(h[ae]t([jnt]?[aáeéou]([dkm]|(t[eéo]k))?)?(tt?)?)|(ni))?'
				item['clean_pattern']	+= r'{1,2}(h[ae][st])?([eaá]?s{0,2}d?)?(([jntv]|([eo]?g[ae]t+))?(([aeiou]n?[dklmt])|(n[aei]k?)|(sz)|[ai])?(t[aeou][dkmt]?(ok)?)?)?((t[ae]t)?(h[ae]t([jnt]?[aeou]([dkm]|(t[eo]k))?)?(tt?)?)|(ni))?'
		item['pattern']			= item['prefix']+item['pattern']	
		item['clean_pattern']	= item['clean_prefix']+item['clean_pattern']
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
	
	def clean(self, text=""):
		if text:
			return self._get_clean_text(text,self.intents)
		else:
			return ""
	
	# Get set of matches from text
	def match_as_set(self, text=""):
		if text:
			matches	= self.match(text)
			return set(list(matches.keys()))
		return set([])
	
	# Get score for intents in text
	def _get_clean_text(self, text, intents):
		text		= lara.nlp.trim(text)
		clean_text	= lara.nlp.strip_accents(lara.nlp.remove_double_letters(text)) #.lower()
		fix_text	= text
		if text:
			for key, value in intents.items():
				for item in self.intents[key]:
					if 'stem' in item:
						fix_text		= self._find_intent(fix_text,item,False,True)
					if 'clean_stem' in item:
						fix_text		= self._find_intent(fix_text,item,True,True)
		return fix_text
			
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
	def _find_intent(self, text, item, is_clean=False, delete=False):
		if text:		
			if is_clean:
				select		= 'clean_'
			else:
				select		= ''	
			if item['boundary']:
				boundary	= r'\b'
			else:
				boundary	= r''
				
			if item['match_at'] == 'regex':
				if item['ignorecase']:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary,re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary).findall(text)
			elif item['match_at'] == 'start':
				if item['ignorecase']:
					matches	= re.compile(r'((^|[,.!?]|(\b[éé]s)|(\bvagy)|(\bhogy))\W?'+item[select+'pattern']+r')'+boundary,re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(r'((^|[,.!?]|(\b[éé]s)|(\bvagy)|(\bhogy))\W?'+item[select+'pattern']+r')'+boundary).findall(text)
			elif item['match_at'] == 'end':
				if item['ignorecase']:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r'((\W*$)|[,.?!]+))',re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r'((\W*$)|[,.?!]+))').findall(text)
			else:
				if item['ignorecase']:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary,re.IGNORECASE).findall(text)
				else:
					matches	= re.compile(boundary+r'('+item[select+'pattern']+r')'+boundary).findall(text)
					
			if matches:
				if delete:
					tmp	= text
					for match in matches:
						tmp	= re.sub(boundary+r'('+re.escape(match[0])+r')'+boundary, '', tmp, flags=re.IGNORECASE)
					return tmp
				else:	
					if not item['match_stem']:
						stem_matches	= re.compile(boundary+r'('+re.escape(item[select+'stem'])+r')'+boundary,re.IGNORECASE).findall(text)
						if stem_matches:
							if len(matches) <= len(stem_matches):
								return (False, 0)
							return (True,(len(matches)-len(stem_matches))*item[select+'score'])
					return (True,len(matches)*item[select+'score'])
		if delete:
			return text
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
	