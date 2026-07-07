n = int(input("enter a number:"))
for i in range(n):
    if i==0 or i==n-1:
        print(''.join(str(j+1) for j in range(n)))
    else:
        print(1, end='')
        print(' ' * (n - 2), end='')
        print(n)