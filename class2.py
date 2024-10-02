import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
data = pd.read_csv(url, sep=';')

tipos = data['Tipo'].unique()
comercial_real_states = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

data = data.query('@comercial_real_states not in Tipo')

mean_per_tipo = data.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
print(mean_per_tipo)

mean_per_tipo.plot(kind='barh', figsize=(14, 10), color ='purple')
plt.show()

print(data['Tipo'].unique())
print(data['Tipo'].value_counts())

data_percent_tipo = data['Tipo'].value_counts(normalize=True).to_frame().sort_values('proportion')

data_percent_tipo.plot(kind='bar', figsize=(14, 10), color ='green', edgecolor='black',
                        xlabel = 'Tipos', ylabel = 'Percentual')
plt.show()