import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados da contagem final
dados = {
    "Menos de 1 ano": 476,
    "de 1 a 2 anos": 1201,
    "de 3 a 4 anos": 1109,
    "de 4 a 6 anos": 463,
    "de 7 a 10 anos": 429,
    "Mais de 10 anos": 557,
    "Não tenho experiência na área de dados": 162
}

# Converter para DataFrame
df_grafico = pd.DataFrame(list(dados.items()), columns=["Faixa de Experiência", "Quantidade"])

# Definir a ordem desejada
ordem = [
    "Menos de 1 ano",
    "de 1 a 2 anos",
    "de 3 a 4 anos",
    "de 4 a 6 anos",
    "de 7 a 10 anos",
    "Mais de 10 anos",
    "Não tenho experiência na área de dados"
]
df_grafico = df_grafico.set_index("Faixa de Experiência").loc[ordem].reset_index()

# Criar o gráfico com seaborn
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
grafico = sns.barplot(
    x="Quantidade",
    y="Faixa de Experiência",
    data=df_grafico,
    palette="viridis"
)

# Título e rótulos
plt.title("Distribuição de Experiência na Área de Dados", fontsize=14)
plt.xlabel("Quantidade de Respostas")
plt.ylabel("Faixa de Experiência")

# Adicionar os valores ao lado das barras
for index, value in enumerate(df_grafico["Quantidade"]):
    plt.text(value + 10, index, str(value), va='center')

plt.tight_layout()
plt.show()
