#lambda functions 
#Named function

def Addition(no1,no2):
    return no1 + no2

#lambda function    
Sum = lambda no1,no2 : no1 + no2

def fun(name):
    ret = name(10,20)
    print("value from fun is :",ret)


def main():
    print("Enter first number")
    value1 = int(input())
    
    print("Enter second number")
    value2 = int(input())
    
    ret = Addition(value1,value2)
    print("Addition is",ret)
    
    ret = Sum(value1,value2)
    print("addition with lambda is :", ret)
    
    fun(Sum)
    fun(Addition)
    

if __name__ == "__main__":
    main()
    
    
# name = lambda parameters : (function body)
