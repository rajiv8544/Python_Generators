def square(num):
    for i in range(1, num):
        yield i**2
    

print(list(square(45)))
