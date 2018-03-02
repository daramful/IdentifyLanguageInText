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