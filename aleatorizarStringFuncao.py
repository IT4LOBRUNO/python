import random
def aleatorizar (texto):
    resultado = ''.join(random.sample(texto, len(texto)))
    print(resultado)
aleatorizar("Teste")