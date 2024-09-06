<h1>Pipeline de Dados em Python com Orientação a Objetos</h1>

Status: Finalizado ✔️

<b>Descrição:</b> Este projeto é um pipeline de dados desenvolvido com orientação a objetos. O objetivo é demonstrar a leitura de arquivos .csv, .json e através de APIs, tratamento e transformação dos dados, e também a gravação do arquivo utilizando Python. O pipeline inclui a exploração dos dados, processamento e a criação de um arquivo final processado.

<h2>Estrutura do Projeto</h2>

+ `.venv:` Contém o ambiente virtual configurado para o projeto.
+ `pipeline_dados_api:`
  + `data_frame:`
  + `notebooks:`
  + `scripts:`
    + `repos_creation.py:`
    + `repos_data.py:`
    + `repos_manipulation.py:`
      
+ `pipeline_dados_csv_json:`
  + `data_processed/:` Contém o arquivo final após o processamento dos dados.
  +  `data_raw/:` Contém arquivos .csv e .json utilizados como exemplo para o processamento de dados.
  + `notebooks/:` Contém um notebook Jupyter onde os dados são explorados, e soluções para leitura, transformação e gravação são desenvolvidas utilizando Python.
  + `scripts/:`
    + `merge_companies.py:` Script responsável pela leitura, tratamento e gravação dos dados.
    + `processing_data.py:` Contém todas as funções orientadas a objetos usadas para processamento dos dados.
