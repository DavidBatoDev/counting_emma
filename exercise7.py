str_x = "Emma is good developer. Emma is a writer"
# split the string by spaces to a list
converted_str_to_list = str_x.split(' ')
# find how many Emma appears on the list 
emma_occurence = converted_str_to_list.count('Emma')
print(f'Emma appeared {emma_occurence} time{'s' if emma_occurence > 1 else ''}')

# Output:
# Emma appeared 2 times