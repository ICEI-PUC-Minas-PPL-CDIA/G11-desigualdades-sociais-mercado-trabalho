import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar e preparar os dados (caso não tenha feito anteriormente)
file_path = "/mnt/data/Pergunta 2.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Planilha1')

# Renomear colunas
df.columns = ['Genero', 'Raca', 'Nivel', 'Faixa_Salarial', 'Tempo_Experiencia']

# Remover valores nulos nas colunas essenciais
df_clean = df.dropna(subset=['Genero', 'Raca', 'Nivel', 'Faixa_Salarial'])

# Mapeamento das faixas salariais para valores médios
faixa_mapping = {
    'Até R$ 2.000/mês': 1000,
    'de R$ 2.001/mês a R$ 4.000/mês': 3000,
    'de R$ 4.001/mês a R$ 6.000/mês': 5000,
    'de R$ 6.001/mês a R$ 8.000/mês': 7000,
    'de R$ 8.001/mês a R$ 12.000/mês': 10000,
    'de R$ 12.001/mês a R$ 16.000/mês': 14000,
    'de R$ 16.001/mês a R$ 20.000/mês': 18000,
    'de R$ 20.001/mês a R$ 25.000/mês': 22500,
    'Acima de R$ 25.000/mês': 27000
}

# Aplicar o mapeamento
df_clean['Salario_Medio'] = df_clean['Faixa_Salarial'].map(faixa_mapping)

# Filtrar apenas gêneros válidos
df_filtered = df_clean[df_clean['Genero'].isin(['Masculino', 'Feminino'])]

# Agrupar por Nível, Gênero e Raça e calcular o salário médio
df_grouped = (
    df_filtered
    .groupby(['Nivel', 'Genero', 'Raca'])['Salario_Medio']
    .mean()
    .reset_index()
)

# Plotar gráfico de barras agrupadas
plt.figure(figsize=(16, 8))
sns.set(style="whitegrid")

sns.barplot(
    data=df_grouped,
    x='Nivel',
    y='Salario_Medio',
    hue='Genero',
    ci=None,
    palette='Set1',
    dodge=True
)

plt.title('Salário Médio por Nível de Cargo, Gênero e Raça', fontsize=16)
plt.xlabel('Nível de Cargo')
plt.ylabel('Salário Médio (R$)')
plt.legend(title='Gênero')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

