#a @ b = (a + b) + (a - b) + (a * b) + (a // b)

def evaluate(equation):
    print(f"Equation: {equation}")

    numbers = equation.split('@')
    numbers = [num.strip() for num in numbers]
    
    result = 0
    for i, num in enumerate(numbers):
        if i == 0:
            result = int(num)
            continue
        
        foo = int(num)
        if foo == 0:
            return None
        result = (result + foo) + (result - foo) + (result * foo) + (result // foo)

        print(f"Index: {i}, Value: {num}, Result: {result}")
    
    return result
