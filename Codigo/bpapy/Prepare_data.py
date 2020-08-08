import pandas as pd
import numpy as np
import scipy.stats as st

class prep_dry_data:
    def __init__(self, dff):
        self.df = dff
        self.info_data = f'Database has a total of {self.df.shape[0]} rows and {self.df.shape[1]} columns'

    def desc_stats(self):
        transp = self.df.transpose()
        df_stats = transp.describe().transpose()
        df_stats['kurtosis'] = st.describe(transp).kurtosis
        df_stats['skewness'] = st.describe(transp).skewness
        df_stats['variance'] = st.describe(transp).variance
        return df_stats

    def Get_min(self):
        df = self.df
        min_vect = []
        for i in range(df.iloc[:,0].count()):
            mn = df.iloc[i,:].min()
            min_vect.append(mn)
        return min_vect

    def Get_dry_data_info(self):
        df = self.df
        index = df.index
        new_df = pd.DataFrame(index = index)
        new_df['Wet_weight_sample'] = df.iloc[:,0]
        new_df['Dry_Weigth_sample'] = self.Get_min() 
        new_df['Initial_moisture (%) wb'] = ((new_df['Wet_weight_sample'] - new_df['Dry_Weigth_sample']) / new_df['Wet_weight_sample'])*100
        new_df['Equilibrium_dry_mass'] =  self.Get_min() 
        new_df['Equilibrium_moisture'] = (new_df['Equilibrium_dry_mass'] - new_df['Dry_Weigth_sample']) / new_df['Equilibrium_dry_mass']
        return new_df

    def moisture_in_time(self):
        df = self.df
        df1 = df.copy()
        name = list(df.columns)
        mm = self.Get_min()
        c = 0
        for i in name:
            df1[i] = (df1[i]-mm)/mm
            c += 1
        return df1

    def free_moisture(self):
        df = self.df
        index = df.index
        ne_df = pd.DataFrame(index = index)
        name = list(df.columns)
        eq_h = self.Get_dry_data_info().iloc[:,4]
        df1 = self.moisture_in_time()
        for i in name:
            ne_df[i] = df1[i]-eq_h
        return ne_df

    def moisture_rate(self, method = 'None'):
        meth = method
        df = self.df
        index = df.index
        n_df = pd.DataFrame(index = index)
        df1 = df.copy()
        name = df.columns
        eq_h = self.Get_dry_data_info().iloc[:,4]
        m_i = self.moisture_in_time().iloc[:,0]
        mm = m_i - eq_h
        df2 = self.free_moisture()
        for i in name:
            df2[i] = df2[i] / mm
        if method == 'None':
            return df2
        elif method == 'mean_leng_surf':
            df3 = df2.groupby(['Surfaces', 'Lengths']).mean()
            return df3 #Return a data frame with the mean of the variables Lengths and Surfaces
        elif method == 'mean_leng':
            df4 = df2.groupby(['Lengths']).mean()
            return df4 #Return a data frame with the mean of the variable Lengths
        elif method == 'mean_surf':
            df5 = df2.groupby('Surfaces').mean()
            return df5  #Return a data frame with the mean of the variable Surfaces
        else:
            raise KeyError('Ha ocurrido un problema con el método elegido')

