#### What is a set? It's an unordered collection of unique elements generally speaking like lists that don't have duplicate elements

###There are 2 ways to create a set the first way is using Python Built in Function 

list4 = [1,2,3,4,5,2,3]

list4

###we can se the set function removed the duplicate elements from the list Which is a very usefull feature to have @ hand

set(list4)

set1 = set([11,12,13,14,15,15,15,11])

set1

type(set1)

###the second way to create a set is to use {} this way of creating is available since Python 2.7 

set2 = {11,12,13,14,15,15,15,11}

set2

type(set2)

len(set2)

11 in set2

10 in set2

10 not in set2

set2

set2.add(16)

set2

set2.remove(11)

set2

set2.add(16) ###in this case python will not return an error but will not add another 16 to the set because it would be duplicate and set doesn't allow that

set2
