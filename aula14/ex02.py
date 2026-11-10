import pandas as pd
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

try: 
    inicio = datetime.now()
    print('obtendo dados parquet...')
    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') pandas
    # df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') # polars

    #sacan parquet cria um plano de exdecuçao e nao obtem dados direto
    df_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') #polars leitura preguispça

    #collect: executa o plano de execuçao e traz os dados 
    df_bolsa_familia = df_bolsa_familia.collect()
    print(df_bolsa_familia.head())

    fim = datetime.now()
    print(f'tempo total {fim - inicio}')

except Exception as e: 
    print(f'errou no parquet')

