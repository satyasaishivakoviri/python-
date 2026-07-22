'''
________OUTPUT FORMATTING

1 comma seperation(,)

example

name = 'satya'
age = '22'
print("Welcome",name,"your age is",age)

2 F-string(doc.string)

example:

name = 'satya'
age = '22'
print(f'Welcome {name} your {age} is age')

%s -----> all
%d -----> digit
%f -----> float

examples:

name = 'satya'
price = 89.0
print("price: %s" % price)

name = 'satya'
price = 89.0
print("name: %d" % name)

name = 'satya'
price = 89.0
print("price: %f" % price)

(dot).fprmat()

example:

name = 'satya'
price = 89.0
print("name:{}\nprice:{}".format(name,price))

'''
name = 'satya'
price = 89.0
print("name:{}\nprice:{}".format(name,price))
