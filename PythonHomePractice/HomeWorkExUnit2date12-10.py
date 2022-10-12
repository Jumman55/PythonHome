#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:00:31 2022

@author: jumman
"""
#Write a function that gets a float number as an input, calculates its cube root, 
#prints it on screen, and returns it

def cubeRootFinder():
    """Function to get cube root from user given number"""
    while True:
        try:
            userNumber = float(input("Enter your number: "))
            break
        except ValueError:
            print("Oops!  that was not a valid number. Try again...")
