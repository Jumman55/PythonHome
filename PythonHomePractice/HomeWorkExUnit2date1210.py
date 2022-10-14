#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:00:31 2022

@author: jumman
"""
#Write a function that gets a float number as an input, calculates its cube root, 
#prints it on screen, and returns it

def cubeRootFinder():
    """Function to get cube root from user given number even if negative number"""
    while True:
        try:
            userNumber = float(input("Enter your number: "))
            break
        except ValueError:
            print("Oops!  that was not a valid number. Try again...")
    
    if userNumber < 0:
        positiveUserNumber = userNumber * (-1) #kind of abs value
        cubeRoot = (positiveUserNumber ** (1/3))
        print("Cube root numer is:", cubeRoot)
        return cubeRoot
    else:
        cubeRoot = userNumber ** (1/3)
        print("Cube root numer is:", cubeRoot)
        return cubeRoot

cubeRootFinder()

# %% ---

#Write a function that gets five integers as an input and returns 
#the sum of all even numbers minus the sum of all odd numbers

def evenMinusOdd():
    """The sum of all even numbers minus the sum of all odd numbers"""
    
    evenNumber = 0
    oddNumber = 0
    
    def userInput():
        """Get valid data from user by handling error"""
        while True:
            try:
                userData = int(input("Enter your value: "))
                return userData
                break
            except ValueError:
                print("Oops! that was not valid number. Try again...")
    
    
    for _ in range(5):
        userNumber = userInput()
        if userNumber % 2 == 0:
            evenNumber += userNumber
        else:
            oddNumber += userNumber
    
    return evenNumber - oddNumber
        
        
        
print("All even minus all odd",  evenMinusOdd())
      

# %% ---
#Write a function that gets three integers as an input d, m, y 
#(it is assumed that a is always an odd number to avoid leap years) and returns
# True or False depending on whether the three numbers form a valid date in the
# "d/m/y" format. Ex: 30/2/2017 False, 1/1/1111 True


def dateValidation():
    """Check if given date is valid by month day numbers"""
    
    
    def userInput():
        """Get valid data from user by handling error"""
        while True:
            try:
                userData = int(input("Enter your value: "))
                return userData
                break
            except ValueError:
                print("Oops! that was not valid number. Try again...")
    
    #problem with this code i can't say date or monthe when ask for user data
    
    givenDate = userInput()
    givenMonth = userInput()
    givenyear = userInput()
    
    if givenMonth == 1:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    elif givenMonth == 2:
        if givenDate >= 1 and givenDate <=28:
            return True
        else:
            return False
    elif givenMonth == 3:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    elif givenMonth == 4:
        if givenDate >= 1 and givenDate <=30:
            return True
        else:
            return False
    elif givenMonth == 5:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    elif givenMonth == 6:
        if givenDate >= 1 and givenDate <=30:
            return True
        else:
            return False
    elif givenMonth == 7:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    elif givenMonth == 8:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    elif givenMonth == 9:
        if givenDate >= 1 and givenDate <=30:
            return True
        else:
            return False
    elif givenMonth == 10:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    elif givenMonth == 11:
        if givenDate >= 1 and givenDate <=30:
            return True
        else:
            return False
    elif givenMonth == 12:
        if givenDate >= 1 and givenDate <=31:
            return True
        else:
            return False
    else:
        return False
     
        
        
print(dateValidation())
    
"""
you can make this program better by dividing and concer algo such as 
if the monthe is 4, 6,9, 11 then it will check 30 days and return bool nor
if the month is 2 it will check 
we can directly return the logic because it's a boolean

"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    