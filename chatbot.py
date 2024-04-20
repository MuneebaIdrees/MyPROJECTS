# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:53:19 2020

@author: munee
"""

from nltk.chat.util import Chat, reflections

from newspaper import Article
import random
import string
import nltk
import nltk.data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings 

warnings.filterwarnings('ignore')

#download the punkt package
nltk.download('punkt', quiet=True)

def aries():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/aries/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def taurus():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/taurus/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def gemini():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/gemini/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def cancer():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/cancer/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def leo():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/leo/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def virgo():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/virgo/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def libra():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/libra/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def scorpio():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/scorpio/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def sagittarius():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/sagittarius/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def capricorn():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/capricorn/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def aquarius():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/aquarius/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text
def pisces():
    #get the article
    article= Article("https://astrostyle.com/horoscopes/daily/pisces/")
    article.download()
    article.parse()
    article.nlp()
    corpus=article.text
    text=corpus
    f=int(len(text)-50)
    text=text[0:f]
    return text


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
}



chat_pairs = [
    
     [
        r"hi|hey|hello|AOA|aoa|assalam.o.alaikum|hy",
        ["Assalam.o.alaikum, Tell me your date of birth in the format '4th november'",]
    ],
    
     [
        r"what is your name ?",
        ["My name is ChatBot and I can tell about your today's horoscope !, Tell me your date of birth in the format '4th november'",]
    ],
    
    [
        r"how are you (.*)",
        ["I'm doing good, Tell me your date of birth in the format '4th november'","Alhamdulillah fine, how are you,Tell me your date of birth in the format '4th november'",]
    ],
    
     [
        r"my name is (.*)(.*)",
        ["Assalam.o.alaikum %1 , do you want to know about your daily horoscope?",]
    ],
    
    [
        r"(.*) (yes) (horoscope) (.*)",
        ["Tell me your date of birth in the format '4th november' ",]
    ],
    
    [
        r"aries|ARIES|20th march|20 mar|20th mar|21st march|21 mar|21st mar|22nd march|22nd mar|22 mar|23rd march|23 mar|23rd mar|24th march|24th mar|24 mar|25th march|25th mar|25 mar|26th march|26th mar|26 mar|27th march|27th mar|27 mar|28th march|28th mar|28 mar|29th march|29th mar|29 mar|30th march|30th mar|30 mar|31st march|31st mar|31 mar", 
        [aries()]
    ],
     [
        r"1st april|1 april|2nd april|2 april|3rd april|3 april|4th april|4 april|5th april|5 april|6th april|6 april|7th april|7 april|8th april|8 april|9th april|9 april|10th april|10 april|11th april|11 april|12th april|12 april|13th april|13 april|14th april|14 april|15th april|15 april|16th april|16 april|17th april|17 april|18th april|18 april|19th april|19 april",
        [aries()]
],
     [r"taurus|TAURUS|20 apr|20th april|20th apr|21 apr|21st apr|21 april|22 april|22apr|22nd apr|23 april|23 apr|23rd april|24 apr|24 april|24th april|25 apr|25 april|25th april|26th april|26 apr|26 april|27th april|27 apr|27 april|28 apr|28 april|28th april|29 apr|29th april|29 april|30th april|30 apr|20 april",
      [aries()]
      ],
     [r"1st may|1 may|2 may|2nd may|3 may|3rd may|4th may|4 may|5th may|5 may|6th may|6 may|7th may|7 may|8th may|8 may|9th may|9 may|10th may|10 may|11th may|11 may|12th may|12 may|13th may|13 may|14th may|14 may|15th may|15 may|16th may|16 may|17th may|17 may|18th may|18 may|19th may|19 may|20th may|20 may",
      [taurus()]
      ],
      [r"gemini|GEMINI|21 may|21st may|22 may|22nd may|23 may|23rd may|24th may|24 may|25th may|25 may|26th may|26 may|27th may|27 may|28th may|28 may|29th may|29 may|30th may|30 may|31 may|31st may|1 june|1st june|1 jun|2nd june|2 jun|2 june|3rd june|3 june|3 jun|4th june|4 june|4 jun|5th june|5 june|5 jun|6th june|6 jun|6 june|7th june|7 june|7 jun|",
       [gemini()]
 ],
      [r"8th june|8 june|8 jun|9th june|9 june|9 jun|10th june|10 june|10 jun|11th june|11 june|11 jun|12th june|12 june|12 jun|13th june|13 june|13 jun|14th june|14 june|14 jun|15th june|15 june|15 jun|16th june|16 june|16 jun|17th june|17 jun|17 june|18th june|18 june|18 jun|19th june|19 june|19 jun|20th june|20 june|20 jun",
       [gemini()]
       ],
      [r"cancer|CANCER|21st june|21 june|21 jun|22nd june|22 jun|22 june|23 june|23 jun|23rd june|24th june|24 june|24 jun|25th june|25 june|25 jun|26th june|26 june|26 jun|27th june|27 june|27 jun|28th june|28 june|28 jun|29th june|29 june|29 jun|30th june|30 june|30 jun|1st july|1 july|2nd july|2 july|3rd july|3 july|4th july|4 july|5th july|5 july|6th july|6 july",
       [cancer()]
       ],
      [r"7th july|7 july|8th july|8 july|9th july|9 july|10th july|10 july|11th july|11 july|12th july|12 july|13th july|13 july|14th july|14 july|15th july|15 july|16th july|16 july|17th julu|17 july|18th july|18 july|19th july|19 july|20th july|20 july|21st july|21 july|22 july|22nd july",
       [cancer()]
       ],
      [r"Leo|LEO|23rd july|23 july|24th july|24 july|25th july|25 july|26th july|27th july|27 july|28th july|28 july|29th july|29 july|30th july|30 july|31st july|31 july|1st august|1 aug|1 august|2nd august|2 aug|2 august|3rd august|3 aug|3 august|4th august|4 aug|4 august|5th august|5 aug|5 august|6th august|6 august|6 aug|7th august|7 august|7 aug|8th august|8 august|8 aug",
       [leo()]
       ],
      [r"8th august|8 aug|8 august|9th august|9 aug|9 august|10th auggust|10 aug|10 august|11th august|11 august|11 aug|12th august|12 august|12 aug|13th august|13 august|13 aug|14th august|14 aug|14 august|15th august|15 aug|15th august|16th august|16 aug|16 august|17th august|17 august|17 aug|18th august|18 aug|18 august|19 august|19th august|19 aug|20th august|20 aug|20 august",
       [leo()]
       ],
      [r"Virgo|VIRGO|23rd august|23 august|23 aug|24th august|24 aug|24 august|25th august|25 aug|25 august|26 august|26th august|26 aug|27th august|27 august|27 aug|28th august|28 aug|28 august|29th august|29 aug|29 august|30th august|30 aug|30th august|31st august|31 august|31 aug|1st september|1 september|1 sep|2nd september|2 sep|2 september",
       [virgo()]
       ],
      [r"3rd September|3 september|3 sep|4th september|4 sep|4 september|5th september|5 september|5 sep|6th september|6 september|6 sep|7th september|7 september|7 sep|8th september|8 sep|8 september|9th september|9 september|9 sep|10th september|10 sep|10 september|11th september|11 september|11 sep|12th september|12 september|12 sep",
       [virgo()]
       ],
      [r"13th september|13 sep|13 september|14th september|14 sep|14 september|15th september|15 sep|15 september|16th september|16 sep|16 september|17th september|17 sep|17 septemmber|18th sep|18th september|18 september|19th september|19 sep|19 september|20th september|20 sep|20 september|21st september|21 sep|21 september|22nd september|22 sep|22 september",
       [virgo()]
       ],
      [r"libra|LIBRA|23rd september|23 sep|23 september|24th september|24 sep|24 september|25th september|25 sep|25 september|26th september|26 september|26 sep|27 sep|27 september|27th september|28th september|28 sep|28 september|29th september|29 sep|29 september|30th september|30 sep|30 september|31st september|31 september|31 sep",
       [libra()]
       ],
      [r"1st october|1 oct|1 october|2nd october|2 oct|2 october|3rd october|3 october|3 oct|4th october|4 october|4 oct|5th october|5 oct|5 october|6th october|6 october|6 oct|7th october|7 october|7 oct|8th october|8 oct|8 october|9th october|9 oct|9 october|10th october|10 oct|10 october|11th october|11 oct|11 october|12th october|12 oct|12 october",
       [libra()]
       ],
      [r"13th october|13 oct|13 october|14th october|14 oct|14 october|15th october|15 oct|15 october|16th october|16 oct|16 october|17th october|17 october|17 oct|18th october|17 oct|17 october|18th october|18 oct|18 october|19th october|19 oct|19 october|20th october|20 oct|20 october|21st october|21 oct|21 october|22nd october|22 oct|22 october",
       [libra()]
       ],
      [r"scorpio|SCORPIIO|23rd october|23 oct|23 october|24th october|24 oct|october|25th october|25 oct|25 october|26th october|26 oct|26 october|27th october|27 oct|27 october|28th october|28 october|28 oct|29th october|29 oct|29 october|30th october|30 oct|30 october|31st october|31 ost|31 october|1st november|1 nov|1 november",
       [scorpio()]
       ],
      [r"2nd november|2 nov|2 november|3rd november|3 nov|3 november|4th november|4 november|4 nov|5th november|5 nov|5 november|6th november|6 nov|6 november|7th november|7 november|7 nov|8th november|8 nov|8 november|9th november|9 nov|9 november|10th november|10 nov|10 november|11th november|11 nov|11 november",
       [scorpio()]
       ],
      [r"12th november|12 nov|12 november|13th november|13 nov|13 november|14th november|14 november|14 nov|15th november|15 nov|15 november|16th november|16 nov|16 november|17th november|17 nov|17 november|18th november|18 nov|18 november|19 nov|19th november|19 november|20th november|20 nov|20 november",
       [scorpio()]
       ],
      [r"21st november|21 november|21 nov|22nd november|22 nov|22 november",
       [scorpio()]
       ],
      [r"sagittarius|SAGITTARIUS|23rdnovember|23 nov|23 november|24th november|24 nov|24 november|25th november|25 nov|25 november|26th november|26 nov|26 november|277th november|27 nov|27 november|28th november|28 nov|28 november|29th november|29 nov|29 november|30th november|30 nov|30 november",
       [capricorn()]
       ],
      [r"31st november|31 november|31 nov|1st december|1 dec|1 december|2nd december|2 dec|2 december|3rd december|3 december|3 dec|4th december|4 dec|4 december|5th december|5 dec|5 december|6th december|6 dec|6 december|7th december|7 dec|7 december|8th december|8 dec|8 december|9th december|9 dec|9 december",
       [sagittarius()]
       ],
      [r"10th december|10 dec|10 december|11th december|11 dec|11 december|12th december|12 december|12 dec|13th december|13 dec|13 december|14th december|14 dec|14 december|15th december|15 dec|15 december|16th december|16 dec|16 december|17th december|17 december|17 dec",
       [sagittarius()]
       ],
      [r"18th december|18 dec|18 december|19th december|19 dec|19 december|20th december|20 dec|20 december|21st december|21 dec|21 december",
       [sagittarius()]
       ],
        [r"CAPRICORN|capricorn|22nd december|22 dec|22 december|23rd december|23 dec|23 december|24th december|24 dec|24 december|25th december|25 dec|25 december|26th december|26 dec|26 december|27th december|27 dec|27 december|28th december|28 dec|28 december|29th december|29 dec|29 december|30th december|30 dec|30 december|31st december|31 dec|31 december",
[capricorn()]
],
        [r"1st january|1 jan|1 january|2nd january|2 jan|2 january|3rd january|3 jan|3 jauary|4th january|4 jan|4 january|5th january|5 jan|5 january|6th january|6 jan|6 january|7th january|7 jan|7 january|8th january|8 jan|8 january|9th january|9 jan|9 january|10th january|10 jan|10 january|11th january|11 jan|11 january|12th january|12 jan|12 january",
         [capricorn()]
         ],
        [r"13th january|13 jan|13 january|14th january|14 jan|14 january|15th january|15 jan|15 january|16th january|16 jan|16 january|17th january|17 jan|17 january|18th january|18 jan|18 january|19th january|19 jan|19 january",
         [capricorn()]
         ],
        [r"AQUARIUS|aquarius|20th january|20 jan|20 january|21st january|21 jan|21 january|22nd january|22 jan|22 january|23rd january|23 jan|23 january|24th january|24 jan|24 january|25th january|25 jan|25 january|26th january|26 jan|26 january|27th januray|27 jan|27 january|28th january|28 jan|28 january|29th january|29 jan|29 january",
         [aquarius()]
         ],
        [r"30th january|30 january|30 jan|31st january|31 january|31 jan|1st february|1 feb|1 february|2nd february|2 feb|2 february|3rd february|3 february|3 feb|4th february|4 feb|4 february|5th february|5 feb|5 february|6th february|6 feb|6 february|7th february|7 feb|7 february|8th february|8 feb|8 february|9th february|9 feb|9 february",
         [aquarius()]
         ],
        [r"10th february|10 feb|10 february|11th february|11 feb|11 february|12th february|12 feb|12 february|13th february|13 february|13 feb|14th february|14 feb|14 february|15th february|!5 feb|15 february|16th february|17th february|17 february|17 feb|18th february|18 feb|18 february|19th february|19 feb|19 february",
         [aquarius()]
         ],
        [r"PISCES|pisces|20th february|20 feb|20 february|21st february|21 feb|21 february|22nd february|22 feb|22 february|23rd february|23 feb|23 february|24th february|24 february|24 feb|25th february|25 feb|25 february|26th february|26 feb|26 february|27th february|27 feb|27 february|28th february|28 feb|28 february|29th february|29 feb|29 february",
         [pisces()]
         ],
        [r"1st march|1 mar|1 march|2nd march|2 mar|2 march|3rd march|3 mar|3 march|4th march|4 mar|4 march|5th march|5 mar|5 march|6th march|6 mar|6 march|7th march|7 mar|7 march|8th march|8 march|8 mar|9th march|9 mar|9 march|10th march|10 mar|10 march|11th march|11 march|11 mar|12th march|12 mar|12 march",
         [pisces()]
         ],
        [r"13th march|13 mar|13 march|14th march|14 mar|14 march|15th march|15 mar|15 march|16th march|16 mar|16 march|17th march|17 mar|17 march|18th march|18 mar|18 march|19th march|19 mar|19 march|10th march|20 mar|20 march",
         [pisces()]
         ],
[           [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def vbot():
    
        #default message at the start
    print('''
         Assalam.o.alaikum, 
        I'm a chatbot made by Misbah Shaukat.
        I have the speciality to tell you about your today's horoscope ;)
        Please type your date of birth in the format '4th november' to proceed
        OR you can directly tell you zoadic sign to get the info
        Note: The format is important otherwise the desired output will not come
        
        
        Type quit to leave ''')
    
    chat = Chat(chat_pairs, reflections)
    chat.converse()
vbot()
