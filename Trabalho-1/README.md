# Trabalho I

## Descrição do Problema
A indústria de alimentos busca otimizar seus processos para maximizar a lucratividade. Uma empresa deseja determinar a quantidade ideal de ingredientes para um novo produto, utilizando a função de custo de produção `f(Q) = C * e^Q - 4 * Q^2`, onde:
- `C` é o custo dos ingredientes (em bilhões), conforme a escolha do fornecedor.
- `Q` é a quantidade de ingredientes comprada (em toneladas), variando conforme o valor de `C`.

Se `Q` ultrapassar 0,7 toneladas, a produção se torna inviável devido à falta de espaço, causando prejuízos financeiros.

## Objetivos
Desenvolver um sistema para calcular o valor de `Q` que atenda aos seguintes requisitos:
1. Implementar algoritmo para calcular `Q` pelo método do Ponto Fixo com uma função `Φ` que converge.
2. Implementar algoritmo para calcular `Q` pelo método de Newton modificado.
3. Implementar algoritmo para calcular `Q` pelo método da Secante original.
4. Testar os resultados utilizando `C = 1`, `Q_0 = 0,5` e `ε = 10^-4`.
5. Fornecer um quadro resposta com `Q` calculado para cada método, comparando resposta, acurácia (erro), tempo, número de iterações, etc.
6. Fornecer um quadro comparativo com todos os dados para cada método.
7. Analisar o efeito da variação do valor de `C` para cada método, comparando resposta, acurácia (erro), tempo, número de iterações, etc.

## Dados de Entrada
- `n`: número de valores de `C`
- `C`: valores de custo dos ingredientes para cada `n`
- `ε`: precisão

## Dados de Saída
- Quadros resposta com `Q` e erro para cada `C` e método
- Quadro comparativo com todos os dados para cada método

## Resultados
Em todos os itens e resultados, indicar se a empresa terá ou não falta de espaço e prejuízo financeiro.

## Estrutura do Projeto
A estrutura do projeto segue a seguinte organização:
```yaml
Trabalho-1/
├── data_analysis_by_C_var.py      # Análise minuciosa dos efeitos da variação de C
├── data_analysis.py               # Análise mais minuciosa dos resultador por método
├── fixed_point_method.py          # Arquivo com o método de ponto fixo
├── modified_newton_method.py      # Arquivo com o método de Newton modificado
├── original_function.py           # Arquivo com a função original do problema
├── README.md                      # Documentação do Trabalho-1
├── secant_method.py               # Arquivo com o método da secante
└── test_results.py                # Testes e comparação dos resultados por método
```

## Como Executar
1. Clone o repositório.
2. Execute os scripts de cada método para calcular `Q`.
3. Ou execute os scripts de `data_analysis` para uma melhor análise dos dados.  

---

### Resumo do README
Este README é organizado para facilitar a compreensão do propósito do projeto, a estrutura do código, e os passos necessários para configuração e execução. Também inclui exemplos claros para ajudar novos usuários e desenvolvedores a começarem rapidamente.
