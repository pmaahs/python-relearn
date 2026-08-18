def apply_twice(func, x):
    return func(func(x))
print(apply_twice(lambda x: x*2, 5))
def compose(f, g):
    return lambda x: f(g(x))
h = compose(lambda x: x + 1,lambda x: x * 2)
print(h(5))