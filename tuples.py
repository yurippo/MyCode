####tuples are another type of sequences in python you can think of tuples as imutable lists you cannot edit but they are useful when we want to store data in a form of a sequence and keep that data untoucheable however unlike set tuples are ordered collections of non unique sets meaning indexes and duplicates are allowed

myTuple =()
type(myTuple)

myTuple = (9)
type(myTuple)

myTuple = (9,)
type(myTuple)

myTuple = (1,2,3,4,5)

myTuple [0]

myTuple [1]

myTuple [-1]

myTuple [-4]

#myTuple[1] = 10 ###python will return error can't edit tuples

#del myTuple[1] ###python will give us the same kind of exception as the previous one can't edit tuples

###Example of tuple packing and unpacking variables assigned to tuple

tuple1 = ("Cisco","2600","12.4")

(vendor,model,ios) = tuple1

vendor

model

ios

###can see it as a kind of mapping between elements of 2 different tuples important to remeber that both tuples should have the same number of elements otherwise a value error will be returned

##tuple2 = (1,2,3,4) 
##(x,y,z) = tuple2
##this will return an error too many items too unpack because the number of elements is different

##another way of assigning tuples

(a,b,c) = (10,20,30)

a
b
c


