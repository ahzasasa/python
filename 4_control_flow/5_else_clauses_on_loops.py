# for, else is executed after the loop finishes its final iteration.
# while, else is executed after the loop's condition become false.
# Skip execution of else:   1. Loop was terminated by break.
#                           2. return or a raised exception.


# Searches for prime number:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")