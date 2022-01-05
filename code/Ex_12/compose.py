
def compose(f,g):
    def _comp(x):
        return f(g(x))
    return _comp

print(compose(int, abs)(-4.5))
