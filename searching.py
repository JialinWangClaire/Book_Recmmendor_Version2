f3=open('person_profile_num.txt','r')
f4=open('person_profile.txt','a')
f=open('book_vector.txt','r')
f5=open('book_person.txt','a')


k=f.readlines()
lining=f3.readlines()
for each in lining:
    ind=int(each.split()[1])
    rating=each.split()[2]
    f4.write(rating)
    f4.write(' ')
    f5.write(k[ind-1])

    result=k[ind-1].split()[1:]
    result=' '.join(result)
    f4.write(result)
    f4.write('\n')

f.close()
f3.close()
f4.close()
f5.close()
