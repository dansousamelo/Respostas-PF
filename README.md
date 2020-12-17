# Respostas-PF

Questões elaboradas para o processo seletivo na Polícia Federal com o intuito de trabalhar no sistema de Integração e Cruzamento de dados Forenses - DELPHOS

## Questão 1
<p>Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', e caso exista, salve o valor dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.</p>

Entrada: ```lista = [{'nome': 'Daniel'}, {'nome': 'daniel'}, {'nome': 'Daniel'}, {'nome': 'João'}, {'nome': 'Maria'}]```
Saída: ```['Daniel', 'João', 'Maria']```

## Questão 2
<p>Dado um arquivo csv com delimitador <b>';'</b> e com o seguinte cabeçalho: id;nome;telefone;idade. Retorne uma lista com os registros ordenados por nome.</p>


Entrada:

```
Id;nome;telefone;idade
1;João;43383832;28
2;Maria;43839322;32
.
.
.
N;Zzzz;99999999;12
```

Saída:

```[{'id': '3', 'nome': 'Alice', 'telefone': '6122223331', 'idade': '21'}, {'id': '4', 'nome': 'Antônio', 'telefone': '6155555666', 'idade': '22'}, {'id': '2', 'nome': 'João', 'telefone': '123123123', 'idade': '19'}, {'id': '1', 'nome': 'Maria', 'telefone': '123123124', 'idade': '22'}]```

## Execução
Para executar basta rodar, por exemplo:
```python3 Q1.py```
