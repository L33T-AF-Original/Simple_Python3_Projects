print ("Hello, World!")
#list all imports first
import json
import random
import math
import ssl
import os
import subprocess
#import pygame
import pip
#import
from math import pi

#help("keywords")
#help("modules") doesn't work
print(" ")
#help(type) 

print('Enter name:') 
name = input()
print('Enter age:') 
age = int(input())
print(name,"is",age,"years old.")

if age >= 18 and age <100:
 print("What's up loser? Lol.")
elif age < 18 and age > 0:
    print("Go study.".upper)
elif age != range(1, 100) :
    print("Really, fool.?")

#from math import pi 

r = float(input ("Input the radius of the circle : ")) 
area = pi * r**2
print ("The area of the circle with radius " + str(r) + " is: " + str(area)) 
print(str(pi) + " * [" + str(r) + " * " + str(r) + "] = " + str(area))

filename = str(area) 
_filename = str(pi)
#f_extns = filename.split(".")
#print ("The extension of the file is : " + repr(f_extns[-1]))

#_f_extns = _filename.split(".")
#print ("The extension of the file is : " + repr(_f_extns[-1]))

#c=0 
#def f(x,y,z): 
#    if(0<=y<10 and 0<=z<10 and x[z][y]=='1'): 
#    	x[z][y]='0' for dy,dz in [[-1,0],[1,0],[0,-1],[0,1]]:
#        f(x,y+dy,z+dz) 
#        print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros") 
#        while 1: 
#        try: if c:input() 
#        except:break 
#       x = [list(input()) for _ in [0]*10] c=1;b=0 for i in range(10): for j in range(10): if x[j][i]=='1': b+=1;f(x,i,j) print("Number of islands:") print(b)	

exit
