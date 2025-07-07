try:
    file=open("file1.txt")
    str=file.readline()
    print(str)
except IOError:
    print("Error occured ")
print("Successfully fetched")
