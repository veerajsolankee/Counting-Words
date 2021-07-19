def count():

    number=0
    fileName=input("enter a file")
    f= open(fileName,'r')
    for line in f:
        word=line.split()
        number=number+len(word)

    print("number of words in a file is",+number)

count()