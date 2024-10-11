#FileNotFound
from numpy.distutils.cpuinfo import key_value_from_command

with open ("./a.txt") as file:
    file.read()


try:
    #Try opening the file
    file = open("./a.txt")
except FileNotFoundError as error_message:
    #If the file doesn't exist, create it.
    open("./a.txt", "w")
else:
    print('File existed')
    file_content = file.read()
finally:
    file.close()

raise KeyError("This is an example of an Exception raised.")


#KeyError
my_dictionary = {"key": "value"}
value = my_dictionary["non_existing_key"]

#IndexError
my_list = ["one", "two", "Three"]
four = my_list [4]

#TypeError
text = 'abc'
print(text + 5)



#-------------------------------------------------

###Caching Exceptions Keywords
try:
    #Something that might cause an exception

except:
    #Do this if there WAS an exception

else:
    #Do this if there were NO exception


finally:
    #Do this no matter what happens


raise:
    #Raise my own Exceptions