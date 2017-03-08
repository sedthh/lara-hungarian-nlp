# -*- coding: UTF-8 -*-

import sys
import re
import json

if 'lara.nlp' not in sys.modules:
	import lara.nlp

class Intents:
	
	##### CONSTRUCTOR #####
	def __init__(self,new_intents={}):		
		self.intents	= {}
		if new_intents:
			self.add_intents(new_intents)

	##### DATA MODEL #####
	def __repr__(self):
		return "<Lara Intents Parser instance at {0}>".format(hex(id(self)))
		
	def __str__(self):
		return json.dumps(self.intents)

	def __len__(self):		
		return len(self.intents.keys())
	
	def __eq__(self,other):
		if self.__class__.__name__ == other.__class__.__name__:
			return (self.intents==other.intents)
		elif isinstance(other, bool):
			return (len(self.intents)!=0)==other
		return False
	
	def __ne__(self,other):
		return not self.__eq__(other)
	
	def __add__(self,other):
		if other:
			tmp = Intents(self.intents)
			if self.__class__.__name__ == other.__class__.__name__:
				tmp.add_intents(other.intents)
			elif isinstance(other,dict):
				tmp.add_intents(other)
			return tmp
		return self
	
	##### CLASS FUNCTIONS #####
				
	# Add dict of intents
	def add_intents(self,new_intents={}):
		for key, value in new_intents.items():
			if key not in self.intents:
				self.intents[key]	= []
			for item in new_intents[key]:
				if item not in self.intents[key]:
					item	= self._fix_intent(item)
					if item not in self.intents[key]:
						self.intents[key].append(item)
	
	# Add default values and fill in optional paramteres for a single intent
	def _fix_intent(self,item):
		prefixes		= ("abba","alá","át","be","bele","benn","el","ellen","elő","fel","föl","hátra","hozzá","ide","ki","körül","le","meg","mellé","neki","oda","össze","rá","szét","túl","utána","vissza")
		clean_prefixes	= ("aba","ala","at","be","bele","ben","el","elen","elo","fel","fol","hatra","hoza","ide","ki","korul","le","meg","mele","neki","oda","osze","ra","szet","tul","utana","visza")
		
		if 'wordclass' not in item or item['wordclass'] not in ('noun','verb','adjective','regex','special'):
			item['wordclass']		= 'special'
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
			
		if 'score' not in item:
			item['score']		= 1
		if 'clean_score' not in item:
			item['clean_score']	= item['score']
		
		if 'match_stem' not in item:
			item['match_stem']	= True
		if 'match_at' not in item or item['match_at'] not in ('regex','start','end','any'):
			item['match_at']	= 'any'
		
		if 'ignorecase' not in item:
			item['ignorecase']	= True
		
		if 'with' in item:
			new_items	= []
			for sub_item in item['with']:
				sub_item	= self._fix_intent(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['with']	= new_items[:]
		else:
			item['with']	= []
		if 'without' in item:
			new_items	= []
			for sub_item in item['without']:
				sub_item	= self._fix_intent(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['without']	= new_items[:]
		else:
			item['without']	= []		
		
		return item
	
	# Get all matches from text
	def match_all_intents(self,text=""):
		if len(text):
			score		= self._get_all_score(text,self.intents)
			final_score	= {}
			for key, value in score.items():
				if value:
					final_score[key]=value
			return final_score
		else:
			return {}
	
	# Get score for intents in text
	def _get_all_score(self,text,intents):
		text		= lara.nlp.trim(text)
		clean_text	= lara.nlp.strip_accents(lara.nlp.remove_double_letters(text)) #.lower()
		score		= {}
		if len(text):
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
	def _find_intent(self,text,item,is_clean=False):
		if len(text):		
			select		= ''
			if is_clean:
				select		= 'clean_'
			if item['wordclass'] == 'regex':
				pattern		= r''+item[select+'stem']+item[select+'affix']
			else:
				pattern		= '('+re.escape(item[select+'stem'])+item[select+'affix']+')'
				if item['wordclass'] == 'noun':
					if is_clean:
						pattern	+= r'{1,2}a?i?n?([aeiou]?[djknmrst])?([abjhkntv]?[aeiou][lgkntz]?)?'
					else:
						pattern	+= r'{1,2}a?i?n?([aáeéioóöőuúü]?[djknmrst])?([abjhkntv]?[aáeéioóöőuúü][lgkntz]?)?'
				elif item['wordclass'] == 'adjective':
					if is_clean:
						pattern	+= r'([ae]?b*)(([aeiou]?[dklmnt])?([aeiou]?[knt]?)?)'
					else:
						pattern	+= r'([aáeé]?b*)(([aáeéioóöőuúü]?[dklmnt])?([aáeéioóöőuúü]?[knt]?)?)'
				elif item['wordclass'] == 'verb':
					if is_clean:
						pattern	+= r'(([jntv]|([eo]?g[ae]t+))?(([aeiou]n?[dklmt])|(n[aei]k?)|(sz)|[ai])?(t[aeou][dkmt]?(ok)?)?)?((t[ae]t)?(h[ae]t([jnt]?[aeou]([dkm]|(t[eo]k))?)?(tt?)?)|(ni))?'
					else:
						pattern	+= r'(([jntv]|([eo]?g[ae]t+))?(([aeioöuü]n?[dklmt])|(n[aáeéi]k?)|(sz)|[aái])?(t[aáeéou][dkmt]?(ok)?)?)?((t[ae]t)?(h[ae]t([jnt]?[aáeéou]([dkm]|(t[eéo]k))?)?(tt?)?)|(ni))?'
			
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
							return [False, 0]
						return [True,(len(matches)-len(stem_matches))*item[select+'score']]
				return [True,len(matches)*item[select+'score']]
		return [False,0]
		
	# Get N best matching intents with the highest value
	def match_best_intent(self,text,n=1):
		score	= self.match_all_intents(text)
		if score:
			best_candidates	= sorted(score, key=score.get, reverse=True)
			best_candidates	= best_candidates[:(min(len(best_candidates),n))]
			return {item:score[item] for item in best_candidates}
			
##### FUNCTIONS OUTSIDE OF CLASS #####
def match_intents(fast_intent,text=""):
	if len(text):
		if isinstance(fast_intent,dict):
			fast_intent=Intents(fast_intent)
		if fast_intent.__class__.__name__=='Intents':
			return fast_intent.match_all_intents(text)
	return {}
	
def get_common_intents():
	return {
		"_negative"		: [{"stem":"nem"},{"stem":"ne"},{"stem":"soha"},{"stem":"mégse","affix":["m"]}],
		"_positive"		: [{"stem":"igen"},{"stem":"aha"},{"stem":"ja"},{"stem":"ok","affix":["é","s"]}],
		"_greeting" 	: [{"stem":"hi","match_at":"start"},{"stem":"szia","match_at":"start"},{"stem":"helló","match_at":"start"},{"stem":"szervusz","match_at":"start"},{"stem":"hali","match_at":"start"}],
		"_leaving" 		: [{"stem":"bye","match_at":"end"},{"stem":"szia","match_at":"end"},{"stem":"viszlát"},{"stem":"viszont látásra"},{"stem":"jó éj","affix":["t","szakát"]}],
		"_thanking"		: [{"stem":"kösz","affix":["i","önöm","önjük","önet"]}],
		"_command"		: [{"stem":"keres(s|d)","wordclass":"regex"},{"stem":"mutass(s|d)","wordclass":"regex"},{"stem":"mond(j|d)","wordclass":"regex"},{"stem":"szeretné(k|m)","wordclass":"regex"},{"stem":"akaro(k|m)","wordclass":"regex"}],
		"_question"		: [{"stem":"\?+($|\s\w+)","wordclass":"regex"},{"stem":"([^,][^,\S+]hogy|^hogy)(an)?","wordclass":"regex"},{"stem":"hol"},{"stem":"honnan"},{"stem":"hová"},{"stem":"hány","affix":["an","at","ból"]},{"stem":"mettől"},{"stem":"meddig"},{"stem":"merre"},{"stem":"mennyi","affix":["en","re"]},{"stem":"mi","affix":["t","k","ket","kor","korra","lyen","lyenek","nek","től","kortól","korra","ből","hez","re","vel"]},{"stem":"ki","affix":["t","k","ket","nek","knek","től","ktől","ből","kből","hez","re","kre","vel","kkel"]}],
		"_conditional"	: [{"stem":"volna"},{"stem":"lenne"},{"stem":"\w+h[ae]t\w+","wordclass":"regex"}]
	}

def merge_dicts(self,*dict_args):
	'''
	Given any number of dicts, shallow copy and merge into a new dict, 
	precedence goes to key value pairs in latter dicts.
	via http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
	'''
	result = {}
	for dictionary in dict_args:
		result.update(dictionary)
	return result
