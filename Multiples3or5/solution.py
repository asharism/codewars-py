def solution(number):
    if number < 0:
        return 0

    list = []  # create an empty list

    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
            # print(f"number: {number}, i: {i}")

    # if list is empty, return 0
    if not list:
        return 0
    
    return sum(list)
