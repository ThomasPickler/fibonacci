print('-----------Fibonacci Sequence----------')
print()

numbers = int(input('How many numbers do you want to show? \n' ))
print()

def fibonacci(numbers):
    print(f'This is the Fibonacci sequence of {numbers} numbers:')
    print()
    
    fib1 = 0
    fib2 = 1

    if numbers <= 2:
        for i in range(0, numbers):
            print(i, end=' ')
    else:
        print(fib1, end=' ')
        print(fib2, end=' ')

        for i in range (2, numbers):
            fib3 = fib2 + fib1
            fib1 = fib2
            fib2 = fib3

            print(fib3, end=' ')
    print()
    print('-'*40)

fibonacci(numbers)

