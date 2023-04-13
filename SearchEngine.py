'''
Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input 
from the user. You have to pull out the sentences matching this query inputted by the user in 
decreasing order of relevance after converting every word in the query and the sentence to lowercase. 
The most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:

Please input your query string
“Python is”

Output:

3 results found:
    python is not python snake
    python is good
    Python is cool
'''

#Importing Required Modules
from collections import OrderedDict
import numpy as np
import time

#Data
sentences_list = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a popular programming language",
    "I love listening to music while I work",
    "The sun rises in the east and sets in the west",
    "The internet is a vast and complex network of computers",
    "Life is like a box of chocolates, you never know what you're gonna get",
    "The sky is a beautiful shade of blue today",
    "I enjoy playing video games in my free time",
    "Reading is one of my favorite hobbies",
    "My favorite color is green",
    "I always try to stay positive and focus on the good things in life",
    "Coffee is my go-to beverage when I need a pick-me-up",
    "Dogs are known for their loyalty and companionship",
    "Cats are independent creatures that like to do things on their own terms",
    "I believe that honesty is the best policy",
    "The world is a fascinating and ever-changing place",
    "I love spending time outdoors, especially in nature",
    "The universe is vast and full of wonders",
    "I enjoy trying new things and exploring different cultures",
    "I believe that everyone deserves to be treated with kindness and respect",
    "Laughter is the best medicine",
    "I'm always looking for ways to improve myself and learn new things",
    "The internet has made it easier than ever to connect with people from all over the world",
    "I believe that we should all do our part to help protect the environment",
    "Traveling is one of the best ways to broaden your horizons and gain new perspectives",
    "The ocean is full of mystery and wonder",
    "I'm grateful for all of the wonderful people in my life",
    "The sky is a canvas that is always changing and evolving",
    "I love to cook and experiment with new recipes",
    "Hard work and perseverance are key to achieving your goals",
    "The human brain is an amazing and complex organ",
    "I believe that a positive attitude can make all the difference",
    "Education is the key to unlocking your full potential",
    "The future is full of endless possibilities",
    "I'm always inspired by people who follow their dreams and pursue their passions",
    "The natural world is full of beauty and wonder",
    "I believe that we should all strive to make a positive difference in the world",
    "The power of love and compassion can change lives",
    "Learning a new language can open up a whole new world of opportunities",
    "The stars in the night sky are a reminder of how vast and mysterious the universe is",
    "I believe that everyone has something valuable to contribute to the world",
    "Perfection is a journey, not a destination",
    "The internet has revolutionized the way we communicate and access information",
    "I love spending time with my friends and family",
    "Music has the power to lift our spirits and soothe our souls",
    "The natural world is full of wonders that we have yet to discover ",
    "I'm always amazed by the resilience of the human spirit",
    "Life is too short to waste time on things that don't matter",
    "The power of imagination can take us anywhere we want to go",
    "I believe that every experience, good or bad, has something to teach us",
    "The world is full of diverse cultures and traditions that are worth exploring",
    "I always try to find the silver lining in every situation",
    "Technology has made our lives easier in so many ways",
    "I believe that we should all strive"
]

#Declaring the variables
relevent_sentences = [ ]
relevent_words_num = [ ]
final_search_dict = { }

#Input
search_query = input("\nEnter the word that you wanna search :: ")
search_query = search_query.lower()

initial = time.time()
#Separating the revelent sentences form data
for items in sentences_list:
    words = items.split()
    for objects in words:
        objects = objects.lower()
        if (objects==search_query):
            relevent_sentences.append(items)
            break

#Calculating how many times the search_query is present in one relevent sentence
for items in relevent_sentences:
    a = 0
    words = items.split()
    for objects in words:
        objects = objects.lower()
        if(objects==search_query):
            a = a+1
    #Storing both the times and relevent sentence in dict
    final_search_dict.update({f"{items}":a})

#Sorting the list on the basis of times of search_query in the relevent sentences
keys = list(final_search_dict.keys())
values = list(final_search_dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

#Displaying how many results were found in how much time
times = 0
for items in relevent_sentences:
    times = times + 1
print(f"\nAbout {times} searches in {time.time()-initial} seconds \n")

if(times==0):
    print("No searches found . Please check if your word or spelling is wrong or not :( \n")
    exit()
#Iterating the dict from backward
for c in reversed(sorted_dict):
    print(f"\t → {c}.");
print("\n")