import pandas as pd

# Caminho do arquivo original
file_path = "State of Data 2023 - atributos principais.xlsx"

# Carrega todas as planilhas do Excel
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

# Cria um dicionário para armazenar os DataFrames limpos
cleaned_sheets = {}

# Itera por cada planilha e remove linhas com valores ausentes
for sheet in sheet_names:
    df = xls.parse(sheet)
    df_cleaned = df.dropna()  # Remove linhas com valores faltantes
    cleaned_sheets[sheet] = df_cleaned

# Define o caminho de saída para o novo arquivo Excel
output_path = "State_of_Data_2023_sem_nulos.xlsx"

# Salva as planilhas limpas no novo arquivo
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for sheet_name, df_cleaned in cleaned_sheets.items():
        df_cleaned.to_excel(writer, sheet_name=sheet_name, index=False)
