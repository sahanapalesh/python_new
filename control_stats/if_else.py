#-------------------------------------------------------------------------------------
#description : If-Else statements
#-------------------------------------------------------------------------------------
saha_marks = 200
meg_marks= 100

print("-------------If-Else Statement----------------");
if(saha_marks != meg_marks):
  print("Mistmatch");
else:
  print("Match");

#-------------------------------------------------------------------------------------
#Description : Nested-if-else statements
#-------------------------------------------------------------------------------------

print("-------------Nested-if-else Statement----------------");
if(saha_marks == meg_marks):
  print("Both scored equal");
else:
  if(saha_marks > meg_marks):
    print("Saha is 1st");
  else:
    print("Meg is 1st");

#-------------------------------------------------------------------------------------
#Description : If-elif-else statements
#-------------------------------------------------------------------------------------

print("-------------If-elif-else Statement----------------");
if(saha_marks >= 50):
  print("Good Score by Saha");
elif(meg_marks >= 50):
  print("Good score by Meg");
else:
  print("Bad score");
