import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo Excel (caso necessário)
file_path = "/mnt/data/Pergunta 2.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('Planilha1')

# Renomear colunas
df.columns = ['Genero', 'Raca', 'Nivel', 'Faixa_Salarial', 'Tempo_Experiencia']

# Limpeza de dados
df_clean = df.dropna(subset=['Genero', 'Raca', 'Nivel', 'Faixa_Salarial'])

# Mapeamento das faixas salariais para valores médios (R$)
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

# Aplicar mapeamento de salário
df_clean['Salario_Medio'] = df_clean['Faixa_Salarial'].map(faixa_mapping)

# Filtrar apenas gêneros válidos
df_filtered = df_clean[df_clean['Genero'].isin(['Masculino', 'Feminino'])]

# Excluir categorias de raça "Prefiro não informar" e "Outra"
df_filtered_raca = df_filtered[~df_filtered['Raca'].isin(['Prefiro não informar', 'Outra'])]

# Agrupar por Nível e Raça para obter salário médio
df_grouped_raca_clean = (
    df_filtered_raca
    .groupby(['Nivel', 'Raca'])['Salario_Medio']
    .mean()
    .reset_index()
)

# Plotar gráfico
sns.set(style="whitegrid")
plt.figure(figsize=(16, 8))

sns.barplot(
    data=df_grouped_raca_clean,
    x='Nivel',
    y='Salario_Medio',
    hue='Raca',
    ci=None,
    palette='tab10',
    dodge=True
)

plt.title('Salário Médio por Nível de Cargo e Raça/Cor/Etnia (Sem "Prefiro não informar" e "Outra")', fontsize=16)
plt.xlabel('Nível de Cargo')
plt.ylabel('Salário Médio (R$)')
plt.legend(title='Raça/Cor/Etnia', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

