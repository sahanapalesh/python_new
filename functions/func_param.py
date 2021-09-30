#-------------------------------------------------------
# Function with non keyword based Args consisting of paramater
#-------------------------------------------------------
def func_non_key(*mems):
  print(mems);

  for mem in mems:
    print (mem);

func_non_key("Saha",4,96,"Palesh");


#-------------------------------------------------------
# Function with keyword based Args consisting of paramater
#-------------------------------------------------------
def func_key(**param):
  for key, value in param.items():
    print('{}:{}'.format(key,value));

func_key(name="Saha",num=4);


#-------------------------------------------------------
# Accessing elements using key
#-------------------------------------------------------
def func_key_param(**param):
  print(param["name"]);

func_key_param(name="Saha",num=4)
