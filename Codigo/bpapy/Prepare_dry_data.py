import pandas as pd
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
    return new_df

def Get_moisture_in_time(df):
    name = list(df.columns)
    mm = Get_min(df)
    c = 0
    for i in name:
        df[i] = (df[i]-mm)/mm
        c += 1
    return df

def Get_free_moisture(df):
    eq_h = Get_dry_data_info(df)['Equilibrium_moisture']
    df1 = Get_moisture_in_time(df)
    name = list(df.columns)
    c = 0
    for i in name:
        df[i] = df1[i]-eq_h
        c += 1
    return df

def Get_moisture_rate(dff):
    df = dff
    name = list(df.columns)
    print(len(name))
    df1 = list(Get_moisture_in_time(df).iloc[:,0])
    print(len(df1))
    df2 = Get_free_moisture(df)
    eq_h = list(Get_dry_data_info(df)['Equilibrium_moisture'])
    print(len(eq_h))
    #mm = df1 - eq_h
    #c = 0
    #for i in name:
    #    df[i] = df2[i] / mm
    #    c += 1
    return df2.shape