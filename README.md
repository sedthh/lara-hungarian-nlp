# lara-hungarian-nlp
**Lara** is a Python3 NLP Class for ChatBots written in Hungarian language. The Class is capable of matching inflected forms of keywords in text messages written in hungarian. 

# Table of contents

1. [Description](#description)
2. [Documentation](#documentation)
  1. [Examples](#examples)
  2. [Functions](#functions)
    1. [Parser functions](#parser-functions)
    2. [NLP functions](#nlp-functions)
  3. [Declaring intents](#declaring-intents)
3. [Misc.](#misc)

## Description
Due to the complexity of the hungarian language most known stemmers and lemmatisers either fail to find the correct lemmas or require a lot of computational power while relying on large dictionaries. Lara provides a smart workaround for this, by tackling the problem the other way around. The user can provide a set of root words and their word classes, and Lara will automatically create complex regular expressions to match most of the root words’ possible inflected forms. The user can then match any root word with a given text and check wether any inflected forms of that word are present. However, it is worth noting that this method might also give false positives for certain words.

Lara is perfect for developing chatbots in hungarian language, where certain keywords would trigger certain answers. The Class will allow developers to easly match almost every possible inflected forms of any keyword in hungarian language. For example:
```python
{"do"		: [{"stem":"csinál","class":"verb"}]}
```

Will match the intent „do” in the following sentences:
- Ő mit **csinál** a szobában?
- Mit fogok még **csinálni**?
- Mikor **csináltad** meg a szekrényt?
- **Megcsináltatták** a berendezést.
- Teljesen **kicsinálva** érzem magamat ettől a melegtől.
- **Csinálhatott** volna mást is.
- **Visszacsinalnad** az ekezeteket a billentyuzetemen, kerlek?

The Class also comes with some basic NLP functions that are most useful for processing short texts in hungarian. Please note, that despite being an NLP Class, Lara is incompatible with languages other than hungarian. It was developed with the focus on all the quirks and specialities of the hungarian grammar in mind and was not meant to be an equally useful processing tool for all languages. 

## Documentation
**The usage of the Class will be explained in hungarian.**

A Lara egy magyar nyelvű, alacsony számítási igényű szövegfeldolgozó osztály Python 3 alá, rövid szöveges üzenetek kulcsszavainak kinyerésére. Automatizálva megállapíthatjuk a szöveg szándékát, úgy, hogy egy dictionary-ben szándékokat definiálunk, amelyekhez a hozzájuk tarrtozó szavak listáját rendeljük. Az elfogadott szavak ezen listájában elegendő a szó szótövét és annak szófaját definiálnunk. Ezek alapján az osztály olyan reguláris kifejezéseket hoz létre, amelyek az adott szótő majdnem minden szófajának megfelelő ragozott alakját képes azonosítani a folyószövegben. 

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

#### Functions
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
| `example.match_best_intents(text="...",[n=1])`  | Returns a dictinoary with n largest score intent:score pairs. If less than n intents were found, returns them all. |
Function str(), repr(), len() and logical operators eq (==), ne (!=) and addition (+) are also available.

Public functions outside of the lara.paser.Intents() Class:

| Function | Description |
| ---         | ---     |
| `lara.parser.match_intents(Intent instance or dictionary, text)` | Same as example.match_all_intents(text), but it allows declaring intents on the fly. |
| `lara.parser.merge_dicts(Arbitrary number of dictionaries)` | Allows merging dictionaries. |
| `lara.parser.get_common_intents()` | Returns dictionary of common intents, that are useful for chatbot development. |

The get_common_intents() function can be used as follows: `example += lara.parser.get_common_intents()`

| Key of common intent | Description |
| ---         | ---     |
| `_negative` | Negation, denial, opposition, etc. **(nem, ne, stb.)**|
| `_positive` | Affirmation, agreeing **(igen, ja, stb.)** |
| `_greeting` | Greeting, saying hello |
| `_leaving` | Leaving, saying bye |
| `_thanking` | Thanking something |
| `_command` | Giving an order / imperative mode |
| `_question` | Asking questions / interrogative mode |
| `_conditional` | Conditional mode |

###### NLP functions

| Function | Description |
| ---         | ---     |
| `lara.nlp.strip_accents(text)` | Returns text without accents (á->a, é->e, etc.). |
| `lara.nlp.trim(text)` | Trims text *and* removes all whitespaces. |
| `lara.nlp.remove_punctuation(text, [replace=''])` | Removes punctuation from text. |
| `lara.nlp.remove_double_letters(text, [replace=''])` | The function replaces characters that are followed by the same character multiple times into single characters (kappan->kapan, busszal->buszal). Case sensitive. |
| `lara.nlp.remove_space_between_numbers(text,[replace=''])` | Removes whitespaces and 
hyphens between numbers (useful for aprsing phone numbers). |
| `lara.nlp.remove_urls(text,[replace=''])` | Removes valid URLs from text. |
| `lara.nlp.remove_email_addresses(text,[replace=''])` | Removes valid e-mail addresses from text. |
| `lara.nlp.remove_html_Tags(text,[replace=''])` | Removes possible HTML tags from text with regular expressions. Regular epressions are not the most efficient solutions for parsing HTML but it usually works for chat messages. |
| `lara.nlp.find_hashtags(text)` | Returns a list of extracted #hashtags. |
| `lara.nlp.find_mentions(text)` | Returns a list of extracted @mentions. |
| `lara.nlp.find_urls(text)` | Returns a list of extracted valid URLs. |
| `lara.nlp.vowel_harmony(word,[vegyes=True])` | Returns the vowel harmony for a word. Can return 'magas', 'mely' and 'vegyes' if optional vegyes parameter was set to True. |
| `lara.nlp.vowel_ending(word)` | Returns True if word ends with a vowel. Returns False otherwise. |
| `lara.nlp.strip_context(text,[context="search"],[including=None])` | Removes words from text that are unimportant based on ceontext. If context is set to "search", words regarding search commands are removed, so the rest of the text could be used as a clean search query. If the optional including variable can be either a regular expression or a string used as a regualr expression. If set, matching words characters will also be removed from the text.  |
| `lara.nlp.extract_message(text)` | Removes a dictionary of extracted items. If text contains a command, the command key will be set accordingly. Arguments following a command will be added as list elements. List of existing hashtags, mentions and urls are also included in this dictionary. This is useful if you want to do a quick check on your received text message. |

#### Declaring intents
TODO: add word classes, tricks and tips, etc.

## Misc
TODO list
TODO current uses of this class
License
