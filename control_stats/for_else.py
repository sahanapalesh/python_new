#--------------------------------------------------------------------------------------------
#description   : For-else loop
#Functionality : Else will be executed only when for loop exits normally without break statement.
#--------------------------------------------------------------------------------------------
numbers = [12,19,67,33,89];

for num in numbers:
  if(num % 7 == 0):
    print(num);
    break;
  else:
    print("Not Found");


#--------------------------------------------------------------------------------------------
#Description   : For-else loop
#Functionality : Else will be executed only when for loop exits normally without break statement.
#Syntax : 
#     for num in nums:
#       statements;
#     else:
#       statements;
#--------------------------------------------------------------------------------------------


numbers2 = [12,19,49,67,33,89];

for num in numbers2:
  if(num % 7 == 0):
    print(num);
    break;
  else:
    print("Not Found");
