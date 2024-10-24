import re

pattern = r"hello"
text = "hello world"
match = re.search(pattern,text)
print("Match found:", match.group() if match else "No match")

text2 = "hello hello world"
match2 = re.search(pattern,text2)
print("Match found:", match2.group() if match2 else "No match")

pattern2 = r"cat"
text3 = "The cat sat on the mat"
match3 = re.search(pattern2,text3)
print("Match found:", match3.group() if match3 else "No match")

pattern3 = r"c.t" #matches any character between c and t
text4 = "The cat sat on the mat"
match4 = re.search(pattern3,text4)
print("Match found:", match4.group() if match4 else "No match")

pattern4 = r"[a-z]+" # + means alteast 1 or more
text5 = "Hello World 123"
match5 = re.findall(pattern4,text5)
print("Match found:", match5)

pattern5 = r"[A-Z, a-z, 0-9]+"
text6 = "Hello World 123"
match6 = re.findall(pattern5,text6)
print("Match found:", match6)

pattern6 = r"[A-Z, a-z,\d]+" # \d means all digits
text7 = "Hello World 123"
match7 = re.findall(pattern6,text7)
print("Match found:", match7)

pattern7 = r"[\w]+" # \w means all characters and digits
text8 = "Hello World 123"
match8 = re.findall(pattern7,text8)
print("Match found:", match8)

pattern8 = r"\d{3}" 
text9 = "123456789"
match9 = re.findall(pattern8,text9)
print("Match found:", match9)

pattern9 = r"h.llo" 
text10 = "hello h1llo h.llo"
match10 = re.findall(pattern9,text10)
print("Match found:", match10)

pattern10 = r"[hlo.]+" 
text11 = "hello h1llo h.llo"
match11 = re.findall(pattern10,text11)
print("Match found:", match11)

pattern11 = r"[\s]+" # \s is for including space 
text12 = "hello h1llo h.llo"
match12 = re.findall(pattern11,text12)
print("Match found:", match12)

pattern12 = r".*"  # largest combination of characters
text13 = "content"
match13 = re.search(pattern12,text13)
print("Greedy match:", match13.group())

pattern12_lazy = r".*?" # lowest combination of characters
match13_lazy = re.search(pattern12_lazy,text13)
print("Lazy match:", match13_lazy.group())

pattern13 = r".+"  
text14 = "content"
match14 = re.search(pattern13,text14)
print("Greedy match:", match14.group())

pattern13_lazy = r".+?"
match14_lazy = re.search(pattern13_lazy,text14)
print("Lazy match:", match14_lazy.group())

#pattern14 = r"(\d{3}-(\d{2}))"
#text15="Phone number: 123=45"
#match15 = re.search(pattern14,text15)
#print("Area code:", match15.group(1))
#print("Local code:", match15.group(2))

#pattern15 = r"world" 
#text16 = "Hello world"
#match16 = re.search(pattern15,text16)
#print("Match found:", match12)

pattern16=r"cat"
text17= "The cat sat on the mat"
result=re.sub(pattern16,"dog", text17)
print("After substitution", result)

pattern17=r"\s+"
text18= "Split this sentence by spaces"
result2=re.split(pattern17, text18)
print("Split method:", result2)

text19="abc efg hig lmn opq"
print(text19.split(" "))