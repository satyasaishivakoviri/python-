'''
python


	- in the year 1991 by russon




what is python
		- high level language
		- oops
		- interpreted language 
					:- the code will be executed line by line that's the reason python is a interpreted language
				        example :- num=9
						   print(num)
						   sum=90
						   print(num)
		- dynamically typed language
					:- no need to mention the type of data pass to the variable
					example :-   num = [5,6]
    					   	     print(type(num))


why python
		- easy to learn
		- less syntax
		- easy to understand
		- cross platform
		- open-source
		-large number of libraries


comments
		- single-line (#) :- this is used to explain line in the code
		- multi-line :- used to comment multiple line using (''' ''',""" """)


variables
		- this is used to store the datatypes 
		- we can start with :- "_", "small letters", "capital letters"
		- we cannot start with :- "special  characters", "number at first position", "space"


Boolean types
		- example :- num = 9
			     num_2 = 89
			     print(num != num_2)


multiple variables with single value
						example :- num = num_2 = num_3 = 78
							   print(num_2)

multiple variables with multiple value
						example :- num,num2 = 9,90 
							   print(num)
							   print(num_2)

swapping variable without using third variable
						example :- num = 7
   							   num_2 = 70
							   num,num_2 = num_2,num
                                                           #7,70 = 70,7
							   print(num)


tokens
	tokens are the smallest individual parts or units in the program
		-keywords
		--> keywords are the words which are already preloaded -if,else,for,return,while
		-identifiers
		--> variables, functions, class names
		-operators
		--> +, -, =
		-literal
		--> int, str, tuple, list


operators
            - arithametic
            --> -, +, /, %, *, **
            num = 8
            num_2 = 7
            print(num + num_2)
            print(num - num_2)
            print(num * num_2)
            print(num ** num_2)
            print(num % num_2)
            print(num / num_2)
            - assignment
            --> =, += (num = num +1), -= (num = num-1), *=, %=, /=
            num = 8
            num_2 = 7
            print(num -= 1)
            - comparision
            --> ==, !=, <, >, <=, >=,
                num = 8
                num_2 = 7
                print(num == num_2)
                print(num != num_2)
                print(num <= num_2)
                print(num >= num_2)
                print(num < num_2)
                print(num > num_2)
            - logical
            --> and, or, not
                num = 8
                num_2 = 7
                print(num < num_2 and num_2 < 100)
                print(num > num_2 or num_2 < 100)
                print(not(num > num_2 or num_2 < 100))
            - identifiers
            --> is , is not
                so = [1,1]
                how = [1,1]
                print(so is how)
                print(so == how)
            - membership
            --> in, not in
            so = [1,2,3,4,5]
            print(7 not in so)
            - bitwise
            --> &, |, ^, <<, >>
            print(1 & 2)
            print(1 | 2)
            print(1 << 2)
            print(1 >> 2)
'''
print(1 & 2)
print(1 | 2)
print(1 << 2)
print(1 >> 2)
