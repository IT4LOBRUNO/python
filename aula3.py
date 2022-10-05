# MANIPULANDO STRINGS
texto = "Técnico em Informática - Programação Orientada a Objetos"
print(texto)

#EXEMPLO DE FATIAMENTO
print(texto[3]) #Irá mostrar somente este indice
print(texto[5:]) #Irá mostrar tudo a partir deste indice

print(texto[:22]) #Irá mostrar do inicio até este indice
print(texto[11:22]) #Irá mostrar apenas este intervalo

#Analisando Strings
print(len(texto))#Funciona como um .length mas a variável deve ser passada como len(variável)
print(texto.lower())#Deixa todo o texto em minúsculo
print(texto.upper())#Deixa todo o texto em maiúsculo
print(texto.replace("Informática", "Mecânica"))
print(texto.replace(" ", "_"))

print("\n\n")#Quebra de linha (x2)
