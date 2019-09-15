import os
import re
import string
f = open("C:\Corpus\output.txt", 'w')
from collections import Counter
wordDict = Counter()
for (path, dir, files) in os.walk("C:\Corpus\Input_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            print("%s/%s" % (path, filename))
            with open(path + "\\" +filename, "r", encoding = 'UTF8') as fILE:
                while True:
                    sentences = fILE.readlines()
                    for sentence in sentences:
                        for word in sentence.split():
                            for word2 in sorted(word.split("+")):
                                if word2.__contains__("NNG") or word2.__contains__("NNP"):
                                    wordDict[word2] += 1
                    if not sentences: break
sorted_dict = sorted(wordDict.items(), key=lambda x: (-x[1], x[0]))
for(word, occ)in sorted_dict[:5024]:
    #print(word, '\t', occ)
    f = open("C:\Corpus\output.txt", 'a')
    str_in = word+ "    "+occ.__str__()+'\n'
    f.write(str_in)
f.close()