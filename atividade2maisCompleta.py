nascimento = input("Informe sua data de nascimento(DD/MM/AAAA")
dias = float(nascimento[0:2])
mes = float(nascimento[3:5])
ano = float(nascimento[6:12])

from datetime import date
data = date.today()

diaAtual = data[9:10]
mesAtual = data[6:8]
anoAtual = data[1:5]

anosVividos = anoAtual - ano
mesesVividos = mesAtual - mes
if mesesVividos < 0:
    mesesTotais = 12 + mesesVividos 
diasVividos = diaAtual - dias
anosBissextos = anosVividos / 4

qtdAnos = anosVividos * 365 + mesesVividos*30 + diasVividos + anosBissextos
print(f"Você viveu {anosVividos} anos, {mesesTotais} meses, {diasVividos} dias, com um total de {qtdAnos} Dias ")
