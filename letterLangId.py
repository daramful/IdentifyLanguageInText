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


''' Above codes are given already '''
#variation of file2bigrams (for words) to file2letters (for letters)
def file2letters(filename):
    return bigrams(list(open(filename).read()))

# Laplace Smoothing (Add-one smoothing)
# Maximum_Likelihood_Estimates
def letters_MLE(input_str, counts):
    total_prob = 0
    letters = list(input_str)  # splits letters
    
    for (k_1, k_2) in zip([None] + letters, letters + [None]):
        bigram = counts[k_1][k_2]  # := Count(W_(n-1)*W_(n))
        unigram = sum(counts[k_1].values())  # := Count(W_(n-1))
        V = len(counts)

        prob = float(bigram + 1)/(unigram + V)
        # We do everything in log space
        total_prob = total_prob + math.log(prob)
    return total_prob


# Source from https://stackoverflow.com/questions/12755587/using-python-to-write-specific-lines-from-one-file-to-another-file
# output of word/letter bigrams will be printed here
letter_sol = open('output/letterLangId.out', 'a')
#number of lines
num_lines = sum(1 for line in open('lib/LangId.test')) 

# line number: https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def output_print():
    i = 1       #initial line number
    while (i != num_lines+1):
        for line in open('lib/LangId.test').readlines():
            english_letter = letters_MLE(line, file2letters("lib/LangId.train.English"))
            french_letter = letters_MLE(line, file2letters("lib/LangId.train.French"))
            italian_letter = letters_MLE(line, file2letters("lib/LangId.train.Italian"))

            '''print("english: ", english_letter)
            print("french: ", french_letter)
            print("italian: ", italian_letter)'''
            letter_mostly_likely = max(english_letter, french_letter, italian_letter)
            if letter_mostly_likely == english_letter:
                with open('lib/LangId.test'):
                    letter_sol.writelines(str(i) + " English\n")
            elif letter_mostly_likely == french_letter:
                with open('lib/LangId.test'):
                    letter_sol.writelines(str(i) + " French\n")
            elif letter_mostly_likely == italian_letter:
                with open('lib/LangId.test'):
                    letter_sol.writelines(str(i) + " Italian\n")
            
            if (i < num_lines+1):
                print("letter ", i)
            
            #increment to finish while loop
            i+=1


output_print()
