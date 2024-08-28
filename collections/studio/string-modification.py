my_string = "LaunchCode"

# a) Use string methods to remove the first three characters from the string and add them to the end.
modified_string = my_string[3:] + my_string[0:3]

# Use a template literal to print the original and modified string in a descriptive phrase.
print("\nThe string {0} is modified to {1}.\n".format(my_string,modified_string))


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
n = int(input("Enter the number of letters to be relocated: "))
usr_modified_string = my_string[n:] + my_string[0:n]
print("The string {0} is modified to {1}.\n".format(my_string,usr_modified_string))

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 
# 3 characters. Also, the template literal should note the error.
n = int(input("Enter the number of letters to be relocated: "))
if n > len(my_string):
    err_msg = "The number is longer than the string!"
    validated_modified_string = my_string[3:] + my_string[0:3]
    print("{2}\nThe string {0} is modified to {1}.".format(my_string,validated_modified_string,err_msg))
else:
    validated_modified_string = my_string[n:] + my_string[0:n]
    print("The string {0} is modified to {1}.".format(my_string,validated_modified_string))



