import pandas as pd
import numpy as np
import scipy.stats as st

def data_info(df):
    shape = df.shape
    print(f'Database has a total of {shape[0]} rows and {shape[1]} columns')

def desc_stats(df):
    transp = df.transpose()
    df_stats = transp.describe().transpose()
    df_stats['kurtosis'] = st.describe(transp).kurtosis
    df_stats['skewness'] = st.describe(transp).skewness
    df_stats['variance'] = st.describe(transp).variance
    return df_stats

def Get_min(df):
    min_vect = []
    for i in range(df.iloc[:,0].count()):
        mn = df.iloc[i,:].min()
        min_vect.append(mn)
    return min_vect

def Get_dry_data_info(df):
    index = df.index
    new_df = pd.DataFrame(index = index)
    new_df['Wet_weight_sample'] = df.iloc[:,0]
    new_df['Dry_Weigth_sample'] = Get_min(df) 
    new_df['Initial_moisture (%) wb'] = ((new_df['Wet_weight_sample'] - new_df['Dry_Weigth_sample']) / new_df['Wet_weight_sample'])*100
    new_df['Equilibrium_dry_mass'] =  Get_min(df) 
    new_df['Equilibrium_moisture'] = (new_df['Equilibrium_dry_mass'] - new_df['Dry_Weigth_sample']) / new_df['Equilibrium_dry_mass']
    n_df = new_df.copy()
    return n_df

def moisture_in_time(df):
    name = list(df.columns)
    mm = Get_min(df)
    c = 0
    for i in name:
        df[i] = (df[i]-mm)/mm
        c += 1
    return df

def free_moisture(df):
    index = df.index
    ne_df = pd.DataFrame(index = index)
    name = list(df.columns)
    eq_h = Get_dry_data_info(df).iloc[:,4]
    df1 = moisture_in_time(df)
    for i in name:
        ne_df[i] = df1[i]-eq_h
    return ne_df

def moisture_rate(df):
    index = df.index
    n_df = pd.DataFrame(index = index)
    df1 = df.copy()
    name = df.columns
    eq_h = Get_dry_data_info(df).iloc[:,4]
    m_i = moisture_in_time(df).iloc[:,0]
    mm = m_i - eq_h
    df2 = free_moisture(df1)
    for i in name:
        df2[i] = df2[i] / mm
    return df2