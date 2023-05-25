print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')



#Functions
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

#operations
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":divide
}   
again=True
while(again==True):
    num1=int    (input("enter first number"))

    for sym in operations:
        print(sym)
    
    symbol=input("pick an operation from above")
    num2=int(input("enter first number"))
            
    cal_calcutionfunction=operations[symbol]
    result=cal_calcutionfunction(num1,num2)
    print(f"{num1} {symbol} {num2} = {result}")
    if input("type y to do calculations again and n to abort")=="y":
        again=True
    else:
        break
