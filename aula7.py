print("-"*10, "Exemplo 7", "-"*10)

pessoas =["João", "Maria", "Lucas", "Fulano", "Mario", "Lais"]
print(type(pessoas))
pessoas.append("Cicrano")#Adiciona no ultimo elemento
pessoas.pop()#Remove o ultimo item da lista
pessoas.pop(2)#remove no valor desse indice
pessoas.remove("João")#Remove este elemento
pessoas.insert(2, "Clovis")# Seleciona um indice para inserir um item
u=0

if "Clovis" in pessoas:
    pessoas.remove("Clovis")
    
for i in pessoas:
    u += 1
    print(f"{u}- ",i)