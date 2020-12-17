# If divisible by 3 'Fizz'
# If divisible by 5 'Buzz'
# If divisible by both 'FizzBuzz'
# any other numbers returns input


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input


print(fizz_buzz(1))
print(fizz_buzz(2))
print(fizz_buzz(3))
print(fizz_buzz(4))
print(fizz_buzz(5))
print(fizz_buzz(6))
print(fizz_buzz(7))
print(fizz_buzz(8))
print(fizz_buzz(9))
print(fizz_buzz(10))
print(fizz_buzz(11))
print(fizz_buzz(12))
print(fizz_buzz(13))
print(fizz_buzz(14))
print(fizz_buzz(15))
