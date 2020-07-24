#!/usr/bin/python3

import wikipedia

# getting user input
topic = input("\nPlease type a topic that you would like to search on the wiki: ")

# setting number of sentaces to return.
result = wikipedia.summary(topic, sentences = 15)

# printing result.
print("\n RESULT: \n \n" + result + "\n")


