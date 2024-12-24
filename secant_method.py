from original_function import f, isViableMessage
# Item c)
# Método da Secante
def secant(C, Q0, Q1, tol, max_iter=100):
    for i in range(max_iter):
        fQ0 = f(Q0, C)
        fQ1 = f(Q1, C)
        if abs(fQ1 - fQ0) < tol:
            raise ValueError("Diferença muito pequena entre f(Q0) e f(Q1), método falhou.")
        Q_next = Q1 - fQ1 * (Q1 - Q0) / (fQ1 - fQ0)
        if abs(Q_next - Q1) < tol or abs(f(Q_next, C)) < tol:
            return Q_next, i + 1
        Q0, Q1 = Q1, Q_next
    return Q1, max_iter

if __name__ == "__main__":
    try:
        C = 1
        Q0 = 0.5
        Q1 = 0.6
        tol = 1e-4
        max_iter = 100

        Q_root, iterations = secant(C, Q0, Q1, tol, max_iter)

        print(f"Raiz encontrada: {Q_root}")
        print(f"Número de iterações: {iterations}")
        print(isViableMessage(Q_root))
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Erro: {e}")
