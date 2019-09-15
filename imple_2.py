import os
import operator
import math
wordDic = dict()
tfDic = dict()
idfDIc = dict()
count = 0

def makeList(line):
    takeLine = []
    for text in line:
        word = text.split('\t')[-1]
        splitWord = word.split('+')
        for word2 in splitWord:
            word2 = "".join(word2.split())
            word3 = word2.split('/')
            if len(word3) == 2:
                if word3[1] == 'NNG' or word3[1] == 'NNP':
                    takeLine.append(word3[0] + '/' + word3[1])
    return takeLine

for (path, dir, files) in os.walk("C:\\Data_Mining\\Corpus\\Input_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            f = open(path + "\\" + filename, "r", encoding="UTF8")
            count += 1
            listedWord = makeList(f.readlines())
            for word in listedWord:
                if word not in wordDic:
                    wordDic[word] = 1
                else:
                    wordDic[word] += 1
            f.close()

sortedFirst = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)
tempList = []
for i in range(0, 5024):
    data = sortedFirst[i]
    tempList.append(data[0])

# IDF 5024개
for (path, dir, files) in os.walk("C:\\Data_Mining\\Corpus\\Input_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.txt':
            f = open(path + "\\" + filename, "r", encoding="UTF8")
            listedWord = list(set(makeList(f.readlines())))
            for word in listedWord:
                if word in tempList:
                    if word not in idfDIc:
                        idfDIc[word] = 1
                    else:
                        idfDIc[word] += 1
            f.close()

# 로그
keyList = idfDIc.keys()
for key in keyList:
    idfDIc[key] = float(format(math.log10((count / idfDIc[key])), '.4f'))

# Input Data
for (path, dir, files) in os.walk("C:\\Data_Mining\\Corpus\\Input_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        folder = "".join(path).split('\\')[-1]
        if ext == '.txt':
            f = open(path + "\\" + filename, "r", encoding="UTF8")
            listedWord = makeList(f.readlines())
            for word in listedWord:  # 문서 전체 단어
                if word in tempList:  #5024개 안에 단어가 있으면
                    if word not in tfDic:
                        tfDic[word] = 1
                    for wordTf in listedWord:
                        if word is wordTf:
                            tfDic[word] += 1
                        keyList = tfDic.keys()
            tf_idf = dict()
            nmlzation = dict()
            tfIdfSum = 0
            for key in keyList:
                value = float(format(math.log10(tfDic[key]), '.4f'))
                tf_idf[key] = float(format(idfDIc[key] * value, '.4f'))
                tfIdfSum += pow(float(format(idfDIc[key] * value, '.4f')), 2)
            for key in keyList:
                tf_idf[key] = format(tf_idf[key] / math.sqrt(tfIdfSum), '.4f')
            tf_idf_sorted = sorted(tf_idf.items())
            f = open("C:\\Data_Mining\\201433718_홍건수\\Input_Data" + '\\' + folder + '\\' + filename, "w")
            for i in range(0, len(tf_idf_sorted)):
                data = tf_idf_sorted[i]
                f.write(data[1] + '\t')
                tfDic.clear()
            tf_idf.clear()


for (path, dir, files) in os.walk("C:\\Data_Mining\\Corpus\\Test_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        folder = "".join(path).split('\\')[-1]
        if ext == '.txt':
            f = open(path + "\\" + filename, "r", encoding="UTF8")
            listedWord = makeList(f.readlines())
            for word in listedWord:
                if word in tempList:
                    if word not in tfDic:
                        tfDic[word] = 1
                    for wordTf in listedWord:
                        if word is wordTf:
                            tfDic[word] += 1
            keyList = tfDic.keys()
            tf_idf = dict()
            nmlzation = dict()
            tfIdfSum = 0
            for key in keyList:
                value = float(format(math.log10(tfDic[key]), '.4f'))
                tf_idf[key] = float(format(idfDIc[key] * value, '.4f'))
                tfIdfSum += pow(float(format(idfDIc[key] * value, '.4f')), 2)
            for key in keyList:
                tf_idf[key] = format(tf_idf[key] / math.sqrt(tfIdfSum), '.4f')
            tf_idf_sorted = sorted(tf_idf.items())
            f = open("C:\\Data_Mining\\201433718_홍건수\\Test_Feature_Data" + '\\' + folder + '\\' + filename, "w")
            for i in range(0, len(tf_idf_sorted)):
                data = tf_idf_sorted[i]
                f.write(data[1] + '\t')
                tfDic.clear()
            tf_idf.clear()

for (path, dir, files) in os.walk("C:\\Data_Mining\\Corpus\\Val_Data"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        folder = "".join(path).split('\\')[-1]
        if ext == '.txt':
            f = open(path + "\\" + filename, "r", encoding="UTF8")
            listedWord = makeList(f.readlines())
            for word in listedWord:
                if word in tempList:
                    if word not in tfDic:
                        tfDic[word] = 1
                    for wordTf in listedWord:
                        if word is wordTf:
                            tfDic[word] += 1
            keyList = tfDic.keys()
            tf_idf = dict()
            nmlzation = dict()
            tfIdfSum = 0
            for key in keyList:
                value = float(format(math.log10(tfDic[key]), '.4f'))
                tf_idf[key] = float(format(idfDIc[key] * value, '.4f'))
                tfIdfSum += pow(float(format(idfDIc[key] * value, '.4f')), 2)
            for key in keyList:
                tf_idf[key] = format(tf_idf[key] / math.sqrt(tfIdfSum), '.4f')
            tf_idf_sorted = sorted(tf_idf.items())
            f = open("C:\\Data_Mining\\201433718_홍건수\\Val_Feature_Data" +'\\' + folder + '\\' + filename, "w")
            for i in range(0, len(tf_idf_sorted)):
                data = tf_idf_sorted[i]
                f.write(data[1] + '\t')
                tfDic.clear()
            tf_idf.clear()