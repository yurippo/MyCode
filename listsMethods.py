#### Python lists Methods

list2 = [-11,2,12]

min(list2)

max(list2)

list3 = ["a","b","c"]

min(list3)

max(list3)

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

###max(list1) ###python 3 will return an error doesn't compare string with other data types

list1.append(100)###to add element in the end

print (list1)

####Python Methods to delete elements
del list1[4]

print (list1)

list1.pop(0)

print (list1)

list1.remove("Juniper")

print (list1)

####Python Methods to add elements

list1.insert(2,"Nortel")

print (list1)

####Example of Method to add a list to another

print (list1)

list2 = [9,99,999]

list1.extend(list2) ####Method to Extend the List

print (list1)

list1.index(-11) ###returns the index of the element -11 in the list that is 3

list1.append(10) ###Now we have 10 twice in the list

print (list1)

list1.count(10) ####it will count the occurances of 10 in the list

print (list2)

list2.append(1)
list2.append(25)
list2.append(500)

print(list2)

###to have the elements sorted in the ascending order

list2.sort()

print(list2)

##to have the elements sorted in the reverse order

list2.reverse()

print(list2)

###to sort the elements of list 2 in ascending order

print (sorted(list2))

print (sorted(list2, reverse = True))####to sort the list in reverse order

####also to add the 2 lists

list1 + list2

#### to multiply the list

list2 * 3






