import math
from original_function import f
# Item b)
# Derivada de f(Q) em relação a Q: f'(Q) = C * e^Q - 8 * Q
def df_dQ(Q, C):
    return C * math.exp(Q) - 8 * Q

# Método de Newton Modificado
def newton_modified(C, Q0, tol, max_iter=100):
    Q = Q0
    for i in range(max_iter):
        df_Q = df_dQ(Q, C)
        if df_Q == 0:
            raise ValueError("Derivada em Q é zero! Método não pode ser aplicado.")
        Q_next = Q - f(Q, C) / df_Q
        if abs(Q_next - Q) < tol  or abs(f(Q_next, C)) < tol:
            return Q_next, i + 1
        Q = Q_next
    return Q, max_iter

if __name__ == "__main__":
    try:
        C = 1
        Q0 = 0.5
        tol = 1e-4
        max_iter = 100
        Q_root, iterations = newton_modified(C, Q0, tol, max_iter)

        print(f"Raiz encontrada: {Q_root}")
        print(f"Número de iterações: {iterations}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Erro: {e}")
