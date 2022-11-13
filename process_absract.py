import numpy as np

f1=open('book_abstract.txt','r')
f2=open('book_vector.txt','a')
f3=open('glove.6B.50d.txt','r')
f4=open('book_vector_rec.txt','a')
f5=open('rec.txt','r')

dic3={}
for lines in f3:
    l=lines.split()
    word=l[0]
    list0=[]
    for each in l[1:]:
        list0.append(float(each))
    dic3[word]=np.array(list0)

for lines in f1:
    v=np.zeros(50)
    count = 0
    num=lines.split()[0]
    f2.write(num)
    f2.write(' ')
    for each in lines.split()[1:]:
        if each in list(dic3.keys()):
            v=v+dic3[each]
            count+=1
    if count!=0:
        v/=count
    for each in v:
        f2.write(str(each))
        f2.write(' ')
    f2.write('\n')

for lines in f5:
    v=np.zeros(50)
    num=lines.split()[0]
    count=0
    f4.write(num)
    f4.write(' ')
    for each in lines.split()[1:]:
        if each in list(dic3.keys()):
            v=v+dic3[each]
            count+=1
    if count!=0:
        v/=count
    for each in v:
        f4.write(str(each))
        f4.write(' ')
    f4.write('\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()



