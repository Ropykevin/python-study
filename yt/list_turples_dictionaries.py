#---list---
# a list can be defined as a collection of objects,values,or items of different types
List1=[1,'adam',107,'usa']
# reverse index from right starts with -1
# from left starts with 0

    #extics of lists
#=>they are ordered
#=>they can store various types of elements
#=>they can be accessed by index
#=>they are mutable
#=>they allow duplicate elements

# method of list
List1=[1,'adam',107,'usa']
#.append(elem to be added)
List1.append(254)
print(List1)#[1,'adam',107,'usa',254]
#.insert(index,elem to be inserted)
List1.insert(1,"uganda")
print(List1)#[1,"uganda'adam',107,'usa',254]
#.extend(another list)//use to compine different lists
List2=[10,20,30,40,50]
List1.extend(List2)#adds list 2 to list one in an odered manner
print(List1)#[1,"uganda'adam',107,'usa',254,10,20,30,40,50]
#.index(elem) returns the index of the first element with thw specified value
print(List1.index("uganda"))# 1
#.remove(elem)removes the specified element from the list
List1.remove("uganda")
print(List1)#[1, 'adam', 107, 'usa', 254, 10, 20, 30, 40, 50]
#.sort()use to sort the list
# List1.sort()
# print(List1)#works on one thype of list
#.reverse()reverses the oder of the list
List1.reverse()
print(List1)
#nested lists
list3=['apple','orange',['one','two','three','four','ke',],'banana','kiwi']
# to access 8
print(list3[2][4])#ke

#slice in python (:)slice operator
print(list3[1:3])#[1, 'adam', 107, 'usa', 254, 10, 20, 30, 40, 50]
print(list3[2::2])#[['one', 'two', 'three', 'four', 'ke'], 'kiwi']

#.pop(index)
print(list3.pop(1))#orange
print(list3)#['apple', ['one', 'two', 'three', 'four', 'ke'], 'banana', 'kiwi']

# .clear() clears/del the list
list3.clear()
print(list3)#[] empty list

# .count (counts the elements in the list)
print(list3.count("adam"))#0 because we already cleared

#---------tuples-------
# a tuples can be defined as a collection of objects,values,or items of different types
#use of ()
Tup1=(1,'adam',107,"usa")
# reverse index from right starts with -1
# from left starts with 0

#---extics of tuples--
#=>tuples are ordered
#=>tuples can be accessed by index
#=>tuples can store various types of elements
#=>tuples are immutable
#=>tuples allow duplicate elements

# -------methods in tuples----
tup1=("apple","orange","banana","kiwi")
print(tup1)#('apple', 'orange', 'banana', 'kiwi')

#index
      #forward
print(tup1[0])#apple
 #   reversed
print(tup1[-1])#kiwi

#slicing
print(tup1[1:3])#('orange', 'banana')

#concatenation

#repetition ("repeat",)*3
print((tup1)*3)
#('apple', 'orange', 'banana', 'kiwi',
# 'apple', 'orange', 'banana', 'kiwi',
# 'apple', 'orange', 'banana', 'kiwi')

#count tuplename.count(elem to be counted)
print(tup1.count("apple"))#1

# index fetching (turple name.index("element"))
print(tup1.index("banana"))#2

#append method
y =list(tup1)#convert to list
y.append("quava") #append
tup1=tuple(y)#convert to tuples
print(tup1)#print ==('apple', 'orange', 'banana', 'kiwi', 'quava')

# executing loops in tuples
for x in tup1:
    print(x) 
    # apple
    # orange
    # banana
    # kiwi
    # quava;
#  dictionaries
# a dictionary can be defined as a collection of objects,values,or items of different types
#STORED IN KEY VALUE-PAIR FORMAT
# enclosed within the curly braces{}
# each key is separated by the colon (:)
Dict1={'a':1,'b':2,'c':3}
#a,b and c are keys 
# 1,2,3 are values

    #extics of dictionaries
#=>dictionaries are ordered 
#=>dictionaries can store various types of elements
#=>elements of dictionaries can not be accessed through index 
#=>dictionaries are mutable
#=>dictionaries does not allow duplicate elements 
dict1={1:'apple',2:'orang',3:'banana',4:'kiwi'}
print(dict1)
    #methods in Dictionaries

#get Dict1.get(keyname)returns values of a specified key
print(dict1.get(1))#apple

#keys Dict1.keys()returns the list containing the dictionaries keys
print(dict1.keys())#dict_keys([1, 2, 3, 4])
# pop Dict1.pop(keyname) removes elements with specified keys
print(dict1.pop(4))#kiwi
print(dict1)#{1: 'apple', 2: 'orang', 3: 'banana'}
#popitem Dict1.popitem() removes the last inserted key value pair in the dictionary
dict1.popitem()
print(dict1)#{1: 'apple', 2: 'orang'}
#length
print(len(dict1))#3

#sorted
print(sorted(dict1))#[1, 2, 3]
# .values
print(dict1.values())#dict_values(['apple', 'orang', 'banana'])

#update
dict1.update({2:'watermelon',3:'banana'})
print(dict1)#{1: 'apple', 2: 'watermelon', 3: 'banana'}
dict1.update({5:'muskmelon'})
print(dict1)#{1: 'apple', 2: 'watermelon', 3: 'banana', 5: 'muskmelon'}      
# loops in dictionaries
# for x in dict1:
#     print(dict1[x])

# for x,y in dict1.item():
#     print(x,y)

    #copy
mydict =dict1.copy()
print(mydict)#{1: 'apple', 2: 'watermelon', 3: 'banana', 5: 'muskmelon'}

#clear Dict1.clear()removes all element in a dictionary
dict1.clear()
print(dict1)#{}


ken =(1,2,3,4,5,6,7,8)
ken=list(ken)
print(ken)
del(ken[2:5])
print(ken)
ken=tuple(ken)
print(ken)
