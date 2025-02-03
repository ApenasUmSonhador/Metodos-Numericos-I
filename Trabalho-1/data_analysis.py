import math
import time
from original_function import f, isViableMessage
from fixed_point_method import phi
from modified_newton_method import df_dQ

# Método do Ponto Fixo
def fixed_point(phi, Q0, tol=1e-4, max_iter=100):
    Q = Q0
    Q_values = []
    for i in range(max_iter):
        start_time = time.time()
        Q_next = phi(Q)
        error = min(abs(Q_next - Q), abs(f(Q_next, C)))
        exec_time = time.time() - start_time
        Q_values.append((Q, error, exec_time))
        if error < tol:
            return Q_next, i + 1, Q_values
        Q = Q_next
    raise ValueError("O Método do Ponto Fixo não convergiu.")

# Método de Newton Modificado
def newton_modified(C, Q0, tol=1e-4, max_iter=100):
    Q = Q0
    Q_values = []
    for i in range(max_iter):
        start_time = time.time()
        df_Q0 = df_dQ(Q, C)
        if df_Q0 == 0:
            raise ValueError("Derivada em Q0 é zero! Método não pode ser aplicado.")
        Q_next = Q - f(Q, C) / df_Q0
        error = min(abs(Q_next - Q), abs(f(Q_next, C)))
        exec_time = time.time() - start_time
        Q_values.append((Q, error, exec_time))
        if error < tol:
            return Q_next, i + 1, Q_values
        Q = Q_next
    return Q, max_iter, Q_values

# Método da Secante
def secant(C, Q0, Q1, tol=1e-4, max_iter=100):
    Q_values = [(Q0, None, None), (Q1, None, None)]
    for i in range(max_iter):
        start_time = time.time()
        fQ0 = f(Q0, C)
        fQ1 = f(Q1, C)
        if abs(fQ1 - fQ0) < tol:
            raise ValueError("Diferença muito pequena entre f(Q0) e f(Q1), método falhou.")
        Q_next = Q1 - fQ1 * (Q1 - Q0) / (fQ1 - fQ0)
        error = min(abs(Q_next - Q1), abs(f(Q_next, C)))
        exec_time = time.time() - start_time
        Q_values.append((Q_next, error, exec_time))
        if error < tol:
            return Q_next, i + 1, Q_values
        Q0, Q1 = Q1, Q_next
    return Q1, max_iter, Q_values

# Item f)
# Função principal para rodar todos os métodos e criar a tabela comparativa
def tabela_comparativa(C, Q0, Q1, tol=1e-4, max_iter=100):
    # Testando os métodos
    # Ponto Fixo
    root_fp, iter_fp, values_fp = fixed_point(lambda Q: phi(Q, C), Q0, tol, max_iter)

    # Newton Modificado
    root_nm, iter_nm, values_nm = newton_modified(C, Q0, tol, max_iter)

    # Secante
    root_sec, iter_sec, values_sec = secant(C, Q0, Q1, tol, max_iter)

    # Exibindo a tabela comparativa
    print(f"{'Iteração':<10}{'Método':<20}{'Q Calculado':<15}{'Erro':<15}{'Tempo (s)':<10}")
    print("-" * 70) 
    for i, (Q, error, exec_time) in enumerate(values_fp, 1):
        print(f"{i:<10}{'Ponto Fixo':<20}{Q:<15.8f}{error if error is not None else 0.0:<15.2e}{exec_time if exec_time is not None else 0.0:<10.8f}")
    print("Conclusão:", isViableMessage(root_fp))
    print("-" * 70)
    for i, (Q, error, exec_time) in enumerate(values_nm, 1):
        print(f"{i:<10}{'Newton Modificado':<20}{Q:<15.8f}{error if error is not None else 0.0:<15.2e}{exec_time if exec_time is not None else 0.0:<10.8f}")
    print("Conclusão:", isViableMessage(root_nm))
    print("-" * 70)
    for i, (Q, error, exec_time) in enumerate(values_sec, 1):
        print(f"{i:<10}{'Secante':<20}{Q:<15.8f}{error if error is not None else 0.0:<15.2e}{exec_time if exec_time is not None else 0.0:<10.8f}")
    print("Conclusão:", isViableMessage(root_sec))
    

# Teste
C = 1  # Valor de C
Q0 = 0.5  # Valor inicial para os métodos
Q1 = 0.6  # Segundo valor inicial para o método da Secante

# Chamando a função para a tabela comparativa
tabela_comparativa(C, Q0, Q1)