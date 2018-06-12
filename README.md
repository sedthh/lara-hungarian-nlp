## **Lara** is a super fast, lightweight Python3 NLP library for ChatBot AI development in Hungarian language. 

Instead of being an all purpose NLP tool, **Lara** was created to fit the [quirks and uniqueness](https://en.wikipedia.org/wiki/Agglutinative_language) of the Hungarian (online) [language](https://en.wikipedia.org/wiki/Hungarian_language) as much as possible. The library is capable of matching inflected forms of keywords in text messages written in Hungarian. It also comes with functions for text processing, and can even identify common expressions and small talk topics in discussions.

# Table of contents

1. [About Lara](#about-lara)
	1. [Find intents](#find-intents)
	2. [Extract information](#extract-information)
	3. [Handle common topics](#handle-common-topics)
	4. [Create ML features](#create-ml-features)
	5. [And much more](#and-much-more)
2. [Licensing](#licensing)

## About Lara

Here is a short list of things you can easily do with **Lara** in Hungarian. For full documentation and further examples, **CHECK OUT [THE WIKI](https://github.com/sedthh/lara-hungarian-nlp/wiki)**.

#### Find intents

With the Intents() Class, developers can easily match almost every possible inflected form of any keyword in Hungarian language. For example:

```python
from lara import parser

ragozott_forma	= {
	"to_do"		: [{"stem":"csinál","wordclass":"verb"}],
}
ragozott_talalat= parser.Intents(ragozott_forma)
```

Will `match` the intent `"to_do"` in the following sentences:
- Ő mit **csinál** a szobában?
- Mit fogok még **csinálni**?
- Mikor **csináltad** meg a szekrényt?
- **Megcsináltatták** a berendezést.
- Teljesen **kicsinálva** érzem magamat ettől a melegtől.
- **Csinálhatott** volna mást is.
- **Visszacsinalnad** az ekezeteket a billentyuzetemen, kerlek?

By defining the `wordclass` and `stem` of a keyword, **Lara** will generate possible patterns for text matching, without having to rely on large dictionaries!

```python
from lara import parser

alma_intents	= {
	"alma"		: [{"stem":"alma","wordclass":"noun"}],
	"szed"		: [{"stem":"szed","wordclass":"verb"}],
	"piros"		: [{"stem":"piros","wordclass":"adjective"}]
}
alma_test	= parser.Intents(alma_intents)
print(alma_test.match("Mikor szedjük le a pirosabb almákat?"))

>>> {'alma': 1, 'szed': 2, 'piros': 2}
```

#### Extract information

It allows simple text processing:

```python
from lara import parser

tweet		= 'A robotok elveszik a munkát! #NLP #ChatBot'
hashtags	= parser.Extract(tweet).hashtags()
print(hashtags)

>>> ['#nlp','#chatbot']
```

And normalization of extracted strings:

```python
from lara import parser

sms		= 'Hívj fel! A számom 30/123 4567!'
info		= parser.Extract(sms)
print(info.phone_numbers(False))
print(info.phone_numbers(True))

>>> ['30/123 4567']
>>> ['+36 30 1234567']
```

It uses Black Magic™:

```python
from lara import parser

sorcery		= 'Hívj fel ezen a számon 2018 IV. huszadikán mondjuk délután nyolc perccel háromnegyed kettő előtt!'
info		= parser.Extract(sorcery)
print(info.dates())
print(info.times())
	
>>> ['2018-04-20']
>>> ['13:37']
```


#### Handle common topics

Common entities are included:

```python
from lara import parser, entities

user_text	= 'Igen, köszönöm a segítséget!'

common	= entities.common()
print(parser.Intents(common).match_set(user_text))

>>> {'yes', 'thx', 'help'}
```

Several small talk topics are also automatically handled:

```python
from lara import parser, entities

user_text	= 'Te egy ember vagy, vagy egy intelligens számítógép vagy?'

chitchat	= entities.smalltalk()
chitchat_match	= parser.Intents(chitchat).match_set(user_text)
if 'user_love' in chitchat_match:
	print('Én is téged.')
elif 'are_you_a_robot' in chitchat_match:
	print('Egy számítógépet akkor nevezhetünk intelligensnek, ha át tud verni egy embert, hogy őt is embernek higgye.')
	
>>> Egy számítógépet akkor nevezhetünk intelligensnek, ha át tud verni egy embert, hogy őt is embernek higgye.
```


#### Create ML features

Rule based stemmers can help you create features from short Hungarian texts for Machine Learning models, without the need for large dictionaries:

```python
from lara import stemmer, nlp

text 	= '''
	A szövegbányászat a strukturálatlan vagy kis mértékben strukturált 
	szöveges állományokból történő ismeret kinyerésének tudománya; 
	olyan különböző dokumentumforrásokból származó szöveges ismeretek
	és információk gépi intelligenciával történő kigyűjtése és 
	reprezentációja, amely a feldolgozás előtt rejtve és feltáratlanul 
	maradt az elemző előtt. 
	'''

clean	= nlp.remove_stopwords(text)
stems	= stemmer.tippmix(clean)
bigrams = nlp.ngram(stems,2)
print(bigrams)

>>> ['szövegbányász strukturál', 'strukturál kis', 'kis mér', 'mér strukturál', 'strukturál szöveg', 'szöveg állományok', ... 'mar elemz']

```

#### And much more

Use keywords in actual sentences:

```python
from lara import nlp, stemmer

query	= "Toto - Afrika"
	
parts	= query.split('-')
artist	= stemmer.inverse(parts[0],'től')	# "tól" and "től" are both valid
title	= stemmer.inverse(parts[1],'t')
the	= nlp.az(title)
	
print('A zenelejátszó program az alábbi számot játssza:')
print(artist,the,title)

>>> A zenelejátszó program az alábbi számot játssza:
>>> Tototól az Afrikát
```

Better understand poetry:

```python
from lara import nlp

huszt	= ['Bús düledékeiden, Husztnak romvára megállék;',
	'Csend vala, felleg alól szállt fel az éjjeli hold.']

for line in husz:
	print(nlp.metre(line))
	
>>> ['-', 'u', 'u', '-', 'u', 'u', '-', '-', '-', '-', '-', 'u', 'u', '-', '-']
>>> ['-', 'u', 'u', '-', 'u', 'u', '-', '-', 'u', 'u', '-', 'u', 'u', '-']
```

## Licensing

This project has **dual licensing**. You may use it either under the [GNU GPLv3 License](LICENSE.md) for Open Source ChatBot solutions and NLP Research purposes or [contact me](https://github.com/sedthh) about different licensing options for commercial use. 
