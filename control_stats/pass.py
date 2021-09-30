#--------------------------------------------------------------------------------------------
# description : Comparison between Pass Statement and continue statement
# About       : Pass has no functionality. But it is syntactically correct.
#--------------------------------------------------------------------------------------------

x = [1,2,4,5];
for i in x:

  if(i is 4):
    print(i);
    pass;

  if(i is 4):
    print("Outside Pass statement",i);

for i in x:
  if(i is 4):
    print(i);
    continue;

  if(i is 4):
    print("Outside Pass statement",i);
