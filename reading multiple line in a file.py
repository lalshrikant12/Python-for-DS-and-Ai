with open("ex1.txt","r")as File1:
    for file_stuff in range(3): #each time loop runs it print the new line
        file_stuff=File1.readline()
        print(file_stuff)


