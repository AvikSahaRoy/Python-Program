# Factorial using recursion ---------------

def fact(f):
    if f == 1:
        return f
    else:
        return f * fact(f-1)
f = int(input("Enter a number: "))
print(fact(f))

# ---------------------------------------------

f = 1
i = 1
def fact(n):
    global f,i
    if i <= n:
        f = f * i
        i = i + 1
        fact(n)
    return f
n = int(input('Enter a number : '))
print('Factorial of %d is: '%n,fact(n))
