from loss1 import cof1
from loss2 import cof2
import numpy as np
f=open('book_vector_rec.txt','r')
lines=f.readlines()
value=[]
for each in lines:
    value0=[]
    t=each.split()[1:]
    for i in t:
        value0.append(float(i))
    value.append(value0)

choice1=np.dot(np.array(value),np.array(cof1))
choice2=np.dot(np.array(value),np.array(cof2))
choice1=choice1*(-1)
choice2=(choice2+1000)/100
