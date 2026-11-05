import numpy as np
from math import erf, exp

S, K, r, s = 100, 100, 0.05, 0.2  # Basic parameters

def tree(n, c=1, am=0):  # c=1 for Call, -1 for Put | am=1 for American
    dt = 1/n
    u = exp(s * dt**0.5)
    d = 1/u
    g = exp(r * dt)
    p = (g - d) / (u - d)
    x = lambda i: S * u ** np.arange(-i, i+1, 2)
    V = np.maximum(c * (x(n) - K), 0)  # Payoffs at maturity
    
    for i in range(n-1, -1, -1):  # Backwards induction
        V = (p * V[1:] + (1-p) * V[:-1]) / g
        V = np.maximum(V, am * c * (x(i) - K))  # Early exercise check
        
    return V[0], u, d, p

# Test convergence with different steps
for n in [1, 2, 3, 10, 1000]:
    print(n, *tree(n))

# Black-Scholes benchmark
N = lambda x: 0.5 + erf(x / 2**0.5) / 2
d1 = (r + s*s/2) / s
print("Black-Scholes Call:", S * N(d1) - K * exp(-r) * N(d1 - s))

# European vs American Put (1000 steps)
print("European Put:", tree(1000, -1)[0])
print("American Put:", tree(1000, -1, 1)[0])