def spuare(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

numbers = [1, 2, 3, 4, 5]
spuared_numbers = spuare(numbers)
print(spuared_numbers)
