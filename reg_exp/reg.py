#--------------------------------------------------------------------
#description : Regular Expressions 
#Used to search any pattern.
#--------------------------------------------------------------------
import re 

pattern = '\d' 
string_line = 'Sahana 4 P 2 P 96 ' 

#--------------------------------------------------------------------
#Description : Finding all matched patterns
#Used Function : findall(pattern,string)
#--------------------------------------------------------------------
result1 = re.findall(pattern, string_line) 
print(result1)

#--------------------------------------------------------------------
#Description : Splits the string at the matched patterns
#Used Function : split(pattern,string)
#--------------------------------------------------------------------
result2 = re.split(pattern, string_line) 
print(result2)

#--------------------------------------------------------------------
#Description : Replaces the matched pattern with the value given
#Used Function : sub(pattern,replace_value,string_line)
#--------------------------------------------------------------------
replace_value = '--'
result3 = re.sub(pattern,replace_value, string_line) 
print(result3)

#--------------------------------------------------------------------
#Description : Searches for the matched pattern
#Used Function : search(pattern,string_line)
#Stops at the first match.
#--------------------------------------------------------------------
result4 = re.search('\d', string_line) 
if(result4):
  print("Match Found");
  print(result4.group(0));
else:
  print("Match Not Found");
