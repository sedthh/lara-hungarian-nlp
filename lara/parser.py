# -*- coding: UTF-8 -*-

import re, json, hashlib, datetime

import lara.nlp


# Intents Class
class Intents:
	# STATIC REGULAR EXPRESSIONS
	prefixes = r'(?:(?i)' + ('|'.join(
		["abba", "alá", "át", "be", "bele", "benn", "el", "ellen", "elő", "fel", "föl", "hátra", "hozzá", "ide", "ki",
		 "körül", "le", "meg", "mellé", "neki", "oda", "össze", "rá", "szét", "túl", "utána", "vissza"])) + ')?'
	typo_prefixes = r'(?:(?i)' + ('|'.join(
		["aba", "ala", "at", "be", "bele", "ble", "ben", "el", "elen", "eln", "elo", "fel", "fol", "hatra", "htara",
		 "harta", "hoza", "hzoa", "ide", "ki", "korul", "kroul", "kourl", "le", "meg", "mele", "mle", "neki", "nkei",
		 "oda", "osze", "ozse", "ra", "szet", "sezt", "tul", "utana", "uatna", "utna", "visza", "vsiza",
		 "vizsa"])) + ')?'
	pattern_noun = r'(?i)a?i?n?(?:[aáeéioóöőuúü]?[djknmrst])?(?:[abjhkntv]?[aáeéioóöőuúü]?[lgkntz]?)?(?:[ae][kt])?'
	typo_pattern_noun = r'(?i)a?i?n?(?:[aeiou]?[djknmrst])?(?:[abjhkntv]?[aeiou]?[lgkntz]?)?(?:[ae][kt])?u?'
	pattern_adj = r'(?i)(?:[aeoóöő]?s)?(?:[aáeéoó]?b{0,2})(?:[ae]?[nk])?(?:j?[ae])?(?:(?:[aáeéioóöőuúü]?[dklmnt])?(?:[aáeéioóöőuúü]?[klnt]?)?)(?:s[aáeé]g[ae]?(?:i\w*)?)?'
	typo_pattern_adj = r'(?i)(?:[aeo]?s)?(?:[aeo]?b?)(?:[ae]?[nk])?(?:j?[ae])?(?:(?:[aeiou]?[dklmnt])?(?:[aeiou]?[klnt]?)?)(?:s[ae]g[ae]?(?:i\w*)?)?u?'
	pattern_verb = r'(?i)(?:h[ae][st]+e?)?(?:j?[ae])?(?:[eaá]?s{0,2}e?d?|[aáeéo]tt)?(?:(?:[jntv]|[eo]?g[ae]t+)?(?:[aeioöuü]n?[dklmt]|n[aáeéi]k?|sz|[aái])?(?:t[aáeéou][dkmt]?(?:ok)?)?)?(?:(?:t[ae]t)?(?:h[ae]t(?:[jnt]?[aáeéou](?:[dkm]|t[eéo]k)?)?t*)|[aáeé]?z?ni)?'
	typo_pattern_verb = r'(?i)(?:h[ae][st]e?)?(?:j?[ae])?(?:[eaá]?s?e?d?|[aeo]t)?(?:(?:[jntv]|[eo]?g[ae]t)?(?:[aeiou]n?[dklmt]|n[aei]k?|sz|[ai])?(?:t[aeou][dkmt]?(?:ok)?)?)?(?:(?:t[ae]t)?(?:h[ae]t(?:[jnt]?[aeou](?:[dkm]|t[eo]k)?)?t?)|[ae]?z?ni)?u?'

	##### CONSTRUCTOR #####
	def __init__(self, new_intents={}, is_raw=False):
		self.intents = {}
		if not isinstance(new_intents, str) and not isinstance(new_intents,
															   dict) and self.__class__.__name__ == new_intents.__class__.__name__:
			raise ValueError('Unsupported value for Intents.')
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
			return (self.intents == other.intents)
		elif isinstance(other, bool):
			return (len(self.intents) != 0) == other
		return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __add__(self, other):
		if other:
			tmp = Intents(self.intents)
			if self.__class__.__name__ == other.__class__.__name__:
				tmp.add(other.intents)
			elif isinstance(other, dict):
				tmp.add(other)
			return tmp
		return self

	##### CLASS FUNCTIONS #####

	# Add dict of intents
	def add(self, new_intents={}):
		for key, value in new_intents.items():
			if key not in self.intents:
				self.intents[key] = []
			for item in new_intents[key]:
				if item not in self.intents[key]:
					item = self._generate(item)
					if item not in self.intents[key]:
						self.intents[key].append(item)

	# Add (previously cached) raw intents without further optimization
	def raw(self, new_intents):
		if new_intents:
			if isinstance(new_intents, str):
				new_intents = json.loads(new_intents)
			elif new_intents.__class__.__name__ == 'Intents':
				new_intents = json.loads(str(new_intents))
			if isinstance(new_intents, dict):
				self.intents = new_intents.copy()
			else:
				raise ValueError('Unsupported value: %s' % (new_intents))

	# Add default values and fill in optional parameters for a single intent
	def _generate(self, item):
		if 'stem' not in item:
			raise KeyError('Intent declaration missing compulsory "stem" key.')
		if not item['stem'] or not isinstance(item['stem'], str):
			raise ValueError('Invalid value for "stem".')

		if 'wordclass' not in item:
			item['wordclass'] = 'special'
		elif item['wordclass'] not in ('special', 'noun', 'verb', 'adjective', 'regex', 'emoji'):
			if item['wordclass'] == 'ADJ':
				item['wordclass'] = 'adjective'
			elif isinstance(item['wordclass'], str) and item['wordclass'].lower() in ('noun', 'verb'):
				item['wordclass'] = item['wordclass'].lower()
			else:
				item['wordclass'] = 'special'
		if item['wordclass'] == 'regex':
			item['stem'] = item['stem'].replace("\b", "\\b")
			if 'typo_stem' in item:
				item['typo_stem'] = item['typo_stem'].replace("\b", "\\b")

		if 'typo_stem' not in item:
			if item['wordclass'] in ('regex', 'emoji'):
				item['typo_stem'] = item['stem']
			else:
				item['typo_stem'] = lara.nlp.trim(lara.nlp.strip_accents(lara.nlp.remove_double_letters(item['stem'])))
				if not item['typo_stem']:
					item['typo_stem'] = lara.nlp.trim(lara.nlp.remove_double_letters(item['stem']))

		if 'prefix' not in item:
			if item['wordclass'] == 'verb':
				item['prefix'] = r'(?i)' + Intents.prefixes
				item['typo_prefix'] = r'(?i)' + Intents.typo_prefixes
			elif item['wordclass'] == 'adjective':
				item['prefix'] = r'(?i)(?:leg(?:esleg)?)?'
				item['typo_prefix'] = r'(?i)(?:leg(?:esleg)?)?'
			else:
				item['prefix'] = r''
				item['typo_prefix'] = r''
		elif not item['prefix']:
			item['prefix'] = r''
			item['typo_prefix'] = r''
		else:
			if 'typo_prefix' not in item:
				if isinstance(item['prefix'], list):
					typo_prefix = ['(?:' + self._scramble(
						lara.nlp.trim(lara.nlp.strip_accents(lara.nlp.remove_double_letters(elem))),
						(item['wordclass'] == 'adjective')) + ')' for elem in item['prefix']]
					item['typo_prefix'] = r'(?:' + ('|'.join(typo_prefix)) + r')?\s?'
				else:
					item['typo_prefix'] = r'' + lara.nlp.trim(
						lara.nlp.strip_accents(lara.nlp.remove_double_letters(item['prefix'])))
			else:
				if isinstance(item['typo_prefix'], list):
					item['typo_prefix'] = [re.escape(prefix) for prefix in item['typo_prefix']]
					item['typo_prefix'] = r'(?:' + ('|'.join(item['typo_prefix'])) + ')?\s?'
				else:
					item['typo_prefix'] = r'' + (item['typo_prefix'])
			if isinstance(item['prefix'], list):
				item['prefix'] = r'(?:' + ('|'.join(item['prefix'])) + ')?'
			else:
				item['prefix'] = r'' + (item['prefix'])

		if 'affix' not in item or not item['affix']:
			item['affix'] = r''
			item['typo_affix'] = r''
		else:
			if 'typo_affix' not in item:
				if isinstance(item['affix'], list):
					typo_affix = ['(?:' + self._scramble(
						lara.nlp.trim(lara.nlp.strip_accents(lara.nlp.remove_double_letters(elem))),
						(item['wordclass'] == 'adjective')) + ')' for elem in item['affix']]
					item['typo_affix'] = r'\s?(?:' + ('|'.join(typo_affix)) + r')?'
				else:
					item['typo_affix'] = r'' + lara.nlp.strip_accents(item['affix'])
			else:
				if isinstance(item['typo_affix'], list):
					item['typo_affix'] = [re.escape(affix) for affix in item['typo_affix']]
					item['typo_affix'] = r'\s?(?:' + ('|'.join(item['typo_affix'])) + ')?'
				else:
					item['typo_affix'] = r'' + (item['typo_affix'])
			if isinstance(item['affix'], list):
				item['affix'] = r'(?:' + ('|'.join([affix + '{1,2}' for affix in item['affix']])) + ')?'
			else:
				item['affix'] = r'' + (item['affix'])

		if 'match_stem' not in item:
			item['match_stem'] = True
		if 'ignorecase' not in item:
			item['ignorecase'] = True
		if 'boundary' not in item:
			if item['wordclass'] == 'emoji':
				item['boundary'] = False
			else:
				item['boundary'] = True
		if 'max_words' not in item or item['max_words'] < 0:
			item['max_words'] = 0

		if 'inc' in item:
			if 'score' not in item:
				item['score'] = 0
			new_items = []
			for sub_item in item['inc']:
				sub_item = self._generate(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['inc'] = new_items[:]
		else:
			item['inc'] = []
			if 'score' not in item:
				item['score'] = 1
		if 'exc' in item:
			new_items = []
			for sub_item in item['exc']:
				sub_item = self._generate(sub_item)
				if sub_item not in new_items:
					new_items.append(sub_item)
			item['exc'] = new_items[:]
		else:
			item['exc'] = []

		if 'typo_score' not in item:
			item['typo_score'] = item['score']

		if item['score'] < 0:
			raise ValueError('Value of "score" can not be less than 0')
		if item['typo_score'] < 0:
			raise ValueError('Value of "typo_score" can not be less than 0')

		# cache pattern
		if item['wordclass'] in ('regex', 'emoji'):
			item['pattern'] = r'' + item['stem'] + item['affix']
			item['typo_pattern'] = r'' + item['typo_stem'] + item['typo_affix']
		else:
			item['pattern'] = r'(?:' + re.escape(item['stem']) + r'{1,2}' + item['affix'] + r')'
			scramble = self._scramble(item['typo_stem'], (item['wordclass'] == 'adjective'))
			item['typo_pattern'] = r'(?:' + scramble + item['typo_affix'] + ')'
			if not item['ignorecase']:
				item['pattern'] = r'(?s)' + item['pattern']
				item['typo_pattern'] = r'(?s)' + item['typo_pattern']

			if item['wordclass'] == 'noun':
				item['pattern'] += Intents.pattern_noun
				item['typo_pattern'] += Intents.typo_pattern_noun
			elif item['wordclass'] == 'adjective':
				item['pattern'] += Intents.pattern_adj
				item['typo_pattern'] += Intents.typo_pattern_adj
			elif item['wordclass'] == 'verb':
				item['pattern'] += Intents.pattern_verb
				item['typo_pattern'] += Intents.typo_pattern_verb

		item['pattern'] = item['prefix'] + item['pattern']
		item['typo_pattern'] = item['typo_prefix'] + item['typo_pattern']

		return item

	# generate scrambled keywords
	def _scramble(self, text, is_adjective=False):
		if len(text) > 3:
			typo = [text[1:-1]]
			remove_one = bool(len(text) > 5)
			for i in range(len(text) - 3):
				typo.append(re.escape(text[1:i + 1] + text[i + 2] + text[i + 1] + text[i + 3:-1]))
				if remove_one:
					typo.append(re.escape(text[1:i + 1] + text[i + 2] + text[i + 3:-1]))
			if remove_one:
				typo.append(re.escape(text[1:-2]))
			is_consonant = lara.nlp.is_consonant(text[-1])
			text = re.escape(text[0]) + '(?:' + ('|'.join(typo)) + ')(?:' + re.escape(text[-1])
			text = '[\s\-]?'.join(text.split('\ '))
			if is_adjective and is_consonant:
				text += '|[bB])'
			else:
				text += ')'
		else:
			text = re.escape(text)
			text = '[\s\-]?'.join(text.split('\ '))
		return text

	# Get all matches from text
	def match(self, text="", zeros=False):
		if text:
			score = self._get_score(text)
			final_score = {}
			for key, value in score.items():
				if value or zeros:
					final_score[key] = value
			return final_score
		else:
			return {}

	# Get set of matches from text
	def match_set(self, text=""):
		if text:
			score = self._get_score(text, False)
			final_score = {}
			for key, value in score.items():
				if value:
					final_score[key] = value
			return set(list(final_score.keys()))
		else:
			return set()

	# Returns dictionary with N best matching intents with the highest value
	def match_best(self, text, n=1):
		if text:
			score = self.match(text)
			if score:
				best_candidates = sorted(score, key=score.get, reverse=True)
				best_candidates = best_candidates[:(min(len(best_candidates), n))]
				return {item: score[item] for item in best_candidates}
		return {}

	# Get best match based on preference hierarchy
	def match_order(self, text, preference=[], reverse=False):
		if text:
			score = self.match(text)
			if score:
				if reverse:
					if max(score, key=score.get) not in preference:
						return max(score, key=score.get)
					for item in score:
						if item not in preference:
							return item
					preference.reverse()
				for item in preference:
					if item in score:
						return item
				return max(score, key=score.get)
		return ''

	# Remove matches from text
	def clean(self, text="", deep=False):
		if text:
			return self._get_clean_text(text, deep)
		else:
			return ""

	# Returns text without the inflected forms of matched intents
	def _get_clean_text(self, text, deep):
		text = lara.nlp.trim(text)
		typo_text = lara.nlp.strip_accents(lara.nlp.remove_double_letters(text))
		c_text = text
		c_typo_text = typo_text
		if text:
			for key, value in self.intents.items():
				ignore = False
				allow = -1
				for item in self.intents[key]:
					if 'exc' in item and item['exc']:
						for exc in item['exc']:
							if self._match_pattern(text, exc)[0]:  # stem
								ignore = True
							elif self._match_pattern(typo_text, exc, True)[0]:  # typo_stem
								ignore = True
					if 'inc' in item and item['inc']:
						if allow == -1:
							allow = 0
						for inc in item['inc']:
							if self._match_pattern(text, inc)[0]:  # stem
								allow = 1
							elif self._match_pattern(typo_text, inc, True)[0]:  # typo_stem
								allow = 1
					if not ignore and allow in (-1, 1):
						max_words = _re.words(text)
						if item['max_words'] <= max_words:
							c_text = self._match_pattern(c_text, item, False, True, deep)  # stem
							c_typo_text = self._match_pattern(c_typo_text, item, True, True, deep)  # typo_stem
			# attempt to merge results
			c_text = lara.nlp.trim(c_text).split()
			c_typo_text = lara.nlp.trim(c_typo_text).split()
			fix_text = []
			last = 0
			for word in c_text:
				x_word = lara.nlp.strip_accents(lara.nlp.remove_double_letters(word))
				for i in range(last, len(c_typo_text)):
					if x_word == c_typo_text[i]:
						fix_text.append(word)
						last = i
						break
			return ' '.join(fix_text)
		return text

	# Get score for intents in text
	def _get_score(self, text, greedy=True):
		text = lara.nlp.trim(text)
		score = {}
		if text:
			typo_text = lara.nlp.trim(lara.nlp.strip_accents(lara.nlp.remove_double_letters(text.replace(',', ' '))))
			for key, value in self.intents.items():
				for item in self.intents[key]:
					found = False

					result = self._match_pattern(text, item)
					found = found or result[0]
					if key not in score:
						score[key] = 0
					score[key] += result[1]
					result = self._match_pattern(typo_text, item, True)
					found = found or result[0]
					if key not in score:
						score[key] = 0
					score[key] += result[1]

					if found and item['inc']:
						for sub_item in item['inc']:
							if key not in score:
								score[key] = 0
							found = self._match_pattern(text, sub_item)
							if found[0]:
								score[key] += found[1]
							found = self._match_pattern(typo_text, sub_item, True)
							if found[0]:
								score[key] += found[1]

					if found and item['exc']:
						if key in score and score[key]:
							for sub_item in item['exc']:
								if self._match_pattern(text, sub_item)[0]:
									score[key] = 0
								elif self._match_pattern(typo_text, sub_item, True)[0]:
									score[key] = 0

					if not greedy and key in score and score[key] > 0:
						break
		return score

	# Find an intent in text
	def _match_pattern(self, text, item, is_clean=False, delete=False, deep=False):
		if text:
			if not delete and item['max_words']:
				if _re.words(text) > item['max_words']:
					return (False, 0)

			if is_clean:
				select = 'typo_'
			else:
				select = ''
			if item['boundary']:
				boundary = r'\b'
			else:
				boundary = r''

			if item['ignorecase']:
				matches = _re.findall(boundary + r'(' + item[select + 'pattern'] + r')' + boundary, re.IGNORECASE, text)
			else:
				matches = _re.findall(boundary + r'(' + item[select + 'pattern'] + r')' + boundary, None, text)

			if matches:
				if delete:
					tmp = text
					for match in matches:
						if not isinstance(match, str):
							match = match[0]
						if item['match_stem'] or (
								item['ignorecase'] and match.lower() != item[select + 'stem'].lower()) or (
								match.lower() != item[select + 'stem']):
							tmp = _re.sub(boundary + r'(' + re.escape(match) + r')' + boundary, re.IGNORECASE, '', tmp)
					if deep and 'inc' in item:
						for inc in item['inc']:
							tmp = self._match_pattern(tmp, inc, is_clean, delete, deep)
					return tmp
				else:
					if not item['match_stem']:
						if item['ignorecase']:
							stem_matches = _re.findall(
								boundary + r'(' + re.escape(item[select + 'stem']) + r')' + boundary, re.IGNORECASE,
								text)
						else:
							stem_matches = _re.findall(
								boundary + r'(' + re.escape(item[select + 'stem']) + r')' + boundary, None, text)
						if stem_matches:
							if len(matches) <= len(stem_matches):
								return (False, 0)
							return (True, (len(matches) - len(stem_matches)) * item[select + 'score'])
					return (True, len(matches) * item[select + 'score'])
		if delete:
			return text
		return (False, 0)


# Extract Class
class Extract:

	##### CONSTRUCTOR #####
	def __init__(self, text=''):
		if not isinstance(text, str):
			raise ValueError('Constructor only accepts strings.')
		elif text:
			self.text = text
			self.ntext = self._convert_numbers(self.text)
			self._text_ = ' ' + self.text + ' '  # some complex regular expressions were easier to write for padded text
			self._ntext_ = ' ' + self.ntext + ' '  # some complex regular expressions were easier to write for padded text

	##### DATA MODEL #####
	def __repr__(self):
		return "<Lara Extract Parser instance at {0}>".format(hex(id(self)))

	def __str__(self):
		return self.text

	def __len__(self):
		return len(self.text)

	def __eq__(self, other):
		if self.__class__.__name__ == other.__class__.__name__:
			return (self.text == other.text)
		elif isinstance(other, bool):
			return (len(self.text) != 0) == other
		elif isinstance(other, str):
			return self.text == other
		return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def __add__(self, other):
		if other:
			if self.__class__.__name__ == other.__class__.__name__:
				self.text += other.text
			elif isinstance(other, str):
				self.text += other
			self._text_ = ' ' + self.text + ' '
			self.ntext = self._convert_numbers(self.text)
			self._ntext_ = ' ' + self.ntext + ' '
			return self
		return self

	##### CLASS FUNCTIONS #####

	# extract list #hashtags from text
	def hashtags(self, normalize=True):
		if self.text:
			matches = _re.findall(r'#([\w\d]+(?:[\w\d_\-\']+[\w\d]+)+)\b', None, self.text)
			if normalize:
				return ['#{0}'.format(hashtag.lower()) for hashtag in matches]
			else:
				return ['#{0}'.format(hashtag) for hashtag in matches]
		return []

	# extract list of @hashtags from text
	def mentions(self):
		if self.text:
			return _re.findall(r'(?<![\w\d\_])(\@[\w\d_]+(?:[\w\d_\-\'\.]+[\w\d_]+)+)\b', None, self._text_)
		return []

	# extract list of http://urls/ from text	
	def urls(self):
		if self.text:
			return _re.findall(
				r'\b((?:https?\:[\/\\]{2}(?:w{3}\.)?|(?:w{3}\.))(?:[\w\d_\-]+\.\w{2,})(?:[\/\\](?:[\w\d\-_]+[\/\\]?)*)?(?:\?[^\s]*)?(?:\#[^\s]+)?)',
				re.IGNORECASE, self.text)
		return []

	# extract list of smileys :) from text
	def smileys(self):
		if self.text:
			return _re.findall(r'(?:[\:\;\=]\-*[DdXxCc\|\[\]\(\)3]+[89]*)|(?:[\(\)D\[\]\|]+\-*[\:\;\=])', None,
							   self.text)
		return []

	# extract digits with n places
	def digits(self, n=0, normalize=True, convert=True):
		results = []
		if self.text:
			matches = _re.findall(r'((?:\d[\-\.\,\s]?)+)', re.IGNORECASE, self.ntext if convert else self.text)
			for item in matches:
				original = item
				item = lara.nlp.trim(''.join(e for e in item if e.isdigit()))
				if n <= 0 or len(item) == n:
					if normalize:
						results.append(item)
					else:
						results.append(original.strip())
		return results

	# extract (decimal) numbers
	def numbers(self, decimals=True, convert=True):
		if self.text:
			if decimals:
				matches = _re.findall(
					r'(?<!\d)(?<!\-)(?<!\:)((?:\-\s?)?(?:(?:\d\s?)+(?:[\.\,]\d+[^\.\,])?|(?:[\.\,]\d+[^\.\,\:]))[\-\:]?)',
					re.IGNORECASE, self._ntext_ if convert else self._text_)
				okay = []
				for item in matches:
					if item[-1] not in ('-', ':'):
						item = item.replace(',', '.')
						if not item[-1].isnumeric():
							item = item[:-1]
						if item[0] == '-':
							if item[1] == '.':
								item = '-0' + item[1:]
						elif not item[0].isnumeric():
							item = item[1:]
						item = ''.join([char for char in item if char != ' '])
						try:
							correct = float(item)
							okay.append(correct)
						except:
							pass
				return okay
			else:
				matches = _re.findall(r'(?<!\d\-)(?<![\.\,\d])(\-?(?:\d\s?)+(?![\.\,]\d))[^\d\-\:]+', re.IGNORECASE,
									  self._ntext_ if convert else self._text_)
				okay = [item for item in matches if item and item[-1] not in ('-', ':')]
				return [int(''.join(number.strip().split())) for number in okay]
		return []

	# extract percentages
	def percentages(self, normalize=True):
		if self.text:
			if normalize:
				matches = _re.findall(r'((?:\d+(?:[\,\.]\d+)?|[\,\.]\d+))\s?(?:\%|sz[aá]zal[eé]k)', re.IGNORECASE,
									  self.text)
				results = []
				for item in matches:
					item = item.replace(',', '.')
					if item.startswith('.'):
						item = '0' + item
					if '.' in item:
						places = len(item.split('.')[1]) + 2
					else:
						places = 2
					item = str("{:." + str(places) + "f}").format(float(item) / 100.00)
					results.append(float(item))
				return results
			else:
				return _re.findall(r'((?:\d+(?:[\,\.]\d+)?|[\,\.]\d+)\s?(?:\%|sz[aá]zal[eé]k))', re.IGNORECASE,
								   self.text)
		return []

	# extract phone numbers
	def phone_numbers(self, normalize=True, convert=True):
		results = []
		if self.text:
			matches = _re.findall(
				r'((?:\(?(?:\+36|0036|06)[\s\-\\\/]?)?\(?\d{1,2}\)?[\s\-\\\/]?\d(?:\d[\s\-\\\/]?){5}\d)', re.IGNORECASE,
				self.ntext if convert else self.text)
			if not normalize:
				return matches
			for item in matches:
				item = lara.nlp.trim(''.join(e for e in item if e.isdigit()))
				if item.startswith('36') or item.startswith('06'):
					item = item[2:]
				elif item.startswith('0036'):
					item = item[4:]
				if len(item) == 8:
					item = item[0] + ' ' + item[1:]
				else:
					item = item[0:2] + ' ' + item[2:]
				results.append('+36 ' + item)
		return results

	# extract list of common Hungarian date formats from text without further processing them
	def dates(self, normalize=True, convert=True, current=False):
		results = []
		if self.text:
			if current:
				now = datetime.datetime.strptime(current, "%Y-%m-%d")
			else:
				now = datetime.datetime.now()
			matches = _re.findall(
				r'((\d{2})?(\d{2}([\\\/\.\-]\s?|\s))([eé]v\s?)?(\d{1,2}([\\\/\.\-]\s?|\s)(h[oó](nap)?\s?)?)?(\d{1,2}))\W*([aáeéio][ikn]|nap)?\b',
				re.IGNORECASE, self.text)
			for item in matches:
				match = re.sub('([eé]v|h[oó]|nap)', '', item[0])
				parts = list(filter(None, re.split(r'\W', match + '-')))
				if len(parts) == 3:
					if int(parts[1]) <= 12:
						if normalize:
							if len(parts[0]) == 4:
								results.append(parts[0] + '-' + parts[1].zfill(2) + '-' + parts[2].zfill(2))
							else:
								results.append('20' + parts[0] + '-' + parts[1].zfill(2) + '-' + parts[2].zfill(2))
						else:
							results.append(item[0])
				elif len(parts) == 2:
					if normalize:
						if len(parts[0]) == 4:
							results.append(parts[0] + '-' + parts[1].zfill(2) + '-??')
						elif int(parts[0]) > 12:
							results.append('20' + parts[0] + '-' + parts[1].zfill(2) + '-??')
						else:
							results.append(str(now.year) + '-' + parts[0].zfill(2) + '-' + parts[1].zfill(2))
					else:
						results.append(item[0])
			matches = _re.findall(
				r'\b((\d{2}(\d{2})?\W{1,2})?((jan|feb|m[aá]r|[aá]pr|m[aá]j|j[uú][nl]|aug|sz?ep|okt|nov|dec)\w{0,10}\W{1,2}|[ivx]{1,4}\W{0,2})(h[aoó][nv]?\w{0,7}\W{1,2})?(\d{1,2})?\W?\w*)\b',
				re.IGNORECASE, self.ntext if convert else self.text)
			for item in matches:
				match = item[0].lower()
				year = ''
				day = ''
				switch = False
				for char in match:
					if switch:
						if char.isdigit():
							day += char
					else:
						if char.isdigit():
							year += char
						else:
							switch = True
				if not year and not day:
					continue
				if not year:
					year = str(now.year)
				elif len(year) == 2:
					year = '20' + year
				if not day:
					day = '??'
				elif len(day) == 1:
					day = '0' + day
				month = ''
				if 'jan' in match:
					month = '01'
				elif 'feb' in match:
					month = '02'
				elif 'mar' in match or 'már' in match:
					month = '03'
				elif 'apr' in match or 'ápr' in match:
					month = '04'
				elif 'maj' in match or 'máj' in match:
					month = '05'
				elif 'jun' in match or 'jún' in match:
					month = '06'
				elif 'jul' in match or 'júl' in match:
					month = '07'
				elif 'aug' in match:
					month = '08'
				elif 'sep' in match or 'szep' in match:
					month = '09'
				elif 'okt' in match:
					month = '10'
				elif 'nov' in match:
					month = '11'
				elif 'dec' in match:
					month = '12'
				else:
					roman = ''
					for char in match:
						if char in ('i', 'v', 'x'):
							roman += char
						elif roman and char.isnumeric():
							break
						elif roman and char.isalpha():
							roman = ''
							break
					if not roman:
						continue
					if 'v' in roman:
						if roman.startswith('v'):
							month = str(4 + len(roman)).zfill(2)
						else:
							month = str(6 - len(roman)).zfill(2)
					elif 'x' in roman:
						if roman.startswith('x'):
							month = str(9 + len(roman)).zfill(2)
						else:
							month = str(11 - len(roman)).zfill(2)
					else:
						month = str(len(roman)).zfill(2)
				if month and month != '00' and len(day) <= 2:
					if normalize:
						results.append(year + '-' + month + '-' + day)
					else:
						results.append(item[0])
			if not results:
				matches = _re.findall(r'\b(?<!\-)([0123]?\d)[\.\-aáeéint]+(?![kloópr])', re.IGNORECASE,
									  self.ntext if convert else self.text)
				for item in matches:
					if int(item) <= 31:
						if normalize:
							year = str(now.year)
							month = str(now.month).zfill(2)
							day = item.zfill(2)
							results.append(year + '-' + month + '-' + day)
						else:
							results.append(item)
		return results

	# extract times like 12:00 or délután 4
	def times(self, normalize=True, convert=True, current=False):
		if self.text:
			matches = _re.findall(
				r'\b((?:ma\s?|holnap(?:\s?ut[aá]n)?\s?|tegnap(?:\s?el[oöő]t+)?\s?)?(?:reggel\s?|hajnal(?:i|ban)?\s?|d[eé]lel[oöő]t+\s?|d\.?e\.?\s?|d[eé]lut[aá]n\s?|d\.?u\.?\s?|este\s?|[eé]j+el\s?)?\,?\s?(?:[12345]?\d\s?perc+el\s)?(?:(?:h[aá]rom)?negyed\s?|f[eé]l\s?)?(?:[012]?\d|d[eé]l\w*|[eé]jf[eé]l\w*)\s?(?:\:\s?|k[oö]z[oö]t+|\-?kor\s?|\-?t[oóöő]l|\-?ig?|\-?r[ae]|[oó]r[aá]\w{0,3}\s?)?(?:el[oöő]t+\s?|ut[aá]n\s?)?(?:[0123456]?\d[\-\s]?(?![cmntvz][ae]l)(?:kor|t[oóöő]l|ig?|r[ae]|perc\w{0,3})?(?:\s?(?:(?:h[aá]rom)?negyed\s?|f[eé]l\s?)?([012]?\d(?:\sel[ooöő]t+|ut[aá]n)?))?)?\,?\s?(?:ma\s?|holnap(?:\s?ut[aá]n)?\s?|tegnap(?:\s?el[oöő]t+)?\s?)?(?:(1)(?:reggel\s?|hajnal(?:i|ban)?\s?|d[eé]lel[oöő]t+\s?|d\.?e\.?\s?|d[eé]lut[aá]n\s?|d\.?u\.?\s?|este\s?|[eé]j+el\s?))?)',
				re.IGNORECASE, self._ntext_ if convert else self._text_)
			results = []
			if normalize:
				last_pm = None
				for _item in matches:
					item = _item[0]
					if len(item.strip()) > 2:
						item = ' ' + item.lower() + ' '
						hour = "00"
						minute = "00"
						pm = last_pm
						zero = False
						elott = False
						del_matches = _re.findall(r'd[eé]l\w*|[eé]jf[eé]l\w*', re.IGNORECASE, item)
						hour_matches = _re.findall(
							r'\D([012]?\d(?!\d))\D*?(?!perc)(?:\:\s?|k[oö]z[oö]t+|\-?kor|\-?t[oóöő]l|\-?ig?|\-?r[ae]|[oó]r[aá]\w*)?',
							re.IGNORECASE, item)
						minute_matches = _re.findall(
							r'(?!negyed|f[eé]l)\D([0123456]?\d(?!\d))\D*?(?![oó]r[aá])(?:\-?kor|\-?t[oóöő]l|\-?ig?|\-?r[ae]|perc\w*)?',
							re.IGNORECASE, item)
						quarter_matches = _re.findall(r'((?:h[aá]rom)?negyed|f[eé]l)', re.IGNORECASE, item)
						am_matches = _re.findall(r'(reggel|hajnal|d[eé]lel[oöő]t|d\.?e\.?)', re.IGNORECASE, item)
						pm_matches = _re.findall(r'(d[eé]lut[aá]n|d\.?u\.?|este|[eé]j+el)', re.IGNORECASE, item)
						if len(hour_matches) in (1, 2):
							if len(hour_matches) == 1:
								if len(minute_matches) == 1:
									hour = (hour_matches[0])
									minute = "00"
								elif len(minute_matches) == 2:
									if (hour_matches[0]) == (minute_matches[0]):
										hour = (hour_matches[0])
										minute = (minute_matches[1])
									else:
										hour = (hour_matches[0])
										minute = (minute_matches[0])
							else:
								if len(minute_matches) == 2:
									if (hour_matches[0]) == (minute_matches[1]):
										hour = (hour_matches[0])
										minute = (minute_matches[0])
									else:
										hour = (hour_matches[0])
										minute = (minute_matches[1])
								elif len(minute_matches) == 1:
									if (hour_matches[0]) == (minute_matches[0]):
										hour = (hour_matches[1])
										minute = "00"
									else:
										hour = (hour_matches[0])
										minute = (minute_matches[0])
								else:
									hour = (hour_matches[0])
									if len(hour_matches) == 2:
										minute = (hour_matches[1])
							if hour[0] == '0':
								zero = True
							hour = int(hour)
							minute = int(minute)
							if hour > 24 and minute < 24:
								minute, hour = hour, minute
							if minute > 60:
								minute = 0
							if _re.findall(r'(el[oöő]t+)', re.IGNORECASE, item):
								if minute:
									if not _re.findall(r'(el[oöő]t+.+?perc)', re.IGNORECASE, item):
										hour, minute = minute, hour
									elott = True
									hour -= 1
									minute = 60 - minute
							if _re.findall(r'(perccel.+?ut[aá]n+)', re.IGNORECASE, item):
								hour, minute = minute, hour
								hour = hour
							if quarter_matches:
								if quarter_matches[0] in ('fel', 'fél'):
									if not elott:
										hour -= 1
									minute += 30
								elif quarter_matches[0] in ('haromnegyed', 'háromnegyed'):
									if not elott:
										hour -= 1
									minute += 45
								elif quarter_matches[0] in ('negyed'):
									if not elott:
										hour -= 1
									minute += 15
							if not zero:
								if pm_matches:
									pm = True
								elif not am_matches:
									if current is not False:
										now = current
									else:
										now = datetime.datetime.now().hour
									if 'holnap' in item and hour < 9:
										pm = True
									elif hour < 12 and now > hour and last_pm is not False:
										pm = True
								else:
									pm = False
								if pm and hour <= 12:
									hour += 12
							hour %= 24
							minute %= 60
							last_pm = pm
							results.append(str(hour).zfill(2) + ':' + str(minute).zfill(2))
						elif del_matches:
							if 'jf' in item:
								results.append('00:00')
							else:
								results.append('12:00')
			else:
				for item in matches:
					item = item[0].strip()
					ok = False
					for char in item:
						if not char.isnumeric():
							ok = True
					if item and ok:
						results.append(item)
			return results
		return []

	# extract list of time durations
	def durations(self, normalize=True, convert=True):
		if self.text:
			matches = _re.findall(
				r'\b((?:(?:(?:\d\s?)+(?:[\.\,]\d+)?\s(?:(?:[eé]s\s)?(?:f[eé]l|(?:h[aá]rom)?negyed)\s)?(?:(?:(?:t[ií]zed|sz[aá]zad|ezred)?m[aá]sod)?perc\w{0,3}|[oó]r[aá]\w{0,3}|nap\w{0,3}|7\w{0,3}|h[eé]t\w{0,3}|h[oó]nap\w{0,3}|[eé]v\w{0,3})(?:\s(?:m[uú]lva|r[aá]|(?:ez)?el[oöő]t+|el[oöő]b+|k[eé]s[oö]b+|bel[uü]l|h[aá]tr(?:a|[eé]bb)|vissza|el[oöő]re))?)(?:\W{1,2}(?:[eé]s|meg)?\W*)?)+)',
				re.IGNORECASE, self.ntext if convert else self.text)
			if normalize:
				results = []
				now = datetime.datetime.now()
				for item in matches:
					sub_matches = _re.findall(
						r'\b((?:(?:\d\s?)+(?:[\.\,]\d+)?\s(?:(?:[eé]s\s)?(?:f[eé]l|(?:h[aá]rom)?negyed)\s)?(?:(?:(?:t[ií]zed|sz[aá]zad|ezred)?m[aá]sod)?perc\w{0,3}|[oó]r[aá]\w{0,3}|nap\w{0,3}|7|h[eé]t\w{0,3}|h[oó]nap\w{0,3}|[eé]v\w{0,3})(?:\s(?:m[uú]lva|r[aá]|(?:ez)?el[oöő]t+|el[oöő]b+|k[eé]s[oö]b+|bel[uü]l|h[aá]tr(?:a|[eé]bb)|vissza|el[oöő]re))?))',
						re.IGNORECASE, item)
					val = 0
					for sub_item in sub_matches:
						match = sub_item.lower().replace(',', '.')
						sval = ''
						for char in match:
							if char.isdigit() or char == '.':
								sval += char
							else:
								break
						sval = float(sval)
						mpx = 1
						if 'tized' in match or 'tízed' in match:
							mpx = 0.1
						elif 'szazad' in match or 'század' in match:
							mpx = 0.01
						elif 'ezred' in match:
							mpx = 0.001
						elif 'masod' in match or 'másod' in match:
							mpx = 1
						elif 'perc' in match:
							mpx = 60
						elif 'or' in match or 'ór' in match:
							mpx = 3600
						elif 'ho' in match or 'hó' in match:
							if now.month in (1, 3, 5, 7, 8, 10, 12):
								mpx = 86400 * 31
							elif now.month == 2:
								if now.year % 400 == 0 or now.year % 100 == 0 or now.year % 4 == 0:
									mpx = 86400 * 29
								else:
									mpx = 86400 * 28
							else:
								mpx = 86400 * 30
						elif 'nap' in match:
							mpx = 86400
						elif 'het' in match or 'hét' in match or '7' in match:
							mpx = 604800
						elif 'ev' in match or 'év' in match:
							if now.year % 400 == 0 or now.year % 100 == 0 or now.year % 4 == 0:
								mpx = 86400 * 366
							else:
								mpx = 86400 * 365
						sval *= mpx
						if 'fel' in match or 'fél' in match:
							sval += mpx * .5
						elif 'negyed' in match:
							if 'háromnegyed' in match or 'haromnegyed' in match:
								sval += mpx * .75
							else:
								sval += mpx * .25
						val += sval
					if _re.findall(r'\b(el[oöő]t+|el[oöő]b+|h[aá]tr[aáeé]b*|vissza)', re.IGNORECASE, item):
						val *= -1
					results.append(val)
				return results
			else:
				return [item.strip() for item in matches]
		return []

	# extract list of common currencies from text (including $ € £ ￥ and forints)
	def currencies(self, normalize=True, convert=True):
		if self.text:
			matches = _re.findall(
				r'((?:(?:\$|€|£|￥)\s?(?:\d(?:[\s\.,]\d)?)+)|(?:(?:\d(?:[\s\.,]\d)?)+\s?(?:\.\-|\$|€|£|￥|huf\b|ft\b|forint\w{0,3}|[jy]en\w{0,3}|font\w{0,3}|doll[aá]r\w{0,3}|eur[oó]?\w{0,3}|gbp\b|usd\b|jpy\b))(?:\,?\s(?:[eé]s\s)?\d+\s?(?:cent|fill[eé]r)\w{0,3})?)',
				re.IGNORECASE, self.ntext if convert else self.text)
			if normalize:
				results = []
				for item in matches:
					if 'cent' in item or 'fill' in item:
						switch = False
						amount = ""
						cent = ""
						for char in item:
							if char != ' ':
								if not switch and not char.isdigit():
									switch = True
								elif not switch and char.isdigit():
									amount += char
								elif switch and char.isdigit():
									cent += char
						if not amount:
							amount = "0"
						if not cent:
							cent = "0"
					else:
						amount = item
						cent = "0"
					amount = ''.join([e for e in amount.replace(',', '.') if e.isdigit() or e == '.'])
					if amount[-1] == '.':
						amount = amount[:-1]
					if '.' in amount:
						amount = float(amount)
					else:
						amount = float(amount) + float("0." + cent)
					currency = 'HUF'
					item = item.lower()
					if '$' in item or 'doll' in item or 'usd' in item:
						currency = 'USD'
					elif '€' in item or 'eur' in item:
						currency = 'EUR'
					elif '£' in item or 'font' in item or 'gbp' in item:
						currency = 'GBP'
					elif '￥' in item or 'yen' in item or 'jen' in item or 'jpy' in item:
						currency = 'JPY'
					results.append(str(amount) + ' ' + currency)
				if not results:
					return [str(item) + ' HUF' for item in self._currencies_fallback()]
				return results
			else:
				if not matches:
					return [str(item) for item in self._currencies_fallback()]
				return matches
		return []

	def _currencies_fallback(self):
		dates = [item.replace('-', ':') for item in self.dates()]
		number = [str(item) for item in self.numbers()]
		against = [item[-2] if (len(item) > 2 and item[-1] == 0 and item[-2] == '.') else item for item in number]
		ignore = []
		for item in dates:
			parts = item.split(':')
			for check in against:
				if check in parts:
					ignore.append(check)
				if len(check) > 2 and check[-1] == '0' and check[-2] == '.':
					if check[:-2] in parts:
						ignore.append(check)
		okay = []
		for item in against:
			if item not in ignore:
				if item + '.0' in number:
					okay.append(item + '.0')
				elif item in number:
					okay.append(item)
		return okay

	# extract commands and arguments from text: /help "about lara" will return ['help','about lara']
	def commands(self):
		result = []
		if len(self.text) > 1 and self.text[0] in ('/', '\\'):
			quote = ''
			keyword = ''
			for char in self.text[1:]:
				if char in (' ', '"', "'"):
					if char == ' ':
						if quote:
							keyword += ' '
						else:
							if keyword:
								result.append(keyword)
								keyword = ''
					elif char in ('"', "'"):
						if not quote:
							if keyword:
								result.append(keyword)
								keyword = ''
							quote = char
						elif quote == char:
							if keyword:
								result.append(keyword)
								keyword = ''
							quote = ''
						else:
							keyword += char
				else:
					keyword += char
			if keyword:
				result.append(keyword)
		return result

	# extract list of emojis from text via https://gist.github.com/naotokui/
	def emojis(self):
		if self.text:
			return _re.findall("["
							   u"\U0001F600-\U0001F64F"  # emoticons
							   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
							   u"\U0001F680-\U0001F6FF"  # transport & map symbols
							   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
							   "]", re.UNICODE, self.text)
		return []

	# extract e-mail addresses
	def emails(self):
		if self.text:
			return _re.findall(r'\b([\w\d\-\_\.]+\@[\w\d\-\_\.]+\.\w{2,4}(?:\.\w{2,4})?)\b', re.IGNORECASE, self.text)
		return []

	# extract relative dates like tomorrow or wednesday
	def relative_dates(self, normalize=True, current=False):
		if self.text:
			matches = _re.findall(
				r'\b((?:(?:meg)?el[oöő]z[oöő]|m[uú]lt|(?:r[aá])?k[oö]vetkez[oöő]|j[oö]v[oöő])?\s?(?:h[eé]t(?:i|en)?\s?)?(?:tegnap(?:el[oöő]t+)?|holnap(?:ut[aá]n)?|m[aá](?:i nap)?|h[eé]tf[oöő]|ked+|szerd[aá]|cs[uü]t[oö]rt[oö]k|p[eé]ntek|szo[nm]bat|vas[aá]rnap))(?:[aáeoö][dm])?(?:ig?|r[ae]|t[oóöő]l|[aáeoöő]?t|[dkmnptv][ae][lk]|[aáeoö]?n)?\b',
				re.IGNORECASE, self.text)
			if normalize:
				if current is not False:
					_now = datetime.datetime.strptime(current, "%Y-%m-%d")
				else:
					_now = datetime.datetime.now()
				results = []
				for item in matches:
					item = item.lower()
					now = _now
					if 'holnap' in item:
						if 'ut' in item:
							now += datetime.timedelta(days=2)
						else:
							now += datetime.timedelta(days=1)
					elif 'tegnap' in item:
						if 'el' in item:
							now += datetime.timedelta(days=-2)
						else:
							now += datetime.timedelta(days=-1)
					elif 'ma' not in item and 'má' not in item:
						now -= datetime.timedelta(days=now.weekday())
						if _re.findall(r'((?:meg)?el[oöő]z[oöő]|m[uú]lt)', re.IGNORECASE, item):
							now -= datetime.timedelta(weeks=1)
						elif _re.findall(r'((?:r[aá])?k[oö]vetkez[oöő]|j[oö]v[oöő])', re.IGNORECASE, item):
							now += datetime.timedelta(weeks=1)
						if 'ked' in item:
							now += datetime.timedelta(days=1)
						elif 'szerd' in item:
							now += datetime.timedelta(days=2)
						elif _re.findall(r'cs[uü]t[oö]rt[oö]k', re.IGNORECASE, item):
							now += datetime.timedelta(days=3)
						elif _re.findall(r'p[eé]ntek', re.IGNORECASE, item):
							now += datetime.timedelta(days=4)
						elif _re.findall(r'szo[mn]bat', re.IGNORECASE, item):
							now += datetime.timedelta(days=5)
						elif _re.findall(r'vas[aá]rnap', re.IGNORECASE, item):
							now += datetime.timedelta(days=6)
					results.append(now.strftime('%Y-%m-%d'))
				return results
			else:
				return [item.strip() for item in matches]
		return []

	# extract full timestamps using dates(), relative_dates() and times()
	def timestamps(self, current=False):
		# testing environment
		c_relative = False
		c_times = False
		if current:
			c_relative = current.split()[0]
			now = c_relative
			c_times = int((current.split()[1]).split(':')[0])
		else:
			now = datetime.datetime.now().strftime('%Y-%m-%d')
		dates = self.dates(False)
		relative = self.relative_dates(False, c_relative)
		times = self.times(False, True, c_times)
		dates_pos = []
		relative_pos = []
		times_pos = []
		for item in dates:
			regex = re.compile(r'\b' + re.escape(item), re.IGNORECASE)
			for match in regex.finditer(self.ntext):
				dates_pos.append(match.span()[0])
		for item in relative:
			regex = re.compile(r'\b' + re.escape(item), re.IGNORECASE)
			for match in regex.finditer(self.ntext):
				relative_pos.append(match.span()[0])
		for item in times:
			regex = re.compile(r'\b' + re.escape(item), re.IGNORECASE)
			for match in regex.finditer(self.ntext):
				times_pos.append(match.span()[0])
		dates_pos.append(-1)
		relative_pos.append(-1)
		times_pos.append(-1)
		dates = self.dates()
		relative = self.relative_dates(True, c_relative)
		times = self.times(True, True, c_times)
		results = []
		last_date = ''
		last_date_a = ''
		last_time = ''
		dates_i = 0
		relative_i = 0
		times_i = 0
		for i in range(max(dates_pos + relative_pos + times_pos) + 1):
			if i == dates_pos[dates_i]:
				if last_date or last_time:
					if last_date != last_date_a:
						results.append((last_date or now) + ' ' + (last_time or '??:??'))
						last_time = ''
				if len(dates) > dates_i:
					last_date = dates[dates_i]
				dates_i += 1
			if i == relative_pos[relative_i]:
				if last_date or last_time:
					if last_date != last_date_a:
						results.append((last_date or now) + ' ' + (last_time or '??:??'))
						last_time = ''
				if len(relative) > relative_i:
					last_date = relative[relative_i]
				relative_i += 1
			if i == times_pos[times_i]:
				if len(times) > times_i:
					last_time = times[times_i]
					results.append((last_date or now) + ' ' + (last_time or '??:??'))
				times_i += 1
				last_time = ''
				last_date_a = last_date
		if last_date or last_time:
			if last_date != last_date_a or last_time:
				results.append((last_date or now) + ' ' + (last_time or '??:??'))
		return results

	# Converts text representation of numbers to digits
	def _convert_numbers(self, text):
		if text:
			matches = _re.findall(
				r'((?:m[ií]n[uú]sz\s?|negat[ií]v\s?)?(?:(?:(?:(?:(?:t[ií]z|h[uú]sz|harminc)(?:[eo]n)?)?(?:nulla|eg+y|els[eoöő]|k[eé]t+[oöő]?|m[aá]sod(?:ik)?|h[aá]rom|harmadik|n[eé]g+y|[oö]t|hat|h[eé]t|nyolc|kilenc)(?:v[ae]n)?)(?:milli[aá]rd|milli[oó]|ezer|sz[aá]z)?\W*)|(?:milli[aá]rd|milli[oó]|ezer|sz[aá]z|t[ií]z|h[uú]sz|harminc|nulla|z[eé]r[oó])\W*)+(?:[aeoö]dik)?(?:j?[aáeéi]+[gnt]?|[aáeéoöő]?t|kor|t[oóöő]l|r[ae]|sz[eoö]r|[ckmrtvz]?[ae]l)?)\b',
				re.IGNORECASE, text)
			results = {}
			for match in matches:
				value = 0
				minusc = _re.findall(r'(m[ií]n[uú]sz\s?|negat[ií]v\s?)', re.IGNORECASE, match)
				if minusc:
					minus = -1
					minusm = minusc[0]
				else:
					minus = 1
					minusm = ''
				parts = _re.findall(
					r'((?:(?:(?:(?:t[ií]z|h[uú]sz|harminc)(?:[eo]n)?)?(?:nulla|eg+y|els[eoöő]|k[eé]t+[oöő]?|m[aá]sod(?:ik)?|h[aá]rom|harmadik|n[eé]g+y|[oö]t|hat|h[eé]t|nyolc|kilenc)(?:v[ae]n)?)(?:milli[aá]rd|milli[oó]|ezer|sz[aá]z)?|(?:milli[aá]rd|milli[oó]|ezer|sz[aá]z|t[ií]z|h[uú]sz|harminc|nulla|z[eé]r[oó]))\W*)',
					re.IGNORECASE, match)
				values = []
				for part in parts:
					val = 0
					scale = 1
					if 'nulla' in part:
						val = 0
					elif _re.findall(r'milli[aá]rd', re.IGNORECASE, part):
						scale = 1000000000
					elif _re.findall(r'milli[oó]', re.IGNORECASE, part):
						scale = 1000000
					elif _re.findall(r'ezer', re.IGNORECASE, part):
						if _re.findall(r'sz[aá]z', re.IGNORECASE, part):
							scale = 100000
						elif _re.findall(r'v[ae]n', re.IGNORECASE, part):
							scale = 10000
						else:
							scale = 1000
					elif _re.findall(r'sz[aá]z', re.IGNORECASE, part):
						scale = 100
					if _re.findall(r'v[ae]n', re.IGNORECASE, part):
						elem = re.split('v[ae]n', part)
						if len(elem) == 2:
							val = self._convert_numbers_helper(elem[1], 0) * 10
							val += self._convert_numbers_helper(elem[0], 0)
						else:
							val = self._convert_numbers_helper(elem[0], 0)
						if 'ezer' in part:
							scale = max(scale, 10)
						else:
							scale = max(scale * 10, 10)
					else:
						if _re.findall(r't[ií]z', re.IGNORECASE, part):
							val = 10
							scale = max(scale, 1)
						elif _re.findall(r'h[uú]sz', re.IGNORECASE, part):
							val = 20
							scale = max(scale, 1)
						elif _re.findall(r'harminc', re.IGNORECASE, part):
							val = 30
							scale = max(scale, 1)
						if 'nulla' not in part:
							if not _re.findall(r't[ií]z|h[uú]sz|harminc|v[ae]n', re.IGNORECASE, part):
								val += self._convert_numbers_helper(part, 1)
							else:
								val += self._convert_numbers_helper(part, 0)
					values.append([part, val * scale])
				number = 0
				maxn = 0
				name = ''
				for n in reversed(values):
					old = name
					name = n[0] + name
					if n[1] < maxn:
						if len(str(n[1])) == 3:
							if len(str(maxn)) == 4:
								n[1] *= int(pow(10, len(str(maxn)) - 1))
							else:
								n[1] *= int(pow(10, len(str(maxn)) - 2))
						else:
							n[1] *= int(pow(10, len(str(maxn)) - len(str(n[1])) + 1))
					elif len(str(n[1])) == len(str(maxn)):
						number *= minus
						name = old
						if self._convert_numbers_name(name):
							results[self._convert_numbers_name(minusm + name)] = number
						name = n[0]
						number = 0
					if not _re.findall(r'\b(milli[oó]|ezer)\b', re.IGNORECASE, n[0]):
						number += n[1]
					maxn = pow(10, len(str(n[1])) - 1)
				number *= minus
				if self._convert_numbers_name(name):
					results[self._convert_numbers_name(minusm + name)] = number

			swap = sorted(results.items(), key=lambda x: x[1], reverse=True)
			for item in swap:
				text = _re.sub(r'\b(' + re.escape(item[
													  0]) + r')((?:[aeoö]dik?)?(?:j?[aáeéi]+[gnt]?|[aáeéoöő]?t|kor|t[oóöő]l|r[ae]|sz[eoö]r|[ckmrtvz]?[ae]l)?)?\b',
							   re.IGNORECASE, re.escape(str(item[1])) + r'\2', text)
			return text
		return ''

	def _convert_numbers_name(self, name):
		newname = ''
		for char in name:
			if char.isalnum() or char in (' ', '.', ',', '-'):
				newname += char
		if newname and not newname[-1].isalnum():
			newname = newname[:-1]
		return newname.strip()

	def _convert_numbers_helper(self, match, default):
		if _re.findall(r'(k[eé]t+[oöő]?|m[aá]sod(ik)?)', re.IGNORECASE, match):
			return 2
		elif _re.findall(r'(harmadik|h[aá]rom)', re.IGNORECASE, match):
			return 3
		elif _re.findall(r'n[eé]g+y', re.IGNORECASE, match):
			return 4
		elif 'egy' in match or 'els' in match or 'eggy' in match:
			return 1
		elif _re.findall(r'[oö]t', re.IGNORECASE, match):
			return 5
		elif _re.findall(r'hat', re.IGNORECASE, match):
			return 6
		elif _re.findall(r'h[eé]t', re.IGNORECASE, match):
			return 7
		elif _re.findall(r'nyolc', re.IGNORECASE, match):
			return 8
		elif _re.findall(r'kilenc', re.IGNORECASE, match):
			return 9
		return default


# Wrapper Class for Regular Expression Caching
class _re:
	compile_cache = {}
	findall_cache = {}
	finditer_cache = {}
	words_cache = {}

	# cache re.compile() outputs
	def compile(e_hash, expression, flags):
		flags_str = str(flags)
		if flags_str not in _re.compile_cache:
			_re.compile_cache[flags_str] = {}
		if e_hash not in _re.compile_cache[flags_str]:
			if flags:
				cache = re.compile(r'' + expression, flags)
				_re.compile_cache[flags_str][e_hash] = cache
			else:
				cache = re.compile(r'' + expression)
				_re.compile_cache[flags_str][e_hash] = cache

	# cache re.compile().findall() outputs
	def findall(expression, flags, text):
		e_hash = hashlib.sha1(str(expression).encode("utf-8")).hexdigest()
		_re.compile(e_hash, expression, flags)
		t_hash = hashlib.sha1(str(text).encode("utf-8")).hexdigest()
		flags_str = str(flags)
		if flags_str not in _re.findall_cache:
			_re.findall_cache[flags_str] = {}
		if t_hash not in _re.findall_cache[flags_str]:
			_re.findall_cache[flags_str][t_hash] = {}
		if e_hash not in _re.findall_cache[flags_str][t_hash]:
			_re.findall_cache[flags_str][t_hash][e_hash] = _re.compile_cache[flags_str][e_hash].findall(text)
		return _re.findall_cache[flags_str][t_hash][e_hash]

	# for some unknown reason this does not work as intended
	'''
	def finditer(expression,flags,text):
		e_hash			= hashlib.sha1(str(expression).encode("utf-8")).hexdigest()
		_re.compile(e_hash,expression,flags)
		t_hash			= hashlib.sha1(str(text).encode("utf-8")).hexdigest()
		flags_str		= str(flags)
		if flags_str not in _re.finditer_cache:
			_re.finditer_cache[flags_str]	= {}
		if t_hash not in _re.finditer_cache[flags_str]:
			_re.finditer_cache[flags_str][t_hash]	= {}
		if e_hash not in _re.finditer_cache[flags_str][t_hash]:
			_re.finditer_cache[flags_str][t_hash][e_hash]	= _re.compile_cache[flags_str][e_hash].finditer(text)
		return _re.finditer_cache[flags_str][t_hash][e_hash]
	'''

	# user cached re.compile() for re.sub()
	def sub(expression, flags, repl, string):
		e_hash = hashlib.sha1(str(expression).encode("utf-8")).hexdigest()
		_re.compile(e_hash, expression, flags)
		flags_str = str(flags)
		return _re.compile_cache[flags_str][e_hash].sub(repl, string)

	def words(text):
		t_hash = hashlib.sha1(str(text).encode("utf-8")).hexdigest()
		if t_hash not in _re.words_cache:
			_re.words_cache[t_hash] = lara.nlp.number_of_words(text)
		return _re.words_cache[t_hash]

	# clean cache
	def flush(self):
		_re.compile_cache = {}
		_re.findall_cache = {}
