import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
data = pd.read_csv(url, sep=';')

data = data.query("Tipo == 'Apartamento'")
data = data.fillna(0)

index_to_remove = data.query('Valor == 0 | Condominio == 0').index
data = data.drop(index_to_remove, axis=0)
data = data.drop('Tipo', axis=1)

selection1 = data['Quartos'] == 1
selection2 = data['Valor'] < 1200
df_filter_1 = (selection1) & (selection2)

selection3 = (data['Quartos'] >= 2) & (data['Valor'] < 3000) & (data['Area'] > 70)
df_filter_2 = data[selection3]

data.to_csv('Data/data_apartamentos.csv',index=False, sep=';')
df_filter_1.to_csv('Data/data_apartamentos_with_filter_1.csv',index=False, sep=';')
df_filter_2.to_csv('Data/data_apartamentos_with_filter_2.csv',index=False, sep=';')