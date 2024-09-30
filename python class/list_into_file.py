#write a program to save a python list into a file and read that same file amd recover original list.
import pickle

list1=[1,2,3,4,5]
filePath="data.txt"

with open(filePath, "w") as fileHandle:
    fileHandle.write(str(list1))
    
with open(filePath,"r") as fileHandle:
    readData = fileHandle.read()
    readData = readData[1:len(readData)-1].replace(" ","").split(",")
    print(f"read data is {readData} \nits type is {type(readData)}")

with open("data.pickle","wb") as file:
    pickle.dump(readData,file)

print("Data has been serialised and saved to data.pickle")
