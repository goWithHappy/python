def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o=odd()
for i in range(1,5):
    print(next(o))