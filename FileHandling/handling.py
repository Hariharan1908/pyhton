# d = open('FileHandling/file.txt', 'r')
# print(d.read())
# print(d.readline())

# f = open('FileHandling/file.txt', 'a')
# f.write("Hello How are YOu im fine")
# f.close()
# f = open('FileHandling/file.txt', 'r')
# print(f.read())

# Reading from a file
try:
    with open("FileHandling/file.txt", "r") as file:
        content = file.read()
        print("Content of example.txt:")
        print(content)
except FileNotFoundError:
    print("File not found")

# Writing to a file
try:
    with open("FileHandling/file.txt", "w") as file:
        file.write("This is some text that we are writing to the output file.")
        print("Text has been successfully written to output.txt")
except:
    print("Error writing to the file")




