#--------------------------------------------------------------------
#description : Appending into the file and reading from the file 
#Used Function : write(), read()
#Mode : 'a+'
#seek() -> Moves the cursor to the character you mention.
#--------------------------------------------------------------------

with open('file.py','a+') as f:
    print("Appending into a file");
    f.write("a+ - Sahana");
    f.seek(0);
    print("Reading from file")
    print(f.read());


#--------------------------------------------------------------------
#Description : Writing into the file and reading from the file 
#Used Function : write(), read()
#Mode : 'w+'
#seek() -> Moves the cursor to the character you mention.
#--------------------------------------------------------------------

with open('file.py','w+') as f:
    print("writing into a file");
    f.write("w+ - Palesh");
    f.seek(1);
    print("Reading from file")
    print(f.read());

#--------------------------------------------------------------------
#Description : Replacing the lines with the string/lines given and reading from the file 
#Used Function : write(), read()
#Mode : 'r+'
#seek() -> Moves the cursor to the character you mention.
#--------------------------------------------------------------------

with open('file.py','r+') as f:
    print("replacing lines in a file");
    f.write("Sahana Palesh -- r+");
    f.seek(0);
    print("Reading from file")
    print(f.read());
