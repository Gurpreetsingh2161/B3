filename="example.txt"
file= open(filename,"w")

file.write("Hello,this is a test.")
file.close()

file= open(filename,"a")

file.write("Hello,this is a test.".upper())
file.close()

file= open(filename,"r")
file_content=file.readline()
file.close()
print(file_content)