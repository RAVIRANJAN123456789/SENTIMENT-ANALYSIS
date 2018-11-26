# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 02:13:04 2018

@author: Ravi Ranjan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:25:49 2018

@author: Ravi Ranjan
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration.I don't like long sentences!So,I am making it short."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

def untokenize(words):
    text="hi,this is ravi @ l!!"
    print(nltk.word_tokenize(text))
    "".join([""+i if i.startswith("'") and i not in words.punctuation else i for i in text]).strip()
print(word_tokenize(example_sent))
print(untokenize(word_tokens))


    
    