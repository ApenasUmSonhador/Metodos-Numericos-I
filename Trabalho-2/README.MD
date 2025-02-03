# Trabalho II

## Descrição do Problema
A análise de dados lineares é largamente utilizada em previsões do mercado financeiro e da bolsa de valores. Assuma que as variações percentuais de preço de várias ações são dadas por `A * p`, onde `p1, p2, ..., pn` são os preços das ações e `A` um parâmetro fornecido, como o fator de ajuste ou uma taxa de crescimento. Caso uma variação percentual passe de 3%, a ação pode estar sujeita a grandes flutuações ou riscos elevados.

Os preços das ações podem ser calculados através da solução do sistema linear `Cp = v`, onde `C` é uma matriz de coeficientes que relaciona os retornos de várias ações a diferentes indicadores econômicos e `v` é um vetor que representa o crescimento esperado para cada ação. Tal sistema pode ser resolvido pela regra de Cramer, onde cada preço é dado por `pi = det(Ci) / det(C)`, onde `det(C)` é o determinante da matriz dos coeficientes `C` e `det(Ci)` é o determinante da matriz obtida trocando-se a coluna `i` da matriz `C` pelo vetor `v` dos termos independentes.

## Objetivos
Desenvolver um sistema para calcular os preços das ações que atenda aos seguintes requisitos:
1. Implementar algoritmo para calcular `{p}` pelo método de Fatoração LU normal.
2. Implementar algoritmo para achar determinantes pelo método de Gauss-Jordan e depois `{p}` por Cramer.
3. Implementar algoritmo para calcular `{p}` pelo método de Gauss-Seidel.
4. Calibrar sistema desenvolvido usando, como padrão, valor `a = 1`, a matriz `[C]` e o vetor `{v}` dados abaixo.
5. Fornecer quadro resposta para cada um dos métodos implementados, variando os valores de `[C]` e de `{v}`.
6. Analisar o que vai acontecer com as várias ações consideradas, para o sistema mencionado abaixo.

## Dados de Entrada
- `n`: número de ações
- `a`: parâmetro de ajuste
- `[C]`: termos da matriz de coeficientes `C` de dimensão `n x n`
- `{v}`: termos do vetor `v` de dimensão `n x 1`

## Dados de Saída
- Termos de `{p}` de dimensão `n x 1` que representam os `n` preços `p1, p2, ..., pn`

## Resultados
Em todos os itens e resultados, indicar se a ação estará sujeita a grandes flutuações ou riscos elevados.

## Estrutura do Projeto
A estrutura do projeto segue a seguinte organização:
```yaml
Trabalho-2/
├── cramer_method.py               # Algoritmo para calcular {p} pela regra de Cramer
├── gauss_jordan_determinant.py    # Algoritmo para calcular determinantes pelo método de Gauss-Jordan
├── gauss_seidel_method.py         # Algoritmo para calcular {p} pelo método de Gauss-Seidel
├── lu_factorization_method.py     # Algoritmo para calcular {p} pelo método de Fatoração LU
├── README.md                      # Documentação do Trabalho-2
├── test_results.py                # Testes e comparação dos resultados por método
└── data_analysis.py               # Análise dos resultados variando os valores de [C] e {v}
```

## Como Executar
1. Clone o repositório.
2. Execute os scripts de cada método para calcular `{p}`.
3. Ou execute os scripts de `data_analysis` para uma melhor análise dos dados.

---

### Resumo do README
Este README é organizado para facilitar a compreensão do propósito do projeto, a estrutura do código, e os passos necessários para configuração e execução. Também inclui exemplos claros para ajudar novos usuários e desenvolvedores a começarem rapidamente.
