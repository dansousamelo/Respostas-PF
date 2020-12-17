# Lista com os nomes
lista = [{'nome': 'Daniel'}, {'nome': 'daniel'}, {'nome': 'Daniel'}, {'nome': 'João'}, {'nome': 'Maria'}]

# Lista final
lista_final = []

''' Verifica-se se existe a chave nome em cada um dos dicionários 
    
    O nome é convertido com a primeira letra em caixa alta para evitar
    casos como: 'Daniel' e 'daniel'
    
    Feita as verificações adiciona-se na lista final'''

for i in lista:
  valor = i.get('nome')
  if valor and lista_final.count(valor.capitalize()) == 0:
    lista_final.append(valor)
  else:
    continue
  
print(lista_final)
