#This is printing numbers from 7-19
print ("Numbers from 7-19")
a=7
while (a<=19):
    print (1)
    a += 1
print ("")


#This is to print even numbers between 12-20
print ("Even numbers between 12 and 20")
c=13
while c<20:
    if c%2!=0:
        c +=1
    else:
        print(c)
        c += 1
    print ("")
    
#This is a function that takes two numbers and prints even numbers btn them
print ("Determine even numbers in the inputs")
def even():
    k =int(input("Enter number 1: "))
    m =int(input("Enter number 2: "))
    
    while k!=0 and m!=0:
    
        if k%2==0 and m%2!=0:
            return print ("'",k,"' ""is an even number"" '",m,"' ""is not")
        
        
        elif k%2!=0 and m%2==0:
            return print ("'",k,"' ""is not"" '",m,"' ""is an even number")
        
        
        else:
            return print ("'",k,"' ""and"" '",m,"' ""are even numbers")
        
    print("'0' is not accpted")
    
    k =int(input("Enter number 1: "))
    m =int(input("Enter number 2: "))
    continue  
    
print (even()) 
        
