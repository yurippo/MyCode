#operations on python strings

a = "Cisco Switch"

print  (a)

print ( a.index("i"))


print (a.count("i"))

print (a.find("sco"))


print (a.find("xyz"))

print (a.lower())

print (a.upper())

print (a.startswith("c"))

print (a.endswith("h"))

### new variable  strip method

b = "    Cisco Switch    "

print (b.strip())


c = "$$$Cisco Switch$$"

print (c.strip("$"))


print (b)


print (b.replace(" ",""))


d = "Cisco,Juniper,HP,Avaya,Nortel"

print (d.split(","))

print(a)

print ( "_".join(a))

print ("I'm a fucking new Python Line!!!")
