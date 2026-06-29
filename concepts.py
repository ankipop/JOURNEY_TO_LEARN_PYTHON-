#CONDITIONAL STATEMENTS 
#IF/ELIF/ELSE
#WRITE A PROGRAM FOR TRAFFIC LIGHT RULES

l=input("type the colour: ")
if(l=="red"):
    print("stop")
elif(l=="green"):
    print("go")
elif(l=="yellow"):
    print("look and wait")
else:
    print("wrong light")

#SINGLE LINE IF
#<Var>=<Var1> if<condition> else <Var2>   

food=input("write the food name: ")
eat= "yes" if food=="cake" else "no"    
print(eat)
