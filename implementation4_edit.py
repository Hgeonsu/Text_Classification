ansFile = open("answer.txt", "r", encoding="utf-8")
outFile = open("output.txt", "r", encoding="utf-8")
predArr = []
ansArr = []
lines = outFile.readlines()
ans = ansFile.readlines()
#각 라인마다 최대찾고, 그 문서 카테고리 값을 pre배열에 save
for line in lines:
    line = "".join(line).split()
    prbL = []
    for p in line:
        prbL.append(float(p))
    max_value = 0.0
    for p in prbL:
        if max_value < p:
            max_value = p
    predArr.append(prbL.index(max_value))

# 답을 저장할 리스트
for ans in ans:
    ans = "".join(ans).split()
    ansArr.append(int(ans[0]))

# 예측 = 정답 개수
crt = 0
for i in range(len(predArr)):
    if predArr[i] == ansArr[i]:
        crt += 1
print("- Accuracy: " + str(crt / len(ansArr)))

# 마크로, 마이크로
pre = [0 for i in range(9)]
tp = [0 for i in range(9)]
fp = [0 for i in range(9)]
fn = [0 for i in range(9)]
recl = [0 for i in range(9)]
totPre = 0
totRe = 0
totTp = 0
totFp = 0
totFn = 0
# 답이면 tp증가
# 틀리면 fp fn 증가
for i in range(len(predArr)):
    if predArr[i] == ansArr[i]:
        tp[predArr[i]] += 1
    else:
        fp[predArr[i]] += 1
        fn[ansArr[i]] += 1

# 마크로 F1
for i in range(len(tp)):
    pre[i] = tp[i] / (tp[i] + fp[i])
    recl[i] = tp[i] / (tp[i] + fn[i])
    totPre += pre[i]/9
    totRe += recl[i]/9
Macro_F1 = (2 * totPre * totRe) / (totPre + totRe)

# 마이크로 F1
for i in range(len(tp)):
    totTp += tp[i]
    totFp += fp[i]
    totFn += fn[i]
totPre = totTp / (totTp + totFp)
totRe = totTp / (totTp + totFn)
Micro_F1 = (2 * totPre * totRe) / (totPre + totRe)

print("- Macro-Averaging F1 = " + str(Macro_F1))
print("\n")
print("- Total Precision = " + str(totPre))
print("- Total Recall = " + str(totRe))
print("- Micro-Averaging F1 = " + str(Micro_F1))