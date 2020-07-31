import pandas as pd
class Get_dry_data(object):

    def __init__(self, file_location, separator):
        self.location = file_location
        self.separator = separator

    def Import_data(self):
        dff = pd.read_csv(self.location, sep = self.separator)
        return dff

    def Get_index_data(self):
        loc = self.location
        sep = self.separator
        df = self.Import_data()
        dft = df.dtypes
        c = 0
        while dft[c] != 'float64':
            c += 1
        print('Data base has a total of %s Index type columns' %c)
        return c

    def Get_dry_df(self, repeats = None, surfaces = None, lengths = None): 
    # It is required database keep this order: Column1 = Repeats, Column2 = Surfaces, Column3 = Lengths
        df = self.Import_data()
        rep = repeats
        surf = surfaces
        long = lengths

        # Change index Lengths column by lengths names used
        if long != None:     
            h2 = pd.unique(df.iloc[:,0])
            hh2 = list(df.iloc[:,0])
            if len(long) == len(h2):
                for i in range(len(hh2)):
                    if hh2[i] == h2[0]:
                        hh2[i] = long[0]
                    elif hh2[i] == h2[1]:
                        hh2[i] = long[1]
                    elif hh2[i] == h2[2]:
                        hh2[i] = long[2]
                    elif hh2[i] == h2[3]:
                        hh2[i] = long[3]
                    elif hh2[i] == h2[4]:
                        hh2[i] = long[4]
                    elif hh2[i] == h2[5]:
                        hh2[i] = long[5]
                    elif hh2[i] == h2[6]:
                        hh2[i] = long[6]
                    elif hh2[i] == h2[7]:
                        hh2[i] = long[7]
                    elif hh2[i] == h2[8]:
                        hh2[i] = long[8]
                    elif hh2[i] == h2[9]:
                        hh2[i] = long[9]
                    else:
                        hh2[i] = long[10]
            df.iloc[:,0] = hh2
        else:
            pass
            #df.drop(columns=['Lengths'])

        # Change index Surface column by surface names
        if surf != None:
            h = pd.unique(df.iloc[:,1])
            hh = list(df.iloc[:,1])
            if len(surf) == len(h):
                for i in range(len(hh)):
                    if hh[i] == h[0]:
                        hh[i] = surf[0]
                    elif hh[i] == h[1]:
                        hh[i] = surf[1]
                    elif hh[i] == h[2]:
                        hh[i] = surf[2]
                    elif hh[i] == h[3]:
                        hh[i] = surf[3]
                    elif hh[i] == h[4]:
                        hh[i] = surf[4]
                    else:
                        hh[i] = surf[5]
            df.iloc[:,1] = hh
        else:
            pass
            #df.drop(columns=['Surfaces'])

        # Change index Repeats column by repeats names
        if rep != None:
            h1 = pd.unique(df.iloc[:,2])
            hh1 = list(df.iloc[:,2])
            d1 = ['Repeticion {0}'.format(i) for i in range(1,len(h1)+1)]
            if rep == len(h1):
                for i in range(len(hh1)):
                    if hh1[i] == h1[0]:
                        hh1[i] = d1[0]
                    elif hh1[i] == h1[1]:
                        hh1[i] = d1[1]
                    elif hh1[i] == h1[2]:
                        hh1[i] = d1[2]
                    elif hh1[i] == h1[3]:
                        hh1[i] = d1[3]
                    else:
                        hh1[i] = d1[4]
            df.iloc[:,2] = hh1
        else:
            pass
            #df.drop(columns=['Repeats'])

        data = df.columns.to_list()[3:]
        dff = df.groupby([df.columns.to_list()[0], 
        df.columns.to_list()[1], df.columns.to_list()[2]])[data].mean()
        return dff
        
class Get_prox_data():

    def __init__(self, file_location, separator):
        self.location = file_location
        self.separator = separator

    def Import_data(self):
        a = Get_dry_data(self.location, self.separator)
        dff = a.Import_data()
        return dff

    def Get_df_prox(self, repeats = None, biomass = None, essays = None):
        a = Get_dry_data(self.location, self.separator)
        dff = a.Get_dry_df(repeats, biomass, essays)
        return dff

class Get_elem_data():

    def __init__(self, file_location, separator):
        self.location = file_location
        self.separator = separator

    def Import_data(self):
        a = Get_dry_data(self.location, self.separator)
        dff = a.Import_data()
        return dff

    def Get_df_elem(self, repeats = None, biomass = None, essays = None):
        a = Get_dry_data(self.location, self.separator)
        dff = a.Get_dry_df(repeats, biomass, essays)
        return dff