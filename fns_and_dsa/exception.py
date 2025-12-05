"""
class ageerror(Exception):
    pass

try:
    age=int(input('what is your age '))
    if age<18:
        raise ageerror
except ageerror:
    print("you are not eligible to vote")
else:
    print("you are eligible to vote")
   


try:
    f = open("grow.txt")
except FileNotFoundError as e:
    print("Error:", e)
else:
    print(f.read())


 """
class ValueTooHighError(Exception):
    pass
try:
    s=int(input('enter a number: '))
    if s>100:
        raise ValueTooHighError
except ValueTooHighError as e:
    print("your number is too high")
else:
    print(" your number is ok")