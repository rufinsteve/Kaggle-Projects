# 1) WORKING WITH SETS
lettersA = {"A", "B", "C", "D"};
lettersB = {"E","F","A","D"};

# Union Sets
union = lettersA | lettersB
print(f"Union = {union}")

# Intersection sets
intersect = lettersA & lettersB
print(f"Intersection = {intersect}")

# Difference sets
Diff = lettersA - lettersB
print(f"Difference = {Diff}")

# 2)  WORKING WITH DICTIONARIES

person = {
    "name" : "Jamel",
    "age" : 20,
    "address" : "Calgary"
}

#get a value from the dictionary
print(person["name"])
print(person["address"])

#Some methods with dictionaries
print(person.keys())
print(person.values())
print(person.get("age"))

# Update a value 
person["age"] = 33
print(person)

#3) LOOPS

names = ["Ahmed", "Annah", "Ricardo", "Francesca"]

for name in names:
    print(name)

for key in person:
    print(key)


for key, value in person.items():
    print(f"key:{key} and value:{value}")
#for key in person:
#    print(f"key:{key} value:{person[key]}")

numbers = [1, 3, 5, 6, 7, 9]
result = 0
for number in numbers:
    result = result + number
print(result)

# WHILE LOOP

number = 0
while number < 10:
    print(number)
    number += 1


n = 0
while n < 10:
    if n == 5:
        break
    n +=1
    print(n)
    

m = 0
while m < 10:
    m +=1
    if m < 5:
         continue
    
    print(m)


#4 FUNCTIONS

def greet():
    print("Hello how are you?")

greet()
     

def person(name):
    print(f"Hello {name}, how are you?")

person("ali")

def people(name, age):
    print(f"Hello {name}, your are {age} years old")

people("Karim", 20)
people("Eric", 54)


def is_adult(age):
    if age >= 16:
        return True
    else:
        return False

print(is_adult(60))


import statistics

from statistics import median


import Calculator
print(Calculator.add(2, 3))
print(Calculator.divide(5, 8))


from Calculator import multiply

print(multiply(5, 10))


# CLASSES

class phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

iphone = phone("Iphone", 300)
samsung = phone("Samsung", 1.400)

print(f"This is a {iphone.brand} \n {iphone.price} CAD")

samsung.call(5874296101)


# WORKING WITH DATES

import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.time())

from datetime import datetime
print(datetime.now())

time = datetime.now()
print(time.strftime("%d/%m/%Y %H:%M:%S"))
print(time.strftime("%d/%B/%Y %H:%M:%S"))


# CREATING FILES
file = open("./data.csv", "r")
print(file.read())
print(file.readlines())
file.close()




# FETCH DATA FROM INTERNET

from urllib import request

page = request.urlopen("https://amazon.com")

print(page.getcode())
print(page.read())


# MAKE API CALL AND WORK WITH JSON OBJECT



import requests
import json
response = requests.get("http://ghoapi.azureedge.net/api/Dimension")
print(response.status_code)
print(response.text)
     
print(json.loads(response.text))


# FROM TEXT TO SPEECH

#import pyttsx3
#pyttsx3.speak("Can I get a piece of paper?")

#file = open("./speakInPython.csv", "r+")
#file.write("import pyttsx3 \n pyttsx3.speak('What is your name')")







