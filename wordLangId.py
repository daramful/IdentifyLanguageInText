#Author: Ginny Lee

from dicts import DefaultDict
import math as math
import numpy as np


def bigrams(words):
    """Given an array of words, returns a dictionary of dictionaries,
    containing occurrence counts of bigrams."""
    d = DefaultDict(DefaultDict(0))
    for (w1, w2) in zip([None] + words, words + [None]):
        d[w1][w2] += 1
    return d


def file2bigrams(filename):
    return bigrams(open(filename).read().split())

''' Above codes are given already '''
# Laplace Smoothing (Add-one smoothing)
# Maximum_Likelihood_Estimates
def words_MLE(input_str, counts):
    total_prob = 0
    words = input_str.split()  # splits words by spaces

    for (k_1, k_2) in zip([None] + words, words + [None]):
        bigram = counts[k_1][k_2]  # := Count(W_(n-1)*W_(n))
        unigram = sum(counts[k_1].values())  # := Count(W_(n-1))
        V = len(counts)

        prob = float(bigram + 1)/(unigram + V)
        # We do everything in log space & @71 from Piazza
        total_prob = total_prob + math.log(prob)
    return total_prob

# Source from https://stackoverflow.com/questions/12755587/using-python-to-write-specific-lines-from-one-file-to-another-file
# output of word/letter bigrams will be printed here
word_sol = open('output/wordLangId.out', 'a')
#number of lines
num_lines = sum(1 for line in open('lib/LangId.test')) 

# line number: https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def output_print():
    i = 1       #initial line number
    while (i != num_lines+1):
        for line in open('lib/LangId.test').readlines():
            english_word = words_MLE(line, file2bigrams("lib/LangId.train.English"))
            french_word = words_MLE(line, file2bigrams("lib/LangId.train.French"))
            italian_word = words_MLE(line, file2bigrams("lib/LangId.train.Italian"))

            '''print("english: ", english_word)
            print("french: ", french_word)
            print("italian: ", italian_word)'''

            word_mostly_likely = max(english_word, french_word, italian_word)
            if word_mostly_likely == english_word:
                with open('lib/LangId.test'):
                    word_sol.writelines(str(i) + " English\n")
            elif word_mostly_likely == french_word:
                with open('lib/LangId.test'):
                    word_sol.writelines(str(i) + " French\n")
            elif word_mostly_likely == italian_word:
                with open('lib/LangId.test'):
                    word_sol.writelines(str(i) + " Italian\n")

            if (i < num_lines+1):
                print("words ", i)
            
            #increment to finish while loop
            i+=1


output_print()
