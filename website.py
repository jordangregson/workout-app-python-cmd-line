# Program for pickling python lists
# importing module
print('<-------------------Pickling----------------------->')
import pickle
# number of input data to take
n = int(input("Enter the number of items "))
data = []  # input list
# adding items to the list
for d in range(n):
    item = input("Enter data :" + str(d+1)+': ')
    data.append((item))
# open a file where data need to be stored
file = open('list.pkl', 'wb')
# dump information to the file
pickle.dump(data, file)
# close the file
file.close()
print('\n')
print('<-------------------Un-Pickling----------------------->')
# open the file where data is dumped
fileo = open('list.pkl', 'rb')
# loading data
datao = pickle.load(fileo)
# close the file
fileo.close()
# showing pickled data
print("showing data pickled")
for i in datao:
    print(i)