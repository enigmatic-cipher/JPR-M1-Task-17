"""
Given 3 numbers a, b and c as input, print Triangle:Yes if they can be sides of a triangle or else print Triangle:No. Note that three numbers can form a triangle if the sum of any two numbers is always greater that the third number.
Input-> a=10, b=20, c= 15
Output-> Triangle:Yes
"""

a = 10
b = 20
c = 15
if (a+b>c) and (a+c>b) and (b+c>a):
  print("Triangle:Yes")
else:
  print("Triangle:No")
