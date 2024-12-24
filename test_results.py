from fixed_point_method import phi, fixed_point
from modified_newton_method import newton_modified
from secant_method import secant
from original_function import f
import time

# Função principal para rodar todos os métodos e criar a tabela comparativa
def tabela_comparativa(C, Q0, Q1, tol, max_iter):
    # Testando os métodos
    # Ponto Fixo
    start_time = time.time()
    root_fp, iter_fp = fixed_point(lambda Q: phi(Q, C), C, Q0, tol, max_iter)
    error_fp = abs(f(root_fp, C))
    tempo_fp = time.time() - start_time

    # Newton Modificado
    start_time = time.time()
    root_nm, iter_nm = newton_modified(C, Q0, tol, max_iter)
    error_nm = abs(f(root_nm, C))
    tempo_nm = time.time() - start_time

    # Secante
    start_time = time.time()
    root_sec, iter_sec = secant(C, Q0, Q1, tol, max_iter)
    error_sec = abs(f(root_sec, C))
    tempo_sec = time.time() - start_time

    # Exibindo a tabela comparativa
    print(f"{'Método':<20}{'Q Calculado':<15}{'Erro':<15}{'Tempo (s)':<15}{'Iterações'}")
    print("-" * 75)
    print(f"Ponto Fixo         {root_fp:<15.6f}{error_fp:<15.2e}{tempo_fp:<15.6f}{iter_fp:>7}")
    print(f"Newton Modificado  {root_nm:<15.6f}{error_nm:<15.2e}{tempo_nm:<15.6f}{iter_nm:>7}")
    print(f"Secante            {root_sec:<15.6f}{error_sec:<15.2e}{tempo_sec:<15.6f}{iter_sec:>7}")

# Teste
C = 1  # Valor de C
Q0 = 0.5  # Valor inicial para os métodos
Q1 = 0.6  # Segundo valor inicial para o método da Secante
tol = 1e-4  # Tolerância
max_iter = 100  # Número máximo de iterações

# Chamando a função para a tabela comparativa
tabela_comparativa(C, Q0, Q1, tol, max_iter)
