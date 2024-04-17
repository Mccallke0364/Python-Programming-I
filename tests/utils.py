import pandas as pd
import numpy as np

convert= pd.read_csv("gene_id_to_symbol.csv")
def id_converter(ids):
    for id in convert.itertuples():
        if id[1]==ids:
            dict[id[1]]=id[3]
  
