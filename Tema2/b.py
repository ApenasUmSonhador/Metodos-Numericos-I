import math

def f(Q, C):
    return C * math.exp(Q) - 4 * Q**2

def f_prime(Q, C):
    return C * math.exp(Q) - 8 * Q

def newton_modified(C, x0, tol=1e-4, max_iter=100):
    Q = x0
    for _ in range(max_iter):
        f_x0 = f(x0, C)
        f_prime_x0 = f_prime(x0, C)
        if f_prime_x0 == 0:
            raise ValueError("Derivative is zero, choose a different initial approximation.")
        Q = x0 - (f(Q, C) / f_prime_x0)
        if abs(Q - x0) < tol:
            break
        x0 = Q
    return Q

# Example usage
C = 1.0  # Example cost value in billion
x0 = 0.5  # Initial approximation
Q = newton_modified(C, x0)
print(Q)
if Q > 0.7:
    print("Quantidade de ingredientes inviável. Sendo {Q:.6f} toneladas")
else:
    print(f"Quantidade ideal de ingredientes: {Q:.6f} toneladas")