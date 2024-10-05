from processing_data import Data

# Extracting Data

path_json = 'pipeline_dados_csv_json/data_raw/dados_empresaA.json'
path_csv = 'pipeline_dados_csv_json/data_raw/dados_empresaB.csv'

companieA_data = Data.read_data(path_json, 'json')
companieB_data = Data.read_data(path_csv, 'csv')


# Transforming Data

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

companieB_data.rename_columns(key_mapping)

merged_data = Data.join(companieA_data, companieB_data)


# Loading Data

end_path = 'pipeline_dados_csv_json/data_processed/data_processed.csv'
merged_data.save_data(end_path)
print(end_path)


