import pickle

with open('my_list.pickle', 'rb') as file:
    newlist = pickle.load(file)

print(type(newlist))

for i in newlist:
    print(i)
