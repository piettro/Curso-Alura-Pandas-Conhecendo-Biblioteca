import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
data = pd.read_csv(url, sep=';')

print(data.head())
print(f'Rows: {data.shape[0]}, Columns: {data.shape[1]}')
print(f'Columns name: {data.columns}')
print(data.info())

print(data['Tipo'])
print(data[['Quartos','Valor']])