import math
import time

# Função original: f(Q) = C * e^Q - 4 * Q^2
def f(Q, C):
    return C * math.exp(Q) - 4 * Q**2

# Mensagem de viabilidade, via de regra, se Q <= 0.7, a produção é viável
def isViableMessage(Q):
    if Q <= 0.7:
        return "A produção é viável."
    return "A produção é inviável devido à falta de espaço, causando prejuízos financeiros."