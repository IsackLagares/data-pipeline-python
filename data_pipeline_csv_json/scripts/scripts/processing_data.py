import json
import csv

class Data:

    def __init__(self, data):
        self.data = data
        self.columns_name = self.__get_columns()

    # Funcao para ler arquivo json
    def __read_json(path):
        data_json = []
        with open(path, 'r') as file:
            data_json = json.load(file)
        return data_json

    # Funcao para ler arquivo csv
    def __read_csv(path):
        data_csv = []
        with open(path, 'r') as file:
            spamreader= csv.DictReader(file, delimiter=',')

            for row in spamreader:
                data_csv.append(row)
        return data_csv

    # Funcao para ler o arquivo no seu respectivo type
    @classmethod
    def read_data(cls, path, type_data):
        data = []
        if type_data == 'csv':
            data = cls.__read_csv(path)
        elif type_data == 'json':
            data = cls.__read_json(path)
        return cls(data)

    # Funcao para armazenar as colunas
    def __get_columns(self):
        return list(self.data[-1].keys())

    # Funcao para renomear colunas
    def rename_columns(self, key_mapping):
        new_data_csv = [{key_mapping.get(old_key): new_key for old_key, new_key in old_dict.items()} for old_dict in self.data]
        self.data = new_data_csv
        self.columns_name = self.__get_columns()

    # Funcao para unir os dados
    def join(dataA, dataB):
        combined_list = []
        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)
        return Data(combined_list)

    # Funcao para tratar os dados ausentes
    def __transforming_data_table(self):
        combined_data_table = [self.columns_name]

        for row in self.data:
            line_temp = []
            for column in self.columns_name:
                line_temp.append(row.get(column, 'Valor Indisponível'))
            combined_data_table.append(line_temp)
        return combined_data_table

    # Funcao para salvar os Dados
    def save_data(self, path):
        combined_data_table = self.__transforming_data_table()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data_table)