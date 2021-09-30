#-------------------------------------------------------
#description : while loop
#syntax      : 
#     while(condition):
#       statements;
#About       : Iterating through a condition
#-------------------------------------------------------

print("-------------Iterating through given condition----------------");
i = 7
while i!=12:
  print(i);
  i += 1; 

#-------------------------------------------------------
#Description : while loop
#About       : Iterating through a list
#-------------------------------------------------------

print("-------------Iterating through a list------------------------");
j=0;
family = ['Palesh','Parvathi','Sahana','Meghana','Vishnu'];
while j!=len(family):
  print(family[j]);
  j += 1;
