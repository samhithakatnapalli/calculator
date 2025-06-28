num1 = float(input())
num2 = float(input())
op = input()

if op =='+':
    print(num1+num2)
elif op =='-':
    print(num1-num2)
elif op =='*':
    print(num1*num2)
elif op =='/':
    if num2 == 0:
        print("Error")
    else:
        print(num1/num2)
else:
    print("Invalid input")
