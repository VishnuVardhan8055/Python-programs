""" An expression is a combination of operators and operands that is interpreted to produce some other value. """

# 1. Constant Expressions: "" These are the expressions that have constant values only. ""

x = 15 + 1.3
print(x)

# 2. Arithmetic Expressions: "" It is a combination of numeric values, operators, and sometimes parenthesis. ""

""" Operators	    Syntax  	Functioning
    ----------------------------------------
    +	     |      x + y	    Addition
    –	     |      x – y	    Subtraction
    *	     |      x * y	    Multiplication
    /	     |      x / y	    Division
    //	     |      x // y	    Quotient
    %	     |      x % y	    Remainder
    **	     |      x ** y	    Exponentiation  """

# Arithmetic Expressions
x = 40
y = 12

add = x + y
sub = x - y
pro = x * y
div = x / y
qutnt = x // y
remndr = x % y
powr = x ** y

print(add)
print(sub)
print(pro)
print(div)
print(qutnt)
print(remndr)
print(powr)

# 3. Integral Expressions:
""" These are the kind of expressions that produce only integer results after all computations and type conversions."""

# Integral Expression
a = 10
b = 34.1
sum = 10 + int(b)
print(sum)

# 4. Floating Expressions:
""" These are the kind of expressions which produce floating point numbers as result after all computations and type conversions. """

# Floating Expressions
a = 23
b = 12

c = a / b
print(c)

# 5. Relational Expressions:
"""In these types of expressions, arithmetic expressions are written on both sides of relational operator (> , < , >= , <=)."""

# Relational Expressions
a = 21
b = 13
c = 40
d = 37

p = (a + b) >= (c - d)
print(p)

# 6. Logical Expressions:
""" These are kinds of expressions that result in either True or False. """

""" 
    Operator	Syntax	    Functioning
    ----------------------------------------------------------
    and	    |   P and Q	  | It returns true if both P and Q are true otherwise returns false
    or	    |   P or Q	  | It returns true if at least one of P and Q is true
    not	    |   not P	  | It returns true if condition P is false 
    
"""

# 7. Bitwise Expressions:
""" These are the kind of expressions in which computations are performed at bit level. """

# Bitwise Expressions
a = 12

x = a >> 2
y = a << 1

print(x, y)

# 8. Combinational Expressions:
""" We can also use different types of expressions in a single expression, and that will be termed as combinational expressions. """

# Combinational Expressions
a = 16
b = 12

c = a + (b >> 1)
print(c)