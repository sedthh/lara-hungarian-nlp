# lara-hungarian-nlp
**Lara** is a Python3 NLP Class for ChatBots written in Hungarian language. The Class is capable of matching inflected forms of keywords in text messages written in hungarian. 

# Table of contents

1. [Description](#description)
2. [Documentation](#documentation)
  1. [Examples](#examples)
  2. [Word classes](#word-classes)
  3. [Tricks](#tricks)
  4. [NLP functions](#nlp-functions)
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

#### Word classes
List of available word classes.
#### Tricks
How to get the most out of this class.
#### NLP functions
List of other available NLP functions implemented by this Class.


## Misc
TODO list
