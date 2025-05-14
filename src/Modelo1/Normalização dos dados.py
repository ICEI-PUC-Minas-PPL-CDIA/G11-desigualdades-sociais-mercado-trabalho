import pandas as pd
from sklearn.preprocessing import StandardScaler
from ace_tools import display_dataframe_to_user

# Caminho do arquivo
file_path = "/mnt/data/Base_KNN_Reduzida.xlsx"

# Carregar a base de dados
df = pd.read_excel(file_path)

# Remover a primeira coluna se for um índice desnecessário
if df.columns[0].lower() in ['id', 'indice', 'index']:
    df = df.iloc[:, 1:]

# Separar variáveis numéricas
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Normalizar os dados numéricos com StandardScaler
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Salvar o resultado em um novo arquivo Excel
output_path = "/mnt/data/Base_KNN_Normalizada.xlsx"
df_scaled.to_excel(output_path, index=False)

# Exibir os dados normalizados ao usuário
display_dataframe_to_user(name="Base KNN Normalizada", dataframe=df_scaled)

output_path
