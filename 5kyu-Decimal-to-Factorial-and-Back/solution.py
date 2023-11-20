def dec_2_fact_string(decimal):
    number = decimal
    result = []

    for i in range(1, 37):
        quotient = number // i
        remainder = number % i
        # print(f"divisor: {i:2}, remainder: {remainder:2}, get_factorial_multiplier_from_number: {get_factorial_multiplier_from_number(remainder):2}, quotient: {quotient}")
        result.append(get_factorial_multiplier_from_number(remainder))
        number = quotient
        if quotient == 0:
            break

    output = ''.join(str(x) for x in result[::-1])
    # print(output)
    return output

def get_factorial_multiplier_from_number(input_number):
    if input_number < 10:
        return str(input_number)
    
    return str(chr(input_number + 55))

def get_factorial(n):
    if n == 0:
        return 1

    return n * get_factorial(n-1)

def is_number(character):
    # print(f"character: {character}, isdigit: {character.isdigit()}")
    return character.isdigit()

def get_number_from_factorial_multiplier_string(factorial_multiplier):
    reversed_factorial_multiplier = list(factorial_multiplier[::-1])

    numbers = []
    for foo in range(0, len(reversed_factorial_multiplier)):
        if is_number(reversed_factorial_multiplier[foo]):
            numbers.append(int(reversed_factorial_multiplier[foo]))
        else:
            numbers.append(ord(reversed_factorial_multiplier[foo]) - 55)

    # print(factorial_multiplier)
    # print(reversed_factorial_multiplier)
    # print(numbers)

    return numbers

def fact_string_2_dec(string):
    numbers = get_number_from_factorial_multiplier_string(string)
    # print(numbers)
    result = 0
    for i in range(0, len(numbers)):
        result += numbers[i] * get_factorial(i)

    # print(result)
    return result