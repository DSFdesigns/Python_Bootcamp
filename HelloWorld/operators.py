# Numeric data types (int, float, complex)
# int = whole number, float = has fractional part



#print(a + b) # 15
#print(a - b) # 9
#print(a * b) # 36
#print(a / b) # 4.0
#print(a // b) # 4 integer divison, rounded down towards minus infinity
#print(a % b) # 0 modulo: the remainder after integer division

# print()
# for i in range(1,4):
#	print(i)

# print()
# for i in range(1, a // b):
#	print(i)

# i = 1
# print(i)
# i = 2
# print(i)
# i = 3
# print(i)

# Quiz:
# bun_price = 2.40
# money = 15
# print(money // bun_price)
a = 12
b = 3
# Operator Precedence
# Multiplication and division are higher priority
# Addition and subtraction have lower priority
# Operator Precedence Acronyms
# PEMDAS Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
# BEDMAS Brackets, Exponents, Division/Multiplication, Addition/Subtraction
# BODMAS Brackets, Order, Division/Multiplication, Addition/Subtraction
# BIDMAS Brackets, Index, Division/Multiplication, Addition/Subtraction

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12)) 
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12 )

c = a + b # 15
d = c / 3 # 5
e = d - 4 # 1
print(e * 12)

print()

print(a / (b * a) / b)
