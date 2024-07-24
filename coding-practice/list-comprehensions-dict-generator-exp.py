squares = [x**2 for x in range(10)]
print ("comprehension for squares in the range of 10 in a list")
print (squares)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print ("comprehension for even squares in the range of 10 in a list")
print(even_squares)

square_dict = {x: x**2 for x in range(5)}
print ("comprehension of squares in the range of 5 in a dictionary")
print(square_dict)

gen = (x**2 for x in range(10))
print ("An example of generator expression in the range of 10")
print(next(gen))
print(next(gen))