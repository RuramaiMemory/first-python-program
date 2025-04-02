#strings
age = 45
first_name ="Lee"
food ="banana"
email ="memo123@.com"
phona = "0789193620"
print(f"you are age is{age}")
print(f"you are phona is{ phona}")
print(f"hello{first_name}")
print(f"you like{food}")
print(f"your email is {email}")

#lntegers
age =20
quantity =5
unm_students =45
time=1.23
menu=7
print(f"you are menu{menu}")
print(f"you are time{time}")
print(f"you are {age}")
print(f"you are duying{quantity}items")
print(f"your are unm_students{unm_students} ")

#Booleans
x=True
y=False

print(x and y)
print(x or y)
print(not x) 

x =6
y =10

if x >y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

#List
my_list =[4,2,1,3]
my_list.sort()
print(my_list)
my_list =[1,2,3,4,5,6]
my_list .reverse()
print(my_list)
my_list =[1,2,3,4,5,6,7,8,9,10]
print(my_list.pop())
print(my_list)
my_list=[20,40,50,60]
print(my_list)

#List 
doudles =[]
for x in range(1,12):
    doudles.append(x*2)
print(doudles)

triples=[y*3 for y in range(1,12)]
squres =[z*z for z in range(1,12)]
print(triples)
print(squres)

fruits=["apple","banana","cocconut","orange"]
fruits_chars=[fruit.upper()for fruit in fruits]
print(fruits_chars)

grades=[80,42,79,90,56,61,30]
passing_grade=[grade for grade in grades if grade>=60 ]

# lntegers(int)
age = 22
print(age)

height = 5.9
print(height)


name = "memory"
print(name)

is_sunny = True
is_raining = False
print(is_sunny)
print(is_raining)

Fruits  = ["apple","banana","cherry",]
print(Fruits)
print(Fruits[1:4])

coordinates = (10,20)
print(coordinates[1])
person ={"name":"Lee","age":29}
print(person)
print(person["name"])


unique_unmbers = {1,2,3,3,2}
print(unique_unmbers)
print(1,2,3,)

a = {1,2,3}
b = {1,2,3}
c =a

print(a is b)
print(a is c )

my_set1 = {1,2,3}
my_set2 = my_set1
print(my_set1 is my_set2)


set1 = {1,2,3}
set2 ={3,4,5}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1^set2)

my_set ={1,2,3,4,5}
print(3 in my_set)
print(6 in my_set)

my_set1 ={1,2,3}
my_set2={1,2,3}
print(my_set1 is my_set2)

nested = ((1,2),(3,4))
print(nested[1][0])

location = {(0,0): "Origin",(1,2): "Point A"}
print(location)

#if_else statement

x=5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
x=5
if x>10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 10")
else:
 print("x is less than 5")

#float
num=23.6
distance=34.50
print(num)
print(type(num))

num= float(input("Enter the num student's  (0-70): "))
if num >= 90:
    distance= "A"
elif num>= 80:
     distance= "B"
elif num >= 70:
    distance= "C"
elif num >= 60:
    distance= "D"
else:  
    distance = "F"
print(f"The student's distance is: {distance}")

a = 23
b = 24 
c = 2

print(a>b and b == c)

username =input("Enter your username:") 
password = int(input("Enter your password"))
if username == "addmin" and password ==1234:
    print(f"welcome {username} your are logged in.")
else:
    print("invalid credentials")
temp = 30
if temp ==30 and 'condition'.lower() =="sunny":
 print(f"the temp is {temp} degrees and it is {'condition'}")
else:
    print(f"it is cold")

day = ("enter day:").lower()
if day == "monday":
   print("wear uniform")
elif day =="tuesday":
   print("wear garments")
elif day =="wednesday":
   print("casual")  
elif day == "thursday":
   print("wear formal")
   days = ["monday","tuesday","wednesday","thursday","friday"]
print("days")
print("monday is wear uniform")

name = input("what is your name ")
print("Hello" + name)

while True:
    command = input("Enter a command: ").lower()  # .lower() to handle case insensitivity
    
    if command == 'start':
        print('car started')
        
    elif command == 'help':
        print("""
start - to start the game
stop - to stop the game
quit - to quit the game
help - to show all commands
""")
        
    elif command == 'stop':
        print('car stopped')
        
    elif command == 'quit':
        print('Exiting the game...')
        break
        
    else:
        print('invalid command')

#fuctions
def greet(name):
    print(f"Hello, {name}!")

greet("Ruru")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Square root of negative number!"
    else:
        return x ** 0.5

def calculator():
 print("Advanced Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")
print("7. Quit")
print("8.pop")

#Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")
if float in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if float == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif float == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif float == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif float == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
  print("Invalid float !")

#sotp

def print_invalid_command():
    print("Invalid command")

def print_menu():
    print("Car Controls:")
    print("1. Start")
    print("2. Accelerate")
    print("3. Brake")
    print("4. Stop")
    print("5. Exit")

def start():
    print("The car is started.")

def accelerate():
    print("The car is accelerating.")

def brake():
    print("The car is braking.")
def stop():
    print("The car has stopped.")

def main():
    car_started = False
    
    while True:
        print_menu()
        user_input = input("Enter a command: ")
        
        if user_input == "1":
            start()
            car_started = True
        elif user_input == "2":
            if car_started:
                accelerate()
            else:
                print("You need to start the car first.")
        elif user_input == "3":
            if car_started:
                brake()
            else:
                print("You need to start the car first.")
        elif user_input == "4":
            if car_started:
                stop()
                car_started = False
            else:
              print("The car is already stopped.")
        elif user_input == "5":
            break
        else:
            print_invalid_command()

print("invalid_command")
print("car_started ")
print("user_input")
print(" accelerate")

score=0
full_name =("memory")
print(score)
print(full_name)
age=20
print(age)
surname =("makara")
print(surname)
birth ="11/13/2005"
print(birth)
print("date to birth")

#loop
correct_number = 7
attempts = 0
while True:
    user_guess = input("Guess a number between 1 and 10: ")
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue
    attempts=1
    if user_guess==correct_number:
        print
    











