# check HCF

print("Check HCF ")
a = int(input("Enter first number "))
b = int(input("Enter second number "))

H = a if a<b else b

while H>=1 :
    if a%H==0 and b%H==0 :
        print(f"HCF is = {H}")
        break
    H-=1