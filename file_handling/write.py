#--------------------------------------------------------------------
#description : Writing into the file 
#Used Function : write()
#Mode : 'w'
#--------------------------------------------------------------------

with open('file.py','w') as f:
    print("writing into a file");
    f.write("Sahana (written)");

#--------------------------------------------------------------------
#Description : Appending data to same file
#Used Function : write()
#Mode : 'a'
#--------------------------------------------------------------------

with open('file.py','a') as f:
    print("appending to a written file");
    f.write("Palesh (appended)");
