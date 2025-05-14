# Aplicar remoção de outliers usando o critério IQR
df_iqr_filtered = df_encoded.copy()

# Selecionar apenas colunas numéricas para o IQR
numeric_cols = df_iqr_filtered.select_dtypes(include=['int64', 'float64']).columns.tolist()
numeric_cols.remove('Nivel')  # Não aplicar IQR no target

# Remover outliers
for col in numeric_cols:
    Q1 = df_iqr_filtered[col].quantile(0.25)
    Q3 = df_iqr_filtered[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_iqr_filtered = df_iqr_filtered[(df_iqr_filtered[col] >= lower_bound) & (df_iqr_filtered[col] <= upper_bound)]

# Salvar a base tratada sem outliers
output_iqr_path = "/mnt/data/Base_KNN_Sem_Outliers.xlsx"
df_iqr_filtered.to_excel(output_iqr_path, index=False)

# Exibir resultado ao usuário
display_dataframe_to_user(name="Base KNN Sem Outliers (IQR)", dataframe=df_iqr_filtered)

output_iqr_path
