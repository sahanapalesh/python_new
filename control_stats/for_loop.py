#-------------------------------------------------------
#description : for loop
#About       : Iterates over single character of a string
#-------------------------------------------------------

name = 'Sahana';
print("------------Iterating over a String----------------");
for i in name:
  print(i);

#-------------------------------------------------------
#Description : for loop
#About       : iterates over a list
#-------------------------------------------------------

family = ['Sahana', 'Meghana', 'Vishnu'];
print("--------------Iterating over a list----------------");
for fam in family:
  print(fam);

#-------------------------------------------------------
#Description : for loop
#About       : Iterates over a associative array
#-------------------------------------------------------

rel  = {'First':'Meghana','Second':'Sahana','Third':'Vishnu'}; 
print("----------Iterating over a associate array---------------");
for fam,name in rel.items():
  print(fam,"->",name);
