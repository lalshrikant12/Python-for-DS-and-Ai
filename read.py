#This code reads the content of file named as ex1.txt 
with open("ex1.txt","r")as File1:
    file_stuff=File1.read()
    print(file_stuff)
    print(File1.closed)
    print(file_stuff)

