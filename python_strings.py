# TODO Create Variables
#   - Create the following variables
#   - my_first_name
my_first_name = "Jackson"
#       -set this equal to your first name
#   - my_last_name
my_last_name = "Hardy"
#       -set this equal to your last name
#   - my_year_of_birth
my_year_of_birth = "1990"
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
current_year = "2023"
#       -set this equal to 2020




# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
print (my_first_name)
#       - last name
print (my_last_name)
#       - first letter of your first name (use the +index)
print (my_first_name[0])
#       - second letter of your last name (use the -index)
print (my_last_name[-2])
#       - first two letter of your first name (use the +index)
print (my_first_name[0:2])
#       - second two letter of your last name (use the -index)
print (my_last_name[-5:-3])



#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
print (my_first_name, my_last_name)
#       -first name six times
print (my_first_name * 6 )





# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
print (my_first_name, my_last_name, "was born in", my_year_of_birth)
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
print (my_first_name, my_last_name, "was born in", str(my_year_of_birth) + ".", my_first_name, "enjoyed celebrating", current_year)




# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
print ("Jackson's", "birth year is", my_year_of_birth)
#       - tab last name current year
print ("\t", my_last_name, current_year)


# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
print(my_first_name.casefold(), my_last_name.casefold())
#       - length of last name
print(my_last_name.__len__())
print(len(my_last_name))
#       - first name and last name all in upper case
print(my_first_name.upper(), my_last_name.upper())
print((my_first_name), (my_last_name))