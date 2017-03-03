# lara-hungarian-nlp
#### Lara is a Python3 NLP Class for ChatBots written in Hungarian language. The Class is capable of matching inflected forms of keywords in text messages written in hungarian. 

Due to the complexity of the hungarian language most known stemmers and lemmatisers either fail to find the correct lemmas or require a lot of computational power while relying on large dictionaries. Lara provides a smart workaround for this, by tackling the problem the other way around. The user can provide a set of root words and their word classes, and Lara will automatically create complex regular expressions to match most of the root words’ possible inflected forms. The user can then match any root word with a given text and check wether any inflected forms of that word are present. However, it is worth noting that this method might also give false positives for certain words.

Lara is perfect for developing chatbots in hungarian language, where certain keywords would trigger certain answers. The Class will allow developers to easly match almost every possible inflected forms of any keyword in hungarian language. For example:
```
{"do"		: [{"stem":"csinál","class":"verb"}]}
```

Will match the intent „do” in the following sentences:
- Ő mit csinál a szobában?
- Mit fogok még csinálni?
- Mikor csináltad meg a szekrényt?
- Megcsináltatták a berendezést.
- Teljesen kicsinálva érzem magamat ettől a melegtől.
- Csinálhatott volna mást is.
- Visszacsinalnad az ekezeteket a billentyuzetemen, kerlek?

The Class also comes with some basic NLP functions that are most useful for processing short texts in hungarian. Please note, that despite being an NLP Class, Lara is incompatible with languages other than hungarian. It was developed with the focus on all the quirks and specialities of the hungarian grammar in mind and was not meant to be an equally useful processing tool for all languages. 
