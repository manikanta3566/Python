#FILE READING
f = open("demo.txt", "r")
txt = f.read()
print(txt)
f.close()

#FILE WRITING
f = open("new.txt", "w")
f.write("hii good morning")
f.close()

#FILE APPENDING
f = open("demo.txt", "a")
f.write("bye")
f.close()
