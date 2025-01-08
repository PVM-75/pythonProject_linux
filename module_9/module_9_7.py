def is_prime(func):
    def wrapper(a, b, c):
        number = func(a, b, c)
        divider = number
        num_of_div = 0
        while divider > 0:
            if number % divider == 0:
                num_of_div += 1
            divider -= 1
        if num_of_div > 2:
            print('Составное')
        else:
            print('Простое')
        return number
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)