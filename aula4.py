nota1 = float(input("Escreva a nota 1 "))
nota2 = float(input("Escreva a nota 2 "))
nota3 = float(input("Escreva a nota 3 "))
notaMedia = (nota1+nota2+nota3)/3

if notaMedia >= 7:
    print("Aluno Aprovado!")
elif notaMedia >= 9:
    print("Aluno Aprovado com Honra!")
else:
    print("Aluno Reprovado!")
