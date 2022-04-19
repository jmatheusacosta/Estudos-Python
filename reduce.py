import functools

letters = ["O","P","A","!"]
word = functools.reduce(lambda x, y: x+y, letters)
print(word)

factorial = [i for i in range(1, 6)]
result = functools.reduce(lambda x, y: x*y, factorial)
print(factorial)
print(result)