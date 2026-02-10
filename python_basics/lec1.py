#this is a single line comment

''' This is a 
	multi line
	comment
'''
print("hello world")

#KEYWORDS
import keyword
print(keyword.kwlist)
'''OUTPUT->
	['False', 'None', 'True', 'and', 'as', 'assert',
 	'async', 'await', 'break', 'class', 'continue', 'def', 'del',
  	'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
   	'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
    'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#VARIABLE

a = 5 #initializing a variable
cup = "Tea"
print(cup) #printing a varible 
cup = "water"
print(cup)
milk =10
choco =2
choco_milk = milk + choco
print(choco_milk)