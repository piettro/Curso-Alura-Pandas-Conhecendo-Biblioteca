import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
data = pd.read_csv(url, sep=';')
data.fillna(0,inplace = True)

data['Valor_per_month'] = data['Valor'] + data['Condominio']
data['Valor_per_year'] = data['Valor_por_mes'] * 12 + data['IPTU']
data['Decription'] = data['Tipo'] + ' em ' + data['Bairro'] + ' com ' + \
                                        data['Quartos'].astype(str) + ' quarto(s) ' + \
                                        ' e ' + data['Vagas'].astype(str) + ' vaga(s) de garagem.'
data['Has_suite'] = data['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")

data.to_csv('Data/data_apartamentos_with_new_columns.csv',index=False, sep=';')