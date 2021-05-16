
###Python functions are blocks of code that can be used over and over again and they have this format below ;)
def HelloWorld():
    print("Hello World")
    
HelloWorld()  

def Greeting(name):
    print(("Hi"+name+"!"))
Greeting("Yuri")    

def NumberSum(number1,number2):
    print (number1 + number2)
    
NumberSum(10,2)

def NumberSumReturn(number1,number2):
    return (number1 + number2)

sumNumber = NumberSumReturn(12,34)    

print(sumNumber)
    
