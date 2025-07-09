#file operations

'''
reading the content (r)
writing the content (w)
append to the file (a)
read write (r+)
binary (b) (rb, wb)
'''

#context manager

print("File Reading \n")
#reading the content from the file file.txt
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

print("File Writing \n")
#write the content onto the file file.txt
with open("file.txt", "w") as file:
    file.write("reading the content (r) \n" \
    "writing the content (w)\n" \
    "append to the file (a)\n" \
    "read write (r+)\n" \
    "binary (b) (rb, wb)\n")

print("File Reading after the content\n")
#reading the content from the file file.txt
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

#Append to add content on top of it
with open("file.txt", "a") as file:
    file.write("reading the content (r) \n" \
    "writing the content (w)\n" \
    "append to the file (a)\n" \
    "read write (r+)\n" \
    "binary (b) (rb, wb)\n")