# Item a)
# Função auxiliar para o Método do Ponto Fixo
import math
from original_function import f, isViableMessage

def phi(Q, C):
    return math.sqrt(C * math.exp(Q) / 4)

# Método do Ponto Fixo
def fixed_point(phi, C, Q0, tol, max_iter=100):
    Q = Q0
    for i in range(max_iter):
        Q_next = phi(Q)
        if abs(Q_next - Q) < tol or abs(f(Q_next, C)) < tol:
            return Q_next, i + 1
        Q = Q_next
    raise ValueError("O Método do Ponto Fixo não convergiu.")


if __name__ == "__main__":
    try:
        C = 1
        Q0 = 0.5
        tol = 1e-4
        max_iter = 100

        Q_root, iterations = fixed_point(lambda Q: phi(Q, C), C, Q0, tol, max_iter)

        print(f"Raiz encontrada: {Q_root}")
        print(f"Número de iterações: {iterations}")
        print(isViableMessage(Q_root))
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Erro: {e}")
