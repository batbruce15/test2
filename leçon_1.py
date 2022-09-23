############################################
#[1] tuple items are enclosed in parentheses
#[2] tuple are immutable
#[3] your can remove parenthses if yo want
#[4] tuple have diffrent data types
#[5] tuple are ordered
############################################
tuple1=(4,7,8,"karim",True)
print(tuple1)
tuple2=4,7,8,"battiu",False
print(tuple2)
#tuple1[2]=55 "this is not possible because tuples are immutable"
print(tuple1[0])
print(tuple1[-1]) #they are oredred

#part 2 : Tuples and methodes
##############################################

##############################################

myTule1=("Karim",) # we use the comma to indicate that is tuple with one element
myTule2="Battou", # same here
print(type(myTule1))
myTule3=myTule1+myTule2 #concatination of tuples

print(myTule3)
myTule4= myTule3*6
print(myTule4.count("Karim"))
print(myTule4.index("Karim"))

#j'ai ajouter un commenttaire pour comprendre Pull requite
print("j'ai ajjouter un print pour comprendre pull request ")