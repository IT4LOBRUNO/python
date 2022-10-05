print("="*10, "Exemplo 5", "="*10)

for i in range(1,10):
    print(i)

print("\n\n")
for cont in range(1, 6):
    print(cont, end=" ")

print("\n\n")
idade = int(input("Qual a sua idade? "))
for i in range(1, idade + 1):
    print("*" * idade)