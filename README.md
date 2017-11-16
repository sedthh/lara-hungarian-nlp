**LARA** is a lightweight Python3 NLP library for ChatBots written in Hungarian language. The parser Class is capable of matching inflected forms of keywords in text messages written in hungarian. **Lara** also comes with a collection of common NLP functions for text processing.

# Table of contents

1. [Description](#description)
2. [Documentation](#documentation)
	1. [Examples](#examples)
	2. [Declaring intents](#declaring-intents)
		1. [Wordclasses](#wordclasses)
		2. [Other properties](#other-properties)
	3. [Functions](#functions)
		1. [Parser functions](#parser-functions)
		2. [Named entities](#named-entities)
		3. [NLP functions](#nlp-functions)
		3. [Stemmer functions](#stemmer-functions)
		4. [Generating intents](#generating-intents)
		5. [Tips and tricks](#tips-and-tricks)
3. [Misc.](#misc)
	1. [Known applications](#known-applications)
	2. [To do list](#to-do-list)

## Description
Due to the complexity of the hungarian language most known stemmers and lemmatisers either fail to find the correct lemmas or require a lot of computational power while relying on large dictionaries. **Lara** provides a smart workaround for this, by tackling the problem the other way around. The user can provide a set of root words and their word classes, and Lara will automatically create complex regular expressions to match most of the root words’ possible inflected forms. The user can then match any root word with a given text and check wether any inflected forms of that word are present. However, it is worth noting that this method might also give false positives for certain words.

**Lara** is perfect for developing chatbots in hungarian language, where certain keywords would trigger certain answers. The Class will allow developers to easly match almost every possible inflected forms of any keyword in hungarian language. For example:
```python
{"to_do"		: [{"stem":"csinál","wordclass":"verb"}]}
```

Will match the intent „to_do” in the following sentences:
- Ő mit **csinál** a szobában?
- Mit fogok még **csinálni**?
- Mikor **csináltad** meg a szekrényt?
- **Megcsináltatták** a berendezést.
- Teljesen **kicsinálva** érzem magamat ettől a melegtől.
- **Csinálhatott** volna mást is.
- **Visszacsinalnad** az ekezeteket a billentyuzetemen, kerlek?

The Class also comes with some basic NLP functions that are most useful for processing short texts in hungarian. Please note, that despite being an NLP Class, **Lara** is currently incompatible with languages other than hungarian. It was developed with the focus on all the quirks and specialities of the hungarian grammar in mind and was not meant to be an equally useful processing tool for all languages. 

## Documentation
**The usage of the Class will be explained in hungarian.**

A **Lara** egy magyar nyelvű, alacsony számítási igényű szövegfeldolgozó osztály Python 3 alá, rövid szöveges üzenetek kulcsszavainak kinyerésére. Automatizálva megállapíthatjuk a szöveg szándékát, úgy, hogy egy dictionary-ben szándékokat definiálunk, amelyekhez a hozzájuk tarrtozó szavak listáját rendeljük. Az elfogadott szavak ezen listájában elegendő a szó szótövét és annak szófaját definiálnunk. Ezek alapján az osztály olyan reguláris kifejezéseket hoz létre, amelyek az adott szótő majdnem minden szófajának megfelelő ragozott alakját képes azonosítani a folyószövegben. 

#### Examples
*A következő példában 3 szándékot definiálunk, amelyekhez 1-1 szótövet és azok szófajait társítjuk. Az osztály a példamondatban megtalálja ezeket a szándékokat, annak ellenére, hogy a megadott szavak ragozott formában vannak.*
```python
import lara
alma_intents	= {
	"alma"			: [{"stem":"alma","wordclass":"noun"}],
	"szed"			: [{"stem":"szed","wordclass":"verb"}],
	"piros"			: [{"stem":"piros","wordclass":"adjective"}]
}
alma_test		= lara.parser.Intents(alma_intents)
print(alma_test.match_all_intents("Mikor szedjük le a pirosabb almákat?"))
 
>>> {'alma': 1, 'szed': 2, 'piros': 2}
```

*A szótövek mellett elő-, és utótagok is definiálhatók lista elemként. Igék (verb) definiálása esetén az alapértelmezett előtagok a gyakori igekötők.*
```python
import lara
busz_intents	= {
	"palyaudvar"	: [{"stem":"pályaudvar","wordclass":"noun","prefix":["busz"]}],
	"auto"			: [{"stem":"autó","wordclass":"noun","affix":["busz"]}],
	"szinten_jo"	: [{"stem":"pálya","wordclass":"noun","prefix":["busz"],"affix":["udvar"]}]
}
busz_test		= lara.parser.Intents(busz_intents)
print(busz_test.match_all_intents("Lassan beérünk az autóval a pályaudvarra."))
print(busz_test.match_all_intents("Lassan beérünk az autóbusszal a buszpályaudvarra."))
 
>>> {'palyaudvar': 2, 'auto': 2, 'szinten_jo': 2}
>>> {'palyaudvar': 2, 'auto': 1, 'szinten_jo': 2}
```

*Teljes-, és részlegeshasonlulás, szótövek megváltozása esetén a szkript nem képes automatikusan, önmagától lekezelni a ragozott formákat. Ebben az esetben az új, megváltozott szótöveket is definiálnunk kell. A "match_stem" kapcsoló segítségével definiálhatunk olyan szótöveket, amelyeket önmagukban állva nem, de tovább ragozva már elfogad az osztály találatként. Az alábbi példában az eszik ige ragozott alakjait találjuk meg, az "esz" és "en" morfémák segítségével, de az "esz" és "en" szavakat nem fogadjuk el találatként.*
```python
import lara
hasonul_intents	= {
	"enni"		: [{"stem":"esz","wordclass":"verb","match_stem":False}, {"stem":"en","wordclass":"verb","match_stem":False}]
}
hasonul_test	= lara.parser.Intents(hasonul_intents)
print(hasonul_test.match_all_intents("Tőmorfémák: esz, en.")) # nem veszi figyelembe
print(hasonul_test.match_all_intents("Eszel valamit?"))
print(hasonul_test.match_all_intents("Azt nem lehet megenni."))
 
>>> {}
>>> {'enni': 2}
>>> {'enni': 2}
```

*Előfordulhat, hogy szókapcsolatok megtalálására van szükségünk a szándékok értelmezéséhez. Ebben az esetben a "with" változóban további szándékokat, szavakat definiálhatunk. A pontozás beállításával definiálhatunk olyan eseteket is, amikor egy szó önmagában állva nem elegendő, de más szavakkal együtt már elfogadottá válik.*
```python
import lara
egyutt_intents	= {
	"jo_ido"	: [{"stem":"jó","wordclass":"adjective","score":0,
				"with":[{"stem":"idő","wordclass":"noun","affix":["járás"]}, {"stem":"meleg","wordclass":"adjective"}]}]
}
egyutt_test		= lara.parser.Intents(egyutt_intents)
print(egyutt_test.match_all_intents("Jó.")) # nem veszi figyelembe
print(egyutt_test.match_all_intents("Meleg van."))	# nem veszi figyelembe
print(egyutt_test.match_all_intents("Milyen az időjárás?"))	# nem veszi figyelembe
print(egyutt_test.match_all_intents("Jó meleg van."))
print(egyutt_test.match_all_intents("Jó az idő."))
print(egyutt_test.match_all_intents("Jó meleg az idő."))  # dupla pont
print(egyutt_test.match_all_intents("Jó meleg az időjárás.")) # dupla pont
>>> {}
>>> {}
>>> {}
>>> {'jo_ido': 2}
>>> {'jo_ido': 2}
>>> {'jo_ido': 4}
>>> {'jo_ido': 4}
```

*Hasonlóan, definiálhatunk olyan szavakat is, amelyek megjelenésekor figyelmen kívül hagyjuk az egész szándékot.*
```python
import lara
kulon_intents	= {
	"jobb_ido"	: [{"stem":"jó","wordclass":"adjective","score":0,
				"with":[{"stem":"idő","wordclass":"noun","affix":["járás"]}, {"stem":"meleg","wordclass":"adjective"}],
				"without":[{"stem":"este","wordclass":"noun"}, {"stem":"esté","match_stem":False,"wordclass":"noun"}]}]
}
kulon_test		= lara.parser.Intents(kulon_intents)
print(kulon_test.match_all_intents("Jó."))  # nem veszi figyelembe
print(kulon_test.match_all_intents("Jó meleg az időjárás."))  # dupla pont
print(kulon_test.match_all_intents("Jó estét!"))  # nem veszi figyelembe
print(kulon_test.match_all_intents("Jó meleg esténk van!")) # szintén nem veszi figyelembe
>>> {}
>>> {'jobb_ido': 4}
>>> {}
>>> {}
```

*Fontos megjegyezni, hogy olyan szavakat is elfogadhat az osztály, amelyek ragozott vagy ragozatlan alakjai megegyeznek más szavak ragozott vagy ragozatlan alakjaival. Hasonlóan, nem értelmes, de nyelvtani szabályok szerint lehetséges ragozást és egyes esetekben a reguláris kifejezések miatt teljesen értelmetlen szavakat is elfogadhat az osztály találatként!*
```python
import lara
fals_pozitiv	= {
	"megszerel"	: [{"stem":"szerel","wordclass":"verb"}],
	"hibasan"	: [{"stem":"alma","wordclass":"noun"}],
}
hibas_test		= lara.parser.Intents(fals_pozitiv)
print(hibas_test.match_all_intents("Gyönyörű dolog a szerelem!")) # elfogadja hibásan
print(hibas_test.match_all_intents("Ezt is elfogadja találatként: Almainüdböz"))  # elfogadja hibásan
>>> {'megszerel': 2}
>>> {'hibasan': 2}
```
Az itt leírt példák a **test.py** fájlban is megtalálhatók. 

#### Declaring intents
**The usage of Intents will be explained in hungarian.**

Minden intenció elemnek tartalmaznia kell minimum egy `stem` változót, amiben a ragozatlan szótő, morféma kell, hogy álljon **string**ként. 
###### Wordclasses
Az alábbi szófajok adhatók meg a `wordclass` változóban:

| Szófaj | Magyarázat |
| ---         | ---     |
| `special` | Alapértelmezett érték. Ebben az esetben semmilyen reguláris kifejezés nem generálódik a szó ragozott formáinak megtalálásához. Egy az egyben történő szóbeli egyezés esetén ad csak találatot. Alapértelmezetten nem tesz különbséget a kis-, és nagybetűk között. |
| `noun` | Főnevek esetén alkalmazandó. |
| `verb` | Igék esetén alkalmazandó. Alapértelmezetten a gyakori igekötők automatikusan hozzáadódnak a 'prefix' listához. |
| `adjective` | Melléknevek esetén alkalmazandó. Alapértelmezetten a 'leg' és 'legesleg' fokozások hozzáadódnak a 'prefix' listához. |
| `regex` | Saját reguláris kifejezések megadásához használható. Ebben az esetben nem ajánlott további tulajdonságok definiálása. Alapértelmezetten nem tesz különbséget a kis-, és nagybetűk között | 

Az NLTK tagsetjével való kompatibilitás megőrzéséhez ADJ, NOUN és VERB érétékek is megadhatóak.

A találatok finomítása érdekében a szavakból létrejön egy **alapértelmezett** és egy **tisztított** forma is. A **tisztított**forma az **alapértelmezetten** megadott formából jön létre: 
- Az osztály kicseréli az ékezetes betüket az ékezet nélküli megfelelőire (távolabb->tavolabb).
- Az egymás után egynél többször megjelenő karakterekből az ismétlődéseket törli (tavolabb->tavolab). 
A **tisztított** formák segítségével egyes, speciális ragozott alakok könnyebben detektálhatóak. 

###### Other properties

A `clean_` előtagú változók az előtag nélküli párjaikból, automatikusan generálódnak. Definiálásuk csak nagyon ritka esetekben indokolt.

| Tulajdonság | Alapértelmezett érték | Magyarázat |
| ---         | ---     | ---     |
| `score` | 1 | Minden **alapértelemzett** találat esetén a megadott értékkel növeli meg az intenció pontszámát. Egy intencióra, ha egyszerre létezik **alapértelmezett** és **tisztított** találat, akkor a `score` és a `clean_score` értékét kapja az intenció. |
| `clean_score` |  `score` értéke | Minden **tisztított** találat esetén a megadott értékkel növeli meg az intenció pontszámát. Egy intencióra, ha egyszerre létezik **alapértelmezett** és **tisztított** találat, akkor a `score` és a `clean_score` értékét kapja az intenció. |
| `prefix` |  `wordclass` beállításoktól függ | Az elfogadott előtagok string **list**ája. |
| `clean_prefix` |  `wordclass` beállításoktól függ, egyéni `prefix` megadása esetén alapértelmezetten az egyéni `prefix` **list**ából generálódik | Az elfogadott **tisztított** előtagok string **list**ája. |
| `affix` |  [] | Az elfogadott utótagok string **list**ája. Összetett szavaknál használandó. Vigyázzunk arra, hogy a **list**ában olyan további elemeket adjunk meg, amelyek nem változtatják meg a szófajt. |
| `clean_affix` |  [], egyéni `affix` megadása esetén alapértelmezetten az egyéni `affix` **list**ából generálódik | Az elfogadott **tisztított** utótagok string **list**ája. Összetett szavaknál használandó. |
| `match_stem` |  True | **Boolean** érték, ami azt adja meg, hogy a  `stem ` változóban megadott morfémát önmagában állva is elfogadja-e az osztály találatként. **False** esetén csak a ragozott alakokat, "affix"-szel álló alakokat és "prefix"-szel álló alakokat fogad el. |
| `match_at` |  "any" vagy `wordlcass`:"regex" esetén "regex" | Elfogadott értékek: "regex","start","end" és "any". "start" esetén *mondatrészek* elején fogadja el az intenciót találatként. "end" esetén *mondatrészek* végén fogadja el az intenciót találatként. Tehát sem a "start" sem az "end" nem a szövegben elfoglalt pozíció, hanem a szövegben elfoglalt logikai pozíció alapján próbál találatokat adni. |
| `with` | [] | További intenció **dictionary**k definiálhatóak az együttjárások pontozásához. Csak egy mélységig ellenőriz az osztály, tehát az itt deklarált további intenciók `with` tulajdonságait már nem veszi figyelembe pontozásnál. |
| `without` | [] | További intenció **dictionary**k definiálhatóak, amelyek megtalálásakor a tulajdonos intenció nem kap pontot. |
| `ignorecase` | True | Figyelmen kívül hagyja-e a kis-, és nagybetűk közötti különbséget a `stem` változóban. Hasznos tulajdonnevek vagy mozaikszavak megadásánál. |

#### Functions
**The rest of the functions will be explained in english.**

###### Parser functions
Public functions available in a lara.parser.Intents() Class instance:
```python
import lara
example	= lara.parser.Intents()
```

| Function | Description |
| ---         | ---     |
| `example.add_intents(new_intents={})` | Add a dictionary of intents to the existing dictionary of intents. Duplicates will be discarded. |
| `example.match_all_intents(text="...")` | Find matching intents in a given string. Returns dictionary with intent:score pairs for all intents where score is more than 0. |
| `example.match_all_intents_as_set(text="...")` | Same as above but returns a set of matched Intents instead. |
| `example.match_best_intents(text="...",[n=1])`  | Returns a dictinoary with n largest score intent:score pairs. If less than n intents were found, returns them all. |
| `example.raw_intents(new_intents)` | For optimization purposes only. Replaces all current intents with a dictionary of new intents, without further processing them. NOTE: this function should only be used with previously generated (cached) intents with all necessary variables already created by the class itself. Accepts dictionary of full intents, string of full intents and existing Intent class instances. |

The constructor also accepts instances.
```python
	def __init__(self, new_intents={}, is_raw=False):		
		self.intents	= {}
		if new_intents:
			if is_raw:
				self.raw_intents(new_intents)
			else:
				self.add_intents(new_intents)
```

Function str(), repr(), len() and logical operators eq (==), ne (!=) and addition (+) are also available.

###### Named entities

Some intents and entities are used regularly. **Lara** offers built in Intents to make Chatbot development and named-entity detection easier.

You can add further entities (dictionary of intents) to an existing Intent: `example += lara.entities.common()`

or you can just check for matches without having to create your own Intent class instance:

```python
match_common	= lara.parser.match_intents_as_set(lara.entities.common(), "Köszönöm szépen!")
print(match_common)
	
>>> {"_thanking"}
```

Common entities for Chatbot conversations:

| `lara.entities.common()` |  |
| ---         | ---     |
| `_negative` | Negation, denial, opposition, etc. **(nem, ne, stb.)**|
| `_positive` | Affirmation, agreeing **(igen, ja, stb.)** |
| `_greeting` | Greeting, saying hello |
| `_leaving` | Leaving, saying bye |
| `_thanking` | Thanking something |
| `_command` | Giving an order / imperative mode |
| `_question` | Asking questions / interrogative mode |
| `_conditional` | Conditional mode |
| `_profanity` | Text contains swearwords |

Other entities:

| Function | Description |
| ---         | ---     |
| `lara.entities.counties()` | Hungarian counties and county seats. |


###### NLP functions

| Function | Description |
| ---         | ---     |
| `lara.nlp.strip_accents(text)` | Returns text without accents (á->a, é->e, etc.). |
| `lara.nlp.trim(text)` | Trims text *and* also removes all whitespaces. |
| `lara.nlp.remove_line_breaks(text, [replace=''])` | Removes line breaks from text. |
| `lara.nlp.remove_punctuation(text, [replace=''])` | Removes punctuation from text. |
| `lara.nlp.remove_double_letters(text, [replace=''])` | The function replaces characters that are followed by the same character multiple times into single characters (kappan->kapan, busszal->buszal). Case sensitive. |
| `lara.nlp.remove_space_between_numbers(text,[replace=''])` | Removes whitespaces and hyphens between numbers (useful for aprsing phone numbers). |
| `lara.nlp.remove_urls(text,[replace=''])` | Removes valid URLs from text. |
| `lara.nlp.remove_email_addresses(text,[replace=''])` | Removes valid e-mail addresses from text. |
| `lara.nlp.remove_html_tags(text,[replace=''])` | Removes possible HTML tags from text with regular expressions. Regular epressions are not the most efficient solutions for parsing HTML but it usually works for chat messages. |
| `lara.nlp.remove_smileys(text)` | Removes common smileys from text (does not remove emojis). |
| `lara.nlp.find_hashtags(text)` | Returns a list of extracted #hashtags. |
| `lara.nlp.find_mentions(text)` | Returns a list of extracted @mentions. |
| `lara.nlp.find_urls(text)` | Returns a list of extracted valid URLs. |
| `lara.nlp.find_smileys(text)` | Returns a list of extracted common smileys (does not return emojis). |
| `lara.nlp.vowel_harmony(word,[vegyes=True])` | Returns the vowel harmony for a word. Can return 'magas', 'mely' and 'vegyes' if optional vegyes parameter was set to True. |
| `lara.nlp.is_vowel(letter)` | Returns True if the letter is a vowel. Returns False otherwise. |
| `lara.nlp.is_consonant(letter)` | Returns True if the letter is a consonant. Returns False otherwise. |
| `lara.nlp.vowel_ending(word)` | Returns True if word ends with a vowel. Returns False otherwise. |
| `lara.nlp.consonant_ending(word)` | Returns True if word ends with a consonant. Returns False otherwise. |
| `lara.nlp.number_of_words(text)` | Returns number of words in text, based on the words received from the tokenizer function. |
| `lara.nlp.crop_text(text,limit=100,end='...',reverse=False)` | Returns a maximum of **limit** letters without cutting words in half. If the returned text is longer than the maximum number of letters allowed, the **end** string will be attached to the text. If **reverse** is True, the function will start from the end of the text and add the **end** string to the beggining if needed. |
| `lara.nlp.tokenizer(text)` | Returns words in text as a list. Note that this function only uses regular expressions. |
| `lara.nlp.is_gibberish(text)` | Returns True if text is most likely just gibberish. |
| `lara.nlp.strip_context(text,[context="search\|request\|mail"],[including=None])` | Removes words from text that are unimportant based on ceontext. If **context** is set to "search", words regarding search commands are removed, so the rest of the text could be used as a clean search query. If **context** is set to "request", common words used for making a request are removed from the text, cleaning the query. If **context** is set to "mail", common formalities used in e-mails will be removed from the query. The optional **including** variable can be either a regular expression or a string used as a regualr expression. If set, matching words characters will also be removed from the text.  |
| `lara.nlp.remove_stopwords(text)` | Removes common hungarian stopwords from text. |
| `lara.nlp.metre(text)` | Returns the rhytmic structure of a *verse line* as list of 'u' and '-' characters (former meaning short, latter meaning long foot). For instance: metre('Bús düledékeiden, Husztnak romvára megállék;') would return ['-', 'u', 'u', '-', 'u', 'u', '-', '-', '-', '-', '-', 'u', 'u', '-', '-'] |
| `lara.nlp.metre_pattern(match,pattern)` | Returns True if the the list representing the rhytmic structure of a *verse line* matches the given pattern, defined as a list of 'u' and '-' characters. |
| `lara.nlp.is_hexameter(pattern)` | Returns True if the the metre list representing the rhytmic structure of a *verse line* is a valid Hexameter. |
| `lara.nlp.is_pentameter(pattern)` | Returns True if the the metre list representing the rhytmic structure of a *verse line* is a valid Pentameter. For example:  is_pentameter(metre('Csend vala, felleg alól szállt fel az éjjeli hold.')) would return True |
| `lara.nlp.number_of_syllables(word, [rhyme=False])` | Returns the number of syllables in a word based on the number of its vowels. If **rhyme** is se to True, the returned number of syllables will be harshly based on pronunciation instead (by taking acronyms in account). |
| `lara.nlp.hasDigits(text)` | Returns True if text has a digit in it. |
| `lara.nlp.ngram(tokens,[n=2])` | Returns list of ngrams generated from the list of **tokens** provided. |
| `lara.nlp.extract_message(text)` | Removes a dictionary of extracted items. If text contains a command, the command key will be set accordingly. Arguments following a command will be added as list elements. List of existing hashtags, mentions and urls are also included in this dictionary. This is useful if you want to do a quick check on your received text message. |

###### Stemmer functions

**Lara** also comes with a stemming algorithm for removing the commoner morphological and inflexional endings from words in hungarian. Its main use is as part of a term normalisation process that is usually done when setting up Information Retrieval systems without relying on dictionaries. It's called **tippmix** because its results are slightly better than random guessing. You can call the **stemmer(text)** function the following way:

```python
import lara.tippmix as tippmix
text = '''A szövegbányászat a strukturálatlan vagy kis mértékben strukturált szöveges állományokból történő ismeret kinyerésének tudománya; olyan különböző dokumentumforrásokból származó szöveges ismeretek és információk gépi intelligenciával történő kigyűjtése és reprezentációja, amely a feldolgozás előtt rejtve és feltáratlanul maradt az elemző előtt. '''
print(tippmix.stemmer(text))

>>> ['a', 'szövegbányász', 'a', 'strukturál', 'vagy', 'kis', 'mér', 'strukturál', 'szöveg', 'állományok', 'törte', 'ismer', 'kinyerése', 'tudomány', 'oly', 'különböz', 'dokumentumforrások', 'származ', 'szöveg', 'ismere', 'és', 'információ', 'gép', 'intelligencia', 'törte', 'kigyűjtés', 'és', 'reprezentáció', 'amely', 'a', 'fel', 'dolgoz', 'elő', 'rej', 'és', 'fel', 'tár', 'mar', 'az', 'elemz', 'elő']
```

Note that number of returned stems might be larger than the actual number of words in the text, as the stemmer aslo separates certain adverb particles. 

###### Generating intents

**Lara** also comes with a built in function to automatically generate parser declarations from CSV files. You can declare stems, wordclasses excluding "regex" and the intent itself. You can also declare possible "affix"es and "prefix"es by putting | separated words in parenthesis before or after the stem.

| stem | wordclass | intent |
| ---         | ---     | ---     |
| körte | noun | gyumolcs |
| (sárga)barack | noun | gyumolcs |
| (arany\|zöld)alma | noun | gyumolcs |
| narancs(lé) | noun | gyumolcs |
| (indián\|fekete)meggy(szörp) | noun | gyumolcs |

```python
import pandas as pd
df			= pd.read_csv('example.csv',sep=';',header=0,names=["stem","wordclass","intent"])
csv_intents	= {}	# you can also use existing dictionary of intents to extend them
for index, row in df.iterrows():
	lara.parser.intents_from_csv(row,csv_intents)
print(csv_intents)

>>> {'gyumolcs': [{'stem': 'körte', 'wordclass': 'noun'}, {'prefix': ['sárga'], 'stem': 'barack', 'wordclass': 'noun'}, {'prefix': ['arany', 'zöld'], 'stem': 'alma', 'wordclass': 'noun'}, {'affix': ['lé'], 'stem': 'narancs', 'wordclass': 'noun'}, {'prefix': ['indián', 'fekete'], 'affix': ['szörp'], 'stem': 'meggy', 'wordclass': 'noun'}]}
```

###### Tips and tricks

Setting multiple properties for intents can be useful in detecting patterns:
- In addition to actual words, regular expressions can also be defined as "stem"s. This also applies to "with" and "without" properties' "stem"s. 
- Both "prefix"es and "affix"es can be set at the same time.
- In case inflection would alter a word's "stem", try defining the altered form as another possible Intent **list** element, with the "match_stem" property set to **False**. This way the defined "stem" would only be matched if inflected.  
- If it is unclear wether or not an iflected word form would be matched by the given definitions, it is always a good idea to manually test it first.

## Misc
Initial work: **Richard Nagyfi**, 2016

Special thanks to [Peter Varo](https://github.com/petervaro) for formatting guidelines.

Created in collaboration with the [Institute of Advanced Studies, Kőszeg](http://iask.hu/) and [Kitchen Budapest](http://kibu.hu)

#### Known applications
Feel free to add your own projects to this list if you've found **Lara** useful.

- Hungarian "Napirajz" Chatbot for Facebook Messenger: https://www.facebook.com/NapirajzBot/
- Online News Monitoring in Hungarian Language for visualizing quantity of articles on the immigrant crisis
- Used to develop the AI for Training2038: http://kibu.hu/en/news/training-2038

#### To do list
- Add more word classes (including: numerals nad pronouns).
- Expand named-entity recognition dictionaries.
- Implement furhter NLTK functions aimed for the hungarian language.
- Rewrite regular expressions in a way that autoamtic POS-tagging would be possible in hungarian.
- Create dictionaries to enable sentiment analysis in hungarian.

This project is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for details

