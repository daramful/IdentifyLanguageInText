Author: Ginny Lee

Description: task is the problem of taking as input a text in an unknown language and determine what language it is written in. N-gram models are very effective solutions for this problem as well. I will be implementing no smoothing, add-one smoothing, and Good-Turing smoothing overall.
Language (version): Python 3.6.3 with GCC 4.2.1. Compatible Clang 4.0.1

First, download my file, and then move into the directory where my file "ling406_hlee295_hw2" is. Then go into the directory by entering "cd ling406_hlee295_hw2" on terminal.


To execute unsmoothed_letterLangId.py (no smoothing)
    - python unsmoothed_letterLangId.py

To execute letterLangId.py (With Add-one smoothing)
    - python letterLangId.py

To execute wordLangId.py  (With Add-one smoothing)
    - python wordLangId.py

To execute wordLangId2.py (with Good-Turing)
    - python wordLangId2.py


To read outputs of each execution, please go into the directory named "output". You will see the respective files for corresponsing executions above:
    - unsmoothed_letterLangId.out
    - letterLangId.out
    - wordLangId.out
    - wordLangId2.out

To execute comparison tests for each files, first go to the directory "Comparison" with command "cd Comparison".
Then execute comparison tests, same as below:
    - python ComparisonTest.unsmoothed_letter.py
    - python ComparisonTest.letter.py
    - python ComparisonTest.word.py
    - python ComparisonTest.word2.py

To see the comparisons output, please go into the directory named "Comparison" in directory "output". You will see the respective files for corresponsing executions above: 
    - Comparison.unsmoothed_letter.out
    - Comparison.letter.out
    - Comparison.word.out
    - Comparison.word2.out




(Q1)
How many times was your program correct?
Referring the very bottom line in a file name Comparison.letter.out (which holds how many lines were the same as LangId.test compared to smoothed letterLangId.py),
    - 298 Correct out of 300 lines
    - ...Which holds the equivalent value of 0.9933333333333333 for the probability 
As for unsmoothed_letterLangId.py, it was as the following on Comparison.unsmoothed_letter.py:
    - 299 Correct ouf of 300 lines
    - ...Which holds the equivalent value of 0.9966666666666667 for the probability


Can the letter bigram model be implemented without any kind of smoothing? Yes/no? What do you decide to do and why did you do it that way?
    I demonstrated that letter bigram model can be implemented without any kind of smoothing in "unsmoothed_letterLangId.py". Unsmoothed model is actually quite accurate in determining the language of the lines. However, in order to avoid zero-counts in the data (which is the same thing as having sparse data), I had to add a significant "insignificant value" of 1e-5 added to each Counts. 

    Therefore, I also submitted letterLangId.py with Laplace Smoothing (Add-one smoothing), which has one less correct determination of language, but does not get affected by sparse data.


To measure running time for letterLangId.py, I ran "time python letterLangId.py".
After identifying each line's possible determination of language, the report was as the following:
    - real    5m49.463s
    - user    5m40.264s
    - sys     0m3.414s



(Q2)
How many times was your program correct?
I used add-one smoothing to avoid zero-counts in the data as instructed.
Referring the very bottom line in a file name Comparison.word.out (which holds how many lines were the same as LangId.test),
    - 293 Correct out of 300 lines
    - ...Which holds the equivalent value of 0.9766666666666667 for the probability

To measure running time for wordLangId.py, I ran "time python wordLangId.py".
After identifying each line's possible determination of language, the report was as the following:
    - real    3m37.919s
    - user    3m24.449s
    - sys     0m1.881s



(Analysis from Q1 and Q2)
Which language model at Question#1, Question#2 is the best? Comment on advantages and disadvantages of these language models on the task. 
    If I were to look at the correct determination of languages only, I would say letterLangID.py with add-one smoothing technique, since letterLangID.py had 5 more lines correct compared to wordLangId.py model. However, if we were also to look at the running time of each model, wordLangId.py had significantly shorter running time to determine the result. (For your information, while letterLangID.py required almost 6 minutes to go through all 300 lines, wordLangId.py required only a little over 3 minutes and 30 seconds.) Also, while letters had much more variations to study from 300 lines, there were only limited words that were used in respective languages in comparison. This could have affected why wordLangId.py had less corrected results.

    For a different scenario, instead of having 300 lines, if we had to decode 1000 pages of international languages, wordLangId.py can be a better model to use since they would have more sophisticated and used languages, while reducing the time. Therefore, I would like to say the model from Question#2, wordLangId.py, would better for a long article, while letterLangId.py would be better for a shorter article.





(Q3/Extra Credit)
I replaced the add-one smoothing technique with Good Turing Discounting technique, in particular where I used Simple Good Turing method from textbook. 


How many times was your program correct?
I used add-one smoothing to avoid zero-counts in the data as instructed.
Referring the very bottom line in a file name Comparison.word2.out (which holds how many lines were the same as LangId.test),
    - 297 Correct out of 300 lines
    - 0.99 probability

To measure running time for wordLangId2.py, I ran "time python wordLangId2.py".
after identifying each line's possible determination of language, the report was as the following:
    - real    22m32.340s
    - user    22m1.113s
    - sys     0m14.675s

Which language model at Question#1, Question#2, and Question#3 is the best? Comment on advantages and disadvantages of these language models on the task. 
    If we were to observe wordLangId.py with add-one smoothing and wordLangId2.py with Good-Turing smoothing, I would say Good-Turing smoothing would be a better model to determine a result to identify the language origin of the sentences. Although running time of wordLangId2.py is 7 times of what wordLangId.py is, It returns higher probability of returning correct result by 0.01333333333 for this scenario. However, with the scenario where we have to decode 1000 pages of international lines, that will be so many lines. Therefore, I would say to decode incredibly many lines, use Good-Turing smoothing with wordLangId2.py from Question 3. However, if there is a high time-restrains to decode (e.g. deadline to report the country origin of international sentences is in 10 minutes), wordLangId.py from Question 2 is highly recommended. However, if the article is not 1000 pages, but if the size of the article is similar to the size of our LangId.test file, then letterLangId.py from Question 1 would be more recommended.
