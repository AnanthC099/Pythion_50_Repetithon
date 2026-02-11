def PowerFunctionFactory(N:int): 
    def InnerFunction(x:float): 
        return x ** N 
    return InnerFunction 

mySquareFunction = PowerFunctionFactory(2) 
myCubeFunction = PowerFunctionFactory(3)

myRaisedToSevenFunction = PowerFunctionFactory(7)

result = mySquareFunction(2)
print('mySquareFunction(2):', result)           # 4 

result = myCubeFunction(2)
print('myCubeFunction(2):', result)             # 8 

result = myRaisedToSevenFunction(2) 
print('myRaisedToSevenFunction(2):', result)    # 128 
