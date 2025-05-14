from sklearn.preprocessing import LabelEncoder

# Copiar o dataframe original
df_encoded = df_scaled.copy()

# Identificar colunas categóricas (não numéricas)
categorical_cols = df_encoded.select_dtypes(include=['object', 'category']).columns.tolist()

# Aplicar LabelEncoder em cada coluna categórica
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    label_encoders[col] = le  # Armazena o encoder caso precise reverter

# Salvar o dataframe com variáveis categóricas tratadas
encoded_output_path = "/mnt/data/Base_KNN_Categorica_Tratada.xlsx"
df_encoded.to_excel(encoded_output_path, index=False)

# Exibir resultado ao usuário
display_dataframe_to_user(name="Base com Variáveis Categóricas Tratadas", dataframe=df_encoded)

encoded_output_path
