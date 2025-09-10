a=20
b=30

#Arithmic operators

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a//b)
print (a%b)
print (a**b)


#Relational operators

print (a==b)
print (a!=b)
print (a<b)
print (a>b)
print (a<=b)
print (a>=b)


#Logical operators

print (a>9 and b<10)
print (a>9 or b<10)
not(a>9)
not(b<10)



#Assignment operators

a=20
b=8
a+=b
print(a)

a=20
b=8
a-=b
print(a)

a=20
b=8
a*=b
print(a)

a=20
b=8
a/=b
print(a)

a=20
b=8
a//=b
print(a)

a=20
b=8
a**=b
print(a)

a=20
b=8
a%=b
print(a)


#Bitwise operators

a=20
b=8
print(a&b)


a=10
b=8
print(a|b)

a=20
b=8
print(a^b)

a=10
b=8
print(a<<2)

a=10
b=8
print(a>>2)

a=10
b=8
print(~a)

a=10
b+20
print('a+b')

a=(10)
b+(20)
print("a+b")

a="10"
b="20"
print(a+b)


a="10"
b="20"
c=("a+b")
print(c)

name= 'abi'
age=29
future_age=age + 10
print(f"hello{name},after 10 years you will be{future_age}.")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
    
    age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
    
    
    units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity Bill: ₹", bill)


mark = int(input("Enter mark: "))
if mark >= 50:
    print("Pass")
else:
    print("Fail")