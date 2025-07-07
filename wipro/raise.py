# try:
#     raise NameError
# except:
#     print("Re-raising the exception")
#     raise 

# try:
#     print("Raising Exception")
#     raise ValueError
# except:
#     print("Exception caught....")
# finally:
#     print("performing clean-up in finally")


# c=int(input("enter temperature in c"))
# f=(c*9/5)+32
# assert(f<=32), "Its Cold"
# print("Fahreheit",f)

# def display(n):
#     while True:
#         try:
#             n=n+1
#             if n==21:
#                 raise StopIteration
#         except StopIteration:
#             break
#         else:
#             print(n,end=" ")
# i=0
# display(i)     




# import random
# class RandomError(Exception):
#     pass
# try:
#     num=random.random()
#     if num<0.1:
#         raise RandomError
# except RandomError as e:
#     print("RandomError generated")
# else:
#     print("%.4f"%num)
    
# import calendar
# year =int(input("enter the number"))
# print(calendar.calendar(year))


# from calendar import *
# year =int(input("enter the number"))
# if isleap(year):
#     print(year,"is leap year")
# else:
#     print(year, "is not a leap year")



#program to print thr next 10 day dates continuously

# from datetime import *
# d=date.today()
# print(d)
# d=date(1966,6,29)
# for x in range(1,10):
#     nextdate=d+timedelta(days=x)
#     print(nextdate)

# import time


import sys
if len(sys.argv)<2:
    print("Usage: hello hi.py <name>")
else:
    name=sys.argv[1]
    print(f"Student ,{name}") 
