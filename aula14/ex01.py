import pandas as pd 
import polars as pl 
from datetime import datetime
import os 

ENDERECO_DADOS = './../DADOS/'

try: 
    inicio = datetime.now()
    print('Obtendo dados de Bolsa Família')

    df_bolsa_familia = None 
    lista_arquivos = [] # lista principal do processamento 

    lista_diretorio_arquivos = os.listdir(ENDERECO_DADOS)
    # print(lista_diretorio_arquivos)
    for arquivo in lista_diretorio_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    # Obtendo os dataframe 

    for arquivo in lista_arquivos: 
        print(f'Processando o arquivo {arquivo}...')
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso8859-1')
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso8859-1')

        if df_bolsa_familia is None: 
            df_bolsa_familia = df
        else: 
            df_bolsa_familia = pl.concat([df_bolsa_familia, df]) #polars
            # df_bolsa_familia = pd.concat([df_bolsa_familia, df])

        del df
        print(df_bolsa_familia.head())
        print(f'\narquivo {arquivo} processado com sucesso')

    print(f'Dados concatenados com sucesso')

    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA')
        .str.replace(',', '.')
        .cast(pl.Float64)
    )

    #salvando em arquivo parquet
    #instalar biblioteca fastparquet
    print(f'\nsalvando arquivo parker...')
    df_bolsa_familia.write_parquet('./../DADOS/bolsa_familia.parquet')
    print('Arquivo parquet criado com sucesso')
        

    fim = datetime.now()
    print(f'Tempo total {fim - inicio}')
except Exception as e: 
    print(f'Erro ao obter os dados {e}')