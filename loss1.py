import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt
f=open('person_profile.txt')
x=[]
y=[]
for each in f:
    temp=[]
    vector=each.split()
    y.append(int(vector[0]))
    for i in vector[1:]:
        temp.append(float(i))
    x.append(temp)

clf=linear_model.Lasso(alpha=0.02,normalize=False,max_iter=3000)
clf.fit(x,y)
cof1=clf.coef_



