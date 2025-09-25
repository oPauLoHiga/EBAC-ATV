import pandas as pd

lista_nomes = ['Ana', 'Marcos', 'Carlos']
print('Lista de nomes: \n', lista_nomes)
print('Lista Elemento na Lista: \n', lista_nomes[0])


dicionario_pessoa = {
    'nome': 'Ana',
    'idade': 20,
    'cidade': 'São Paulo'
}

print('Dicionario de pessoa: \n', dicionario_pessoa)
print('Atributo do Dicionario: \n', dicionario_pessoa.get('nome'))


dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'São Paulo'},
    {'nome':'Marcos', 'idade': 25, 'cidade': 'São José dos Campos'},
    {'nome':'Carlos','idade': 35, 'cidade': 'Rio de janeiro'}
]

df = pd.DataFrame(dados)
print('DataFrame: \n', df)

print(df['nome'])

print(df[['nome','idade']])

print('Primeira linha \n', df.iloc[0])

df['salario'] = [4100, 3600, 5200]

df.loc[len(df)]={
    'nome': 'João',
    'idade': 30,
    'cidade': 'Taubaté',
    'salario': 4800
}

print('DataFrame: \n', df)

df.drop('salario', axis=1, inplace=True)

filtro_idade = df[df['idade'] >= 30]
print('Filtro \n', filtro_idade)

df.to_csv('dados.csv', index=False)

df_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n',df_lido)


