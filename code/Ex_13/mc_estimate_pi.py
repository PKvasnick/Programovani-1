import random

def generate_hits(n):
    yield from ((random.random(), random.random()) for _ in range(n))

def good_hit(u, v):
    return (u-0.5)**2 + (v-0.5)**2 < 0.25

def count_hits(n):
    return sum(good_hit(u,v) for u, v in generate_hits(n))
            
n=1000000
print(4*count_hits(n)/n, math.pi)
    
    
