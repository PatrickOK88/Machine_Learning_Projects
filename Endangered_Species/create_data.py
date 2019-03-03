# This file will prepare the data in a .csv file that will be used to train the model

import os
import settings
import pandas as pd


# I have noticed some differences in the header names of some of the files, so I think it's best to define them here
def header(df):
    df.columns = ['id_no,N,10,0',
                  'binomial,C,254',
                  'presence,N,5,0',
                  'origin,N,5,0',
                  'seasonal,N,5,0',
                  'compiler,C,200',
                  'year_,N,5,0',
                  'citation,C,254',
                  'source,C,254',
                  'dist_comm,C,254',
                  'island,C,200',
                  'subspecies,C,50',
                  'subpop,C,200',
                  'legend,C,80',
                  'tax_comm,C,250',
                  'kingdom,C,100',
                  'phylum,C,100',
                  'class,C,100',
                  'order_,C,100',
                  'family,C,100',
                  'genus,C,100',
                  'category,C,5',
                  'marine,C,5',
                  'terrestial,C,5',
                  'freshwater,C,5',
                  'SHAPE_Leng,N,19,11',
                  'SHAPE_Area,N,19,11']


def concatenate():
    files = os.listdir(settings.DATA_DIR)
    dfs = []
    for f in files:
        if f.endswith('.csv'):
            df = pd.read_csv(os.path.join(settings.DATA_DIR, f), index_col=None, header=0)
            header(df)

            dfs.append(df)

    final_df = pd.concat(dfs, axis=0, ignore_index=True)

    final_df.to_csv(os.path.join(settings.PROCESSED_DIR, "endangered_species.csv"), sep=',', encoding='utf-8')


if __name__ == "__main__":
    print("***** Starting concatenation *****\n")
    concatenate()
    print("\n***** Completed concatenation *****")
