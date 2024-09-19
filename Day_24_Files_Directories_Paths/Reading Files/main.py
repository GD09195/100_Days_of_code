file = open("my_file.txt")
file_content = file.read()
print(file_content)
file.close()

# Common way to open a file, not needing to file.close(). "with" will manage it.
with open("my_file.txt") as file_1:
    file_content = file_1.read()
    print(file_content)

#write into a file
with open("my_file.txt", mode="a") as file_to_write:
    file_to_write.write("\nNew Text")

# Create a new file. This is in write mode & when the file doesn't previously exists
with open("new_file.txt", mode= 'w') as new_file:
    new_file.write("\nThis file is new")


