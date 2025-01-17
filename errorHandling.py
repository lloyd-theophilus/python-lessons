# Tpyes of errors: Syntax errors, runtime errors, and logical errors.
# Syntax errors are caused by incorrect syntax in the code.
#x = 10
#y = 20
#if x == y:
#print(x == y)

# Runtime errors are caused by incorrect input or incorrect usage of functions.
#y = 20
#x = 10
#print(x / y)

# Logical errors are caused by incorrect logic in the code.
#x = 10
#y = 20
#if x > y:
  #  print(str(x) + ' is greater than y')
    
    # Try, except, and finally blocks are used to handle errors in Python.
    # Stack trace is a list of the function calls that are currently active in the program.

# Try, Except, and Finally blocks
x = 10
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Cannot divide by zero')
else:
    print('Division successful')

finally:
    print('This is the finally block')


#Conditional Logic
# code needs to take different actions on different conditions.
price = 200
tax = 0
if price >= 100:
    tax == 20
    print(tax)
else:
    tax = 0
    print(tax)
    
# Use string functions to make case insensitive comparisons.
country = 'USA'
country = 'usa'
if country.lower() != 'usa':
    if country.upper() == 'USA':
        print('You are from the United States')
else:
    print('You are not from the United States')
    
# Adding conditions
price = input('Enter the price: ')
price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is:' + str(tax))
    
# Handling multiple conditions
# If only one of the conditions will occur, you can use a single if statement with elif
    
# example
if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

# If multiple conditions cause the same action, they can be combined into a single condition.
province = 'Alberta'
province = 'Nunavut'
province = 'Ontario'

if province == 'Alberta' or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15


# Use the in operator to check if a value is in a list.
provinces = ['Alberta', 'Nunavut', 'Ontario']
if province in provinces:
    tax = 0.05
elif province == 'York':
    tax = 0.13
else:
    tax = 0.15

# If an action depends on a combination of conditions, you can nest if statements.
if country == 'Canada':
    if province in provinces:
        tax = 0.05
elif province == 'Brownsvick':
    tax = 0.20
else:
    tax = 0.15