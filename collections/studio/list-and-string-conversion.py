proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]
print("\n")
# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for string in strings:
    
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array 
# into a new comma separated string.
    if ',' in string:
        print(string, " uses commas.")

        # split it into an array
        stringTOlist = string.split(',')
        print(stringTOlist, " converted to list.")

        # reverse the entries
        for index in range(len(stringTOlist)):
            stringTOlist[index] = stringTOlist[index][::-1]
# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as 
# part “b”, making sure that the extra spaces are NOT part of the final string.
            stringTOlist[index] = stringTOlist[index].strip()
        print(stringTOlist, "Reversed string list")

        # join the array into a new comma separated string.
        reversed_combined_string = ','.join(stringTOlist)
        print(reversed_combined_string, " Reversed string list to comma separated string.\n ")

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, 
# and then join the array into a new comma separated string.
    elif ';' in string:
        print(string, " uses semicolons.")
        semicolon_List = string.split(';')
        print(semicolon_List, " converted to list.")
        semicolon_List.sort()
        print(semicolon_List, " sorted in ascending.")
        reversed_semicolon_str = ','.join(semicolon_List)
        print(reversed_semicolon_str, " Reversed semicolon list into string.\n")

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the 
# entries, and then join the array into a new space separated string.
    elif ' ' in string:
        print(string, " uses spaces.")
        spaces_list = string.split()
        print(spaces_list, " converted to list.")
        spaces_list.sort(reverse=True)
        print(spaces_list, "sorted in reverse order.")
        reversed_spaces_Str = ' '.join(spaces_list)
        print(reversed_spaces_Str, " Reversed spaces list into string.\n")
