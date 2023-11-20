def dec_2_fact_string(decimal):
    number = decimal
    result = []

    for i in range(1, 10):
        quotient = number // i
        remainder = number % i
        # print(f"quotient: {quotient}, remainder: {remainder}")
        result.append(remainder)
        number = quotient
        if quotient == 0:
            break

    output = ''.join(str(x) for x in result[::-1])
    # print(output)
    return output

def fact_string_2_dec(string):
  #your code here
  pass
