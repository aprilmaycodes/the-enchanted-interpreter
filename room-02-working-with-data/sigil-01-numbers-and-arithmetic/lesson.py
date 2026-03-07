example_one = 5
example_two = "5"


# INTEGERS
5
-3
1
10000

# FLOATS
3.14
-.5
0.0
2.0 # 2 is an integer, 2.0 is a float


print(0.1 + 0.2) 


# STRINGS
"hello"
"5"
"3.14"


# EXERCISE
potion_count = 6
ingredient_weight = 2.4
keeper_name = "April"

# print(potion_count)
print(ingredient_weight)
print(keeper_name)


# BASIC ARITHMETIC
print(10 + 3)   # addition
print(10 - 3)   # subtraction
print(10 * 3)   # multiplication
print(10 / 3)   # division
print(10 / 2)   # regular division always returns a float


# MIXING INTS AND FLOATS
print(3 - 2.0)


# CONCATENATION vs ADDITION
print("Hello " + "World")
print("5" + 3)
print(5 + 3.0)

# SAVING RESULTS IN VARIABLES
print(19.99 + 1.60)

price = 19.99
tax = 1.60

total = price + tax

print(price)
print(tax)
print(total)

# UPDATING A VARIABLE USING ITSELF

score = 10
score = score + 1
print(score)



# EXERCISE
healing_potion_price = 12.5
mana_potion_price = 9.75
tax = .06

healing_potion_total = healing_potion_price * 3
mana_potion_total = mana_potion_price * 2
subtotal = healing_potion_total + mana_potion_total
tax_amount = subtotal * tax
final_total = subtotal + tax_amount

print(f"Your subtotal is {subtotal}. After {tax_amount} tax, your final total is {subtotal + tax_amount}.")



# FLOOR DIVISION AND THE MODULUS OPERATOR
print(17 // 5)


total_seconds = 367
print(total_seconds / 60)

minutes = total_seconds // 60

seconds = total_seconds % 60

print(f"There are {minutes} minutes and {seconds} seconds in {total_seconds} seconds")


# EXERCISE
brewed_potion = 40
vial_capacity = 6

vials = brewed_potion // vial_capacity
ounces_remaining = brewed_potion % vial_capacity

print(f"You can fill {vials} vials, and there will be {ounces_remaining} ounces leftover.")


# ORDER OF OPERATIONS
print((2 + 3) * 4)


# EXPONENTS

print(2 ** 3)

