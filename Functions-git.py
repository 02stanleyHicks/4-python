#4.13.3: greetings
#colton hicks
#2.5.19
'''
name = input("what is your name: ")
def greeting():
    print("Hi there " + name +"!")
    print ("nice to meet you ")
greeting()
'''
#4.13.4 Functions and variables
#Colton Hicks
#2.11.19
x=10
def print_something():
    x=3
    print('\n', x)
print (x)
print_something()


4.14.7:print multiple times
#colton hicks
#2.19.19


def print_mult_times(string,times):
    for i in range(times):
        print(string)
print_mult_times('hey there computer scientist',7)
#4.13.6: functions and Variavle, part 3
#Colton Hicks
#2.18.19

def print_number(x):
    print (x)

print_number(13)
print('\n')
print_number(23)

#4.16.3 enter a number usning try and except
#2.20.19
#colton hicks


try:
    my_num = int(input('Enter an inerger:'))
    print('Your number:', my_num)

except ValueError:
    print('\n''that was not an integer,:(')


#4.16.4 enter name and age using the try and eccept rule
#Colton hicks
#2.20.19

name = input('enter your name: ')

age = -1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('\n''that wasn\'t an intager for your age :(')
print('\n''name:', name)
print('age:',age)


