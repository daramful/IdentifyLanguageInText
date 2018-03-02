Comparison_out = open('../output/Comparison/Comparison.letter.out', 'a')

with open('../lib/LangId.sol', 'r') as file1:
    with open('../output/letterLangId.out', 'r') as file2:
        same = set(file1).intersection(file2)

with open('../output/Comparison/Comparison.letter.out', 'w') as file_out:
    for line in same:
        file_out.writelines(line)


All = sum(1 for line in open('../lib/LangId.sol')) 
Correct = sum(1 for line in open('../output/Comparison/Comparison.letter.out'))
Comparison_out.writelines(str((Correct))+ " Correct out of " + str(All) + " lines\n")
Comparison_out.writelines(str(float(Correct/All))+ " probability")
