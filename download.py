import json
import csv
import pandas as pd
from nltk.corpus import stopwords
EngStopWords = set(stopwords.words('english'))

f1=open('book_abstract.txt','a')
f2=open('book_abstract_num.txt','a')
f_t=open('rec.txt','a')

def load_data(file_name, head=400):
    count = 0
    data = []
    with open(file_name) as fin:
        for l in fin:
            d = json.loads(l)
            count += 1
            data.append(d)
            # break if reaches the 100th line
            if (head is not None) and (count > head):
                break
    return data
books = load_data('goodreads_books.json')
print(books[0].keys())

count=0
for each in range(200):
    content=books[each]['description']
    idnum=books[each]['book_id']
    num_rating=books[each]['ratings_count']
    if content!='':
        count += 1
        f2.write(idnum)
        f2.write(' ')
        f2.write(str(count))
        f2.write('\n')
        f1.write(num_rating)
        f1.write(' ')
        for word in content.split():
            if word in EngStopWords:
                pass
            else:
                f1.write(word)
                f1.write(' ')
        f1.write('\n')
f1.close()
f2.close()

for each in range(200,400):
    content=books[each]['description']
    idnum=books[each]['book_id']
    if content!='':
        f_t.write(idnum)
        f_t.write(' ')
        for word in content.split():
            if word in EngStopWords:
                pass
            else:
                f_t.write(word)
                f_t.write(' ')
        f_t.write('\n')

with open('goodreads_interactions.csv') as fileObject:
    reader_obj = csv.reader(fileObject)
    list0=[]
    i=0
    for row in reader_obj:
        if i!=0:
            list0.append(map(int,row))
        else:
            list0.append(row)
        i+=1
        if i==1000:
            break
    df=pd.DataFrame(list0[1:],columns=list0[0])
    df0=df.loc[(df['user_id']==0) & (df['is_read']==1)&(df['is_reviewed']==1)]


list1=list(df0['book_id'])
list2=list(df0['rating']) 
person_book_id=[]

with open('book_id_map.csv') as fileObject1:
    reader_obj1 = csv.reader(fileObject1)
    next(reader_obj1, None)
    c=0
    diction={}
    for i in reader_obj1:
        diction[int(i[0])]=int(i[1])
        c+=1
        if c==10000:
            break
    for each in list1:
        person_book_id.append(diction[each])

f2=open('book_abstract_num.txt','r')
f3=open('person_profile_num.txt','a')
Lines=f2.readlines()


for each in person_book_id:
    indexing=0
    for lines in Lines:
        k=int((lines.split())[0])
        if each==k:
            f3.write(lines.rstrip('\n'))
            f3.write(' ')
            f3.write(str(list2[indexing]))
            f3.write('\n')
    indexing+=1
f2.close()
f3.close()
f_t.close()
