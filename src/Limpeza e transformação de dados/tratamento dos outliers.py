import pandas as pd
import numpy as np
from scipy import stats

# Caminho do arquivo de entrada
file_path = "State_of_Data_2023_para tratamento.xlsx"

# Carregar o arquivo Excel
df = pd.read_excel(file_path)

# Selecionar apenas colunas numéricas
numeric_cols = df.select_dtypes(include=[np.number]).columns

# Calcular o Z-score e identificar os outliers
z_scores = np.abs(stats.zscore(df[numeric_cols], nan_policy='omit'))

# Manter apenas as linhas que não possuem outliers (Z < 3)
filtered_df = df[(z_scores < 3).all(axis=1)]

# Salvar o novo DataFrame em um novo arquivo Excel
output_path = "dados_sem_outliers.xlsx"
filtered_df.to_excel(output_path, index=False)
