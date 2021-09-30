//-------------------------------------------------------
// Function with Default Args
//-------------------------------------------------------
def func_def (name="Saha",year=1996):
  print (name, "born in year", year);

func_def();

//-------------------------------------------------------
// Function with Default Args and Different in Function Call
//-------------------------------------------------------
def func_def (name="Saha",year=1996):
  print (name, "born in year", year);

func_def("Paru",1964);

//-------------------------------------------------------
// Function with Default Args and Different in Function Call
// With only 1 Arg changed
//-------------------------------------------------------
def func_def (name="Saha",year=1996):
  print (name, "born in year", year);

func_def("Megu");
