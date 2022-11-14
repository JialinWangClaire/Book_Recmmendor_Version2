from al4 import main
list0=[]
for i in range(5):
    list0.append(main())
print(list0)
print('books to be recommended:')
print(set.intersection(*[set(x) for x in list0]))

