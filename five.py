n = int(input("enter a number: "))
fib = [0, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])

result = ''.join(str(num) for num in fib[:n])
print(result)