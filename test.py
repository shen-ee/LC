def gen(num):
    for prime in range(1,5):
        yield num*prime


f1 = gen(5)
print(next(f1))
print(next(f1))
