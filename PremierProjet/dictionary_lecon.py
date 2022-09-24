#==============================
#=========Dictionary===========
#==============================
# [1] are between curly bracket
# [2] every dictionnary item contain key and value
# [3] Dict key need to be immutable (num,str,tuple) list not allowed
# [4] value can have any datatype
# [5] key must be unique
#==============================

dic_identity={"name":"Karim","age":31,"birthday":{"year":1991,"month":7,"day":1}}
print(dic_identity)
print(dic_identity.keys())
print(dic_identity.values())
print(dic_identity["name"])

# Two dimentional dictionary
Student_list={"Karim":{"Number":"B01","name":"Batou","Age":31},
              "Rachida":{"Number":"B02","name":"Khalladi","Age":26},
              "Wiam":{"Number":"B03","name":"Moussa","Age":23}
}
print(Student_list)
print(Student_list["Karim"])

#clear
Student_list.clear()
print(Student_list)

#uptdate methode
Student_list={"Karim":{"Number":"B01","name":"Batou","Age":31},
              "Rachida":{"Number":"B02","name":"Khalladi","Age":26},
              "Wiam":{"Number":"B03","name":"Moussa","Age":23}}
Student_list.update({"Mehdia":{"Number":"B05","name":"Mebarki","Age":22}})
print(Student_list)

#copy methode
S=Student_list.copy()
print(S)