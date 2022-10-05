paisA = 80000
paisB = 200000
ano = 0
while paisA < paisB:
    paisA = paisA + paisA * 0.03
    paisB = paisB + paisB * 0.015
    ano += 1
print(ano)