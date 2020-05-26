#This code reads the content of file named as ex1.txt 
with open("ex1.txt","r")as File1: #file ex1.txt is opened as File1
    file_stuff=File1.read() #content of File1 is stored in the string named as file_stuff
    print(file_stuff)
    print(File1.closed)
    print(file_stuff)

