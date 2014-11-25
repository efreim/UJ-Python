def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print "Podaj liczbe ktorej silnie chcesz obliczyc"
num = int(raw_input())
print factorial(num)

def fibonacci(m):
    if m == 0:
        return 0
    a = 1
    b = 1
    for i in range(0, m-2):
        tmp = a
        a = b
        b = tmp
        b += a
    return b
print "Podaj dla ktorego chcesz obliczyc n-ty wyraz ciag Fibonacciego"
num = int (raw_input())
print fibonacci(num)