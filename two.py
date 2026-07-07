n= str (input("Enter a Number:"))
while len(n) > 1:
    x = sum(int(i) for i in n)
    print(x)
    n = str(x)