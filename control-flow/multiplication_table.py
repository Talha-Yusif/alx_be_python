
number=int(input("Enter a number to see its multiplication table:"))
for x in range(number,number+1):
    for y in range(1,11):
        print(f"{x} * {y} = {x*y}")