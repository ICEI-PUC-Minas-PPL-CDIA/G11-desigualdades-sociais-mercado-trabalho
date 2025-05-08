import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o Excel
df = pd.read_excel("State of Data 2023 - atributos principais.xlsx", sheet_name="Planilha1")

# Renomear colunas
df.columns = [
    "ID", "Idade", "Faixa_Idade", "Genero", "Raca", "PCD", "Estado",
    "Nivel_Ensino", "Nivel_Profissional", "Faixa_Salarial", "Experiencia"
]

# Converter faixas salariais em valores médios
faixa_salarial_media = {
    'Menos de R$ 1.000/mês': 500,
    'de R$ 101/mês a R$ 2.000/mês': 1050,
    'de R$ 1.001/mês a R$ 2.000/mês': 1500,
    'de R$ 2.001/mês a R$ 3.000/mês': 2500,
    'de R$ 3.001/mês a R$ 4.000/mês': 3500,
    'de R$ 4.001/mês a R$ 6.000/mês': 5000,
    'de R$ 6.001/mês a R$ 8.000/mês': 7000,
    'de R$ 8.001/mês a R$ 12.000/mês': 10000,
    'de R$ 12.001/mês a R$ 16.000/mês': 14000,
    'de R$ 16.001/mês a R$ 20.000/mês': 18000,
    'de R$ 20.001/mês a R$ 25.000/mês': 22500,
    'de R$ 25.001/mês a R$ 30.000/mês': 27500,
    'de R$ 30.001/mês a R$ 40.000/mês': 35000,
    'Acima de R$ 40.001/mês': 45000
}
df["Salario_Medio"] = df["Faixa_Salarial"].map(faixa_salarial_media)

# Mapear estados para regiões
estado_para_regiao = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste',
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro-Oeste', 'GO': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

# Extrair sigla do estado e mapear região
df["Sigla"] = df["Estado"].str.extract(r'\((\w{2})\)')
df["Regiao"] = df["Sigla"].map(estado_para_regiao)

# Filtrar dados válidos
df_valid = df[df["Salario_Medio"].notna() & df["Regiao"].notna() & df["Genero"].notna()]

# Remover "Outro" e "Prefiro não informar"
df_valid_filtrado = df_valid[~df_valid["Genero"].isin(["Outro", "Prefiro não informar"])]

# Agrupar por região e gênero
salario_por_regiao_genero_filtrado = df_valid_filtrado.groupby(["Regiao", "Genero"])["Salario_Medio"].mean().reset_index()

# Plotar o gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=salario_por_regiao_genero_filtrado, x="Regiao", y="Salario_Medio", hue="Genero")
plt.title("Salário Médio por Gênero em Cada Região do Brasil (excluindo 'Outro' e 'Prefiro não informar')")
plt.ylabel("Salário Médio (R$)")
plt.xlabel("Região")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
