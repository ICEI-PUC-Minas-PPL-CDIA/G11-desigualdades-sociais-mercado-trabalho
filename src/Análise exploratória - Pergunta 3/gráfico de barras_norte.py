import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel("Pergunta 3.xlsx", sheet_name="Planilha1")
df.columns = ['Estado', 'Escolaridade', 'Faixa_Salarial']

# Definir os estados da região Norte
norte_estados = [
    'Acre (AC)', 'Amazonas (AM)', 'Amapá (AP)', 'Pará (PA)', 
    'Rondônia (RO)', 'Roraima (RR)', 'Tocantins (TO)'
]

# Filtrar os dados da região Norte
df_norte = df[df['Estado'].isin(norte_estados)].dropna(subset=['Escolaridade', 'Faixa_Salarial'])

# Definir a ordem das faixas salariais
faixa_ordem = [
    'Menos de R$ 1.000/mês',
    'de R$ 1.001/mês a R$ 2.000/mês',
    'de R$ 2.001/mês a R$ 3.000/mês',
    'de R$ 3.001/mês a R$ 4.000/mês',
    'de R$ 4.001/mês a R$ 6.000/mês',
    'de R$ 6.001/mês a R$ 8.000/mês',
    'de R$ 8.001/mês a R$ 12.000/mês',
    'de R$ 12.001/mês a R$ 16.000/mês',
    'de R$ 16.001/mês a R$ 20.000/mês',
    'de R$ 20.001/mês a R$ 25.000/mês',
    'de R$ 25.001/mês a R$ 30.000/mês',
    'de R$ 30.001/mês a R$ 40.000/mês',
    'Acima de R$ 40.001/mês'
]

# Agrupar os dados
bar_data_norte = df_norte.groupby(['Escolaridade', 'Faixa_Salarial']).size().reset_index(name='Contagem')
bar_data_norte['Faixa_Salarial'] = pd.Categorical(bar_data_norte['Faixa_Salarial'], categories=faixa_ordem, ordered=True)
bar_data_norte = bar_data_norte.sort_values(by=['Escolaridade', 'Faixa_Salarial'])

# Criar o gráfico de barras
plt.figure(figsize=(14, 7))
sns.barplot(data=bar_data_norte, x='Faixa_Salarial', y='Contagem', hue='Escolaridade')
plt.title('Distribuição de Escolaridade por Faixa Salarial - Região Norte')
plt.xlabel('Faixa Salarial')
plt.ylabel('Número de Pessoas')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Escolaridade', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
