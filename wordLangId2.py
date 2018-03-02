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
'''
Good-Turing Method
Idea: re-estimate probability mass assigned to N-grams with zero counts
G-T = c∗(wn-1,wn) / C(wn−1)

'''
#Frequency of how many same "count" occured in a series
'''
def freq_of_freq(counts, freq):
the number of N-grams that occur c times
'''
def freq_of_freq_x(counts, freq):
    return sum(1 for c in counts.values() for i in c.values() if i == freq )


def total_bigram_count(filename):
    return (len(open(filename).read().split())-1)**2

'''
Variables explanation
#N = Number of values of bigrams species "seen"
#MLE count for GT = c.
#c* = is a smoothed count

We are going to use "Simple Good-Turing" in order to compute for undefined cases where N_c+1 = 0 for the last N_c. 
i.e. if N_4 = 0, it would be impossible to compute N_3 with Good-Turing.
'''
#Katz (1987) suggests settings K at 5. 
K = 5

def good_turing_MLE(input_str, filename):
    total_prob = 0
    words = input_str.split()
    counts = file2bigrams(filename)
    N =total_bigram_count(filename)
    #K+1 to iterate until the last counts, and another +1, since without it, that last count won't be in the range
    N_counts = [freq_of_freq_x(file2bigrams(filename), x) for x in range(1, (K+1)+1)]

    for (k_1, k_2) in zip([None] + words, words + [None]):
        #bigram = counts[k_1][k_2]
        unigram = sum(counts[k_1].values())
        C = counts[k_1][k_2]            #for notation for GT formula, although it's same as "bigram" above, I set it also equal to C

        if (counts.values == 0):
            print("There does not exist any count")
        if (C <= K):
            #For the occurence with C = 0; slide 58 of lecture 4
            if C == 0:
                N_1  = N_counts[0]
                #missing mass
                prob = float(N_1)/(N)   
            else:
                #notations for the corrected equation for C_star when some k is introduced
                N__c_plus_1 =  N_counts[C]         # Nc+1
                N__c = N_counts[C - 1]             # Nc                
                N__k_plus_1 = N_counts[K]               # Nk+1
                N_1 = N_counts[0]                       # N1
                
                # new disocunted bigram count: c*
                C_star = (((C + 1) * float(N__c_plus_1 / (N__c))) - (C*(float(K + 1) * ((N__k_plus_1) / (N_1))))) / (1-(float(K + 1) * ((N__k_plus_1) / (N_1))))
                prob = float(C_star)/(unigram)
        else:
            prob = float(C)/(unigram)
            
        # We do everything in log space & @71 from Piazza
        total_prob += math.log(prob)
        
    return total_prob


# Source from https://stackoverflow.com/questions/12755587/using-python-to-write-specific-lines-from-one-file-to-another-file
# output of word/letter bigrams will be printed here
word_sol = open('output/wordLangId2.out', 'a')
#number of lines
num_lines = sum(1 for line in open('lib/LangId.test')) 
fileEng = ("lib/LangId.train.English")
fileFr = ("lib/LangId.train.French")
fileIt = ("lib/LangId.train.Italian")
# line number: https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def output_print():
    i = 1       #initial line number
    while (i != num_lines+1):
        for line in open('lib/LangId.test').readlines():
            english_word = good_turing_MLE(line, fileEng)
            french_word = good_turing_MLE(line, fileFr)
            italian_word = good_turing_MLE(line, fileIt)

            '''print("english: ", english_word)
            print("french: ", french_word)
            print("italian: ", italian_word)'''

            GT_word_mostly_likely = max(english_word, french_word, italian_word)
            if GT_word_mostly_likely == english_word:
                with open('lib/LangId.test'):
                    word_sol.writelines(str(i) + " English\n")
            elif GT_word_mostly_likely == french_word:
                with open('lib/LangId.test'):
                    word_sol.writelines(str(i) + " French\n")
            elif GT_word_mostly_likely == italian_word:
                with open('lib/LangId.test'):
                    word_sol.writelines(str(i) + " Italian\n")

            if (i < num_lines+1):
                print("GT words ", i)
            
            #increment to finish while loop
            i+=1

output_print()
