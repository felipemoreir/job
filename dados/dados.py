import json
with open("dados.json") as arquivo:
    dados = json.load(arquivo)

valor_dif_zero = [dicionario['valor'] for dicionario in dados if dicionario['valor']!=0]
tamanho=len(valor_dif_zero)
soma= sum(valor_dif_zero)
menor = min(valor_dif_zero )
maior = max(valor_dif_zero )
media = soma/tamanho
contador = 0


for dicionario in dados:
    if dicionario['valor']== menor:
        print("o dia que menos vendeu foi:",dicionario['dia']," o valor vendido foi:", menor)
        break
for dicionario in dados:
    if dicionario['valor']== maior:
        print("o dia que mais vendeu foi:",dicionario['dia']," o valor vendido foi:", maior)
        break
for dicionario in dados:
    if dicionario['valor']> media:
        contador += 1
        
        
print("dias do mes que teve o faturamento superior a media mensal:",contador)
