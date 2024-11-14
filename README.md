<h1>Pipeline de Dados em Python com Orientação a Objetos</h1>

Status: Finalizado ✔️

<b>Descrição:</b> Este projeto é um pipeline de dados desenvolvido com orientação a objetos. O objetivo é demonstrar a leitura de arquivos .csv, .json e através de APIs, tratamento e transformação dos dados, e também a gravação do arquivo utilizando Python. O pipeline inclui a exploração dos dados, processamento e a criação de um arquivo final processado.

<h2>Estrutura do Projeto</h2>

+ `data_pipeline_api:` Pipeline de Dados através de API
  + `data_frame:` Contém o arquivo final após o processamento dos dados
  + `notebooks:` Contém um notebook Jupyter onde os dados são explorados, e soluções para leitura, transformação e gravação são desenvolvidas utilizando Python.
  + `scripts:`
    + `repos_creation.py:` Script responsável por criar o repositório.
    + `repos_data.py:` Script responsável por salvar os DataFrames no repositório.
    + `repos_manipulation.py:` Script responsável pela manipulação dos dados.
      
+ `data_pipeline_csv_json:` Pipeline de Dados através de arquivos .csv e .json
  + `data_processed/:` Contém o arquivo final após o processamento dos dados.
  +  `data_raw/:` Contém arquivos .csv e .json utilizados como exemplo para o processamento de dados.
  + `notebooks/:` Contém um notebook Jupyter onde os dados são explorados, e soluções para leitura, transformação e gravação são desenvolvidas utilizando Python.
  + `scripts/:`
    + `merge_companies.py:` Script responsável pela leitura, tratamento e gravação dos dados.
    + `processing_data.py:` Contém todas as funções orientadas a objetos usadas para processamento dos dados.
