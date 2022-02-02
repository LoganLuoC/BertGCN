
data = ""
with open('data/label.txt','r') as fr:
    index = 0
    for line in fr.readlines():
        if index > 15000:
            data += "%d\ttest\t%s" %(index, line)
        else:
            data += "%d\ttrain\t%s" %(index, line)
        index += 1
    print(data)
    

with open('data/label.txt','w') as fw:
    fw.write(data)