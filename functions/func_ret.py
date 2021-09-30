#-------------------------------------------------------
# Return value without Args
#-------------------------------------------------------
def func_ret():
  name = "Saha";
  return ("(Without args) My name is " +name);

value = func_ret();

print (value);


#-------------------------------------------------------
# Return value with Args
#-------------------------------------------------------

def func_ret_1(name):
  return ("(With args) My name is " +name);

value_1 = func_ret_1("Saha");

print (value_1);
