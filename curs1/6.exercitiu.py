

lista = [10, 2, 30, 50, 300, 10]

# versiunea 2 - filter + funtctia lambda
print(list(filter(lambda x: x > 5, lista)))

# versiunea 3 - list comprehention
print([element for element in lista if element > 5])