# ------------------------
# ----------set-----------
# ------------------------
# [1] set items are closed in curly bracket
# [2] set items are not ordered and not indexed
# [3] set indexing and slicing can't be done
# [4] set has only immutable data
# [5] set items are unique
#mySetOne ={"Karim","Battou",31, [1,4,5,6]} #only immutable data
mySetOne ={"Karim","Battou",31}
#print(mySetOne{0}) can't be indexed
print(mySetOne)
mySetTwo={"Karim",22,"Battou","Battou",4,22}
print(mySetTwo)

#set methodes
#clear()
mySetOne.clear()
print(mySetOne)

#union
mySetThree={"html","css","php"}
print(mySetTwo.union(mySetThree))
print(mySetTwo|mySetThree)

#add() methode
mySetTwo.add("python")
print(mySetTwo)

# copy methode
mySetfour=mySetTwo.copy()
print(mySetfour)

#remove() methode
mySetfour.remove("python")
print(mySetfour)