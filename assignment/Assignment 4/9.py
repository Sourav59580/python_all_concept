# check LCM
print("Check LCM ")
a = int(input("Enter first number "))
b = int(input("Enter second number "))

L = a if a>b else b 

while L<=a*b :
    if L%a==0 and L%b==0 :
        print(f"LCM = {L}")
        break
    L+1