
#1.WRITE A PROGRAM TO DO SUM OF TWO NUMBERS
a=int(input("type 1st number: "))
b=int(input("type 2nd number: "))
sum=a+b
print("sum is:",sum)


#2.WRITE A PROGRAM FOR TRAFFIC LIGHT RULES
l=input("type the colour: ")
if(l=="red"):
    print("stop")
elif(l=="green"):
    print("go")
elif(l=="yellow"):
    print("look and wait")
else:
    print("wrong light")

#3.WRITE A PROGRAM TO GRADE STUDENTS
m=int(input("type marks obtained: "))
if(m>=90 and m<=100):
    print("A")
elif(m>=80 and m<90):
    print("B")
elif(m>=70 and m<80):
    print("C")    
elif(m<70 and m>=0):
    print("D")    
else:
    print("Not Funny")


#4.WRITE A PROGRAM TO CHECK IF A NUMBER IS EVEN OR ODD
num=int(input("type a number: "))
if num%2==0:
    print("even")
else:
     print("odd")

#5.PROGRAM TO CLASSIFY USER TO AGE BASED CATEGORIES 
age=int(input("type age:"))
if age>0 and age <=13:
    print("child")
elif age > 13 and age <= 18:
    print("teenager")
else:
    print("adult")
