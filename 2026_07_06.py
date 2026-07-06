numbers = [x for x in range(5)]
print(numbers)

def square(x):
    return x*x

squares = list(map(lambda x: x*x, range(5)))
print(squares)
print([square(x) for x in range(5)])

even_numbers = [x for x in range(5) if x%2==0]
odd_numbers = [x for x in range(6) if x%2!=0]
print(even_numbers)
print(odd_numbers)

even_list = [x if x%2==0 else -x for x in range(5)]
print(even_list)

# 딕셔너리
