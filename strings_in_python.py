#Strings can be stored in a variable
first_name = 'james'
last_name = 'delphina'
print(first_name, last_name)

output = f'hello {first_name} {last_name}'

#When displaying a string that contians numbers, you can convert the number to a string
days_of_feb = 28
print(str(days_of_feb) + ' days in feb')

days_of_march = 31
print(str(days_of_march) + ' days in march')

#Numbers can be stored as strings / Numbers stored as strings are treated as strings 
first_name = '10'
last_name = '20'

print(first_name + last_name)

#Now numbers stored as astrings must be converted to numberic values before doing the math
first_name = '10'
last_name = '20'

print(int(first_name) + int(last_name))
print(float(first_name) + float(last_name))
