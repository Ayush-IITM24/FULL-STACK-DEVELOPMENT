# sum of digits: 
n= input("Enter any number: ")
sum=0
for i in n:
    sum += int(i)
    
print("The sum of digits:",sum)


# reversing a string:
name= input("Enter any word: ")
reversed_name= name[::-1]
print("The reversed name is:",reversed_name)