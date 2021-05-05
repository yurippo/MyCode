movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman",["Michael Palin", "John Cleese", "Terry Gilliam","Eric Idle", "Terry Jones"]]]

###the for loop prints the items of the Outer Loop only
for eachItem in movies:
    print(eachItem)

####For improved with if else, isistance and nested loop this code is a little better but still needs to be improved to print the items of the last list

for eachItem in movies:
    if isinstance (eachItem,list):
        for nestedItem in eachItem:
            print(nestedItem)
    else:
        print(eachItem)

####New code with one more loop this time for a deeper item

for eachItem in movies:
    if isinstance (eachItem,list):
        for nestedItem in eachItem:
            if isinstance (nestedItem,list):
                for deeperItem in nestedItem:
                    print(deeperItem)
            else:
                print(nestedItem)
    else:
        print(eachItem)
