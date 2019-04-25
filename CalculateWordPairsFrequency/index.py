### 问题 ###
# 要把同一篇论文里出现的关键词配对统计比如（a,b,c）配成（a,b）（a,c）（b,c），然后统计期刊里所有论文配对关键词相同的数量。

### 解决思路 ###
# 1、将这篇论文和期刊所有其它论文的词频的统计结果分别拿来组合成词对的字典列表:
# 字典的列表A（[{word1:m次,word2:n次},...]）和字典的列表Bn(B1=[{word3:i次,word4:j次},...]、B2=[{word5:k次,word6:l次},...]、...)
# （这样是为了避免重复词和其它词组合成重复的词对）；
# 2、分别用字典的列表A和字典的列表Bn 一一进行比较，从Bn取出相同组合词对组合Cn (C1=[{word7:o次,word8:p次},...]，词对出现的次数为Max(o,p)，即o和p中较大数值为该词对的出现次数)

### 通过这个问题学到的，可忽略，嘿嘿 ###
# 1、拿到复杂的问题通过思考进行充分的分析，分析的基本原则是分解问题，将复杂问题分解为一个一个简单的小问题；
# 2、在提出问题、分析问题和解决问题中，自认为分析问题是最关键的，也是最体现能力的，不过其它两个也是不可或缺的；

message = input("请输入要查询两个关键词同时出现在一篇论文次数的文档名称：")
message += '.txt'

counts = {}
list1 = []
list2 = []
filename = 'jieguo2.txt'
with open(message)as file_object:
    for line in file_object.readlines():
        line = line.strip('\n')
        words = line.split(';')

        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                # 把两个词放在列表里，如['1 2','2 3','2 1','5 6']
                list1.append(words[i]+' '+words[j])
                # 刚好和list1相反['2 1','3 2','1 2','6 5']
                list2.append(words[j]+' '+words[i])
print(list1)
print(list2)
for keyword_1 in list1:
    if keyword_1 in counts:
        counts[keyword_1] += 1
        for m in range(0, len(list1)):
            for n in range(0, len(list2)):
                if list1[m] == list2[n]:  # 如上边说的例子，list1[0]==list2[2],就把list1[2]删掉并给list1[0]计数加1
                    counts[keyword_1] += 1
                    del counts[n]

    else:
        counts[keyword_1] = 1

print(counts)
