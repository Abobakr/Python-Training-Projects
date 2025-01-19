import math

m1 = float(input("enter student's degree1 : "))
while m1 < 0 or m1 > 100:
    m1 = float(input("invalid degree please reenter again "))
m2 = float(input("enter student's degree2 : "))
while m2 < 0 or m2 > 100:
    m2 = float(input("invalid degree please reenter again "))
m3 = float(input("enter student's degree3 : "))
while m3 < 0 or m3 > 100:
    m3 = float(input("invalid degree please reenter again "))
x = m1 + m2 + m3
s = x / 3
s = math.ceil(s)
if s >= 60:
    print("successful")
else:
    print("failed")
