f=open("C:\\23bca273\\sqlite3\\data\\bca.txt","w")
f.write("bca is it cose \n")
f.write("bca is corently high dimand \n")
f.write("bca is used for internet \n")
f.write("bca is cyber cisyority \n")
f.write("bca is to developer \n")
f.close()
f=open("C:\\23bca273\\sqlite3\\data\\bca.txt","r")
l=f.read()
print(l)
f.close()
f=open("C:\\23bca273\\sqlite3\\data\\bca.txt","w")
l=[]
for i in range(5):
    user_input=input()
f.close()
f=open("C:\\23bca273\\sqlite3\\data\\bca.txt","r")
content=f.read()
word=content.split()
if word:
    smallest_word=min(words,key=len)
    larger_word=max(words,key=len)
    print(f"The smallest word is: '{smallest_word}'")
    print(f"The largest word is: '{largest_word}'")
else:
        print("No words found in the file.")

