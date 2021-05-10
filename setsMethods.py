>>> ####let's create a couple of sets to better understand
>>> set1 = {1,2,3,4}
>>> set2 = {3,5,8}
>>> #####now let's identify the common itens of the 2 sets using the intersection method
>>> set1.intersection(set2)
{3}
>>> ###now let's use the difference method to identify the different itens the 2 sets have
>>> set1.difference(set2)
{1, 2, 4}
>>> set2.difference(set1)
{8, 5}
>>> ###the union method merges the itens of the 2 sets
>>> set1.union(set2)
{1, 2, 3, 4, 5, 8}
>>> ###the pop method removes a randon element from the set
>>> set1
{1, 2, 3, 4}
>>> set1.pop()
1
>>> set1
{2, 3, 4}
>>> ####we can clear the set using the clear method
>>> set1.clear()
>>> set1
set()
>>> 
