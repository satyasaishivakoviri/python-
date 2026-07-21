'''
INPUT FORMATTING

___integer: int(input())

example :

num = int(input('enter a num: '))
print(num + 9)
print(type(num))

___string: str(input())

example:

we = input('enter: ')
print(type(we))

___list:

example for integer:

nums = list(map(int,input('enter nums: ').split()))
print(nums)

example for string:

names= input('enter nums: ').split()
print(names)

___tuple:

example for integer:

nums = tuple(map(int,input('enter nums: ').split()))
print(nums)

example for string:

names= tuple(input('enter nums: ').split())
print(names)

___eval:

example:

names= eval(input('enter nums: '))
print(type(names))
'''
times = input('enter time of 24: ')
part = times.split(':')
hours = int(part[0])-12
print(hours, ":", part[1], "PM")

