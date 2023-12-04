
import pandas as pd
import numpy as np
def run_theory(time_serie, threshold=-1): # The spi threshold for drought it's -1.

    # Create a dataframe with time_serie and mask the values less than threshold
    dataBase = pd.DataFrame({'time_serie': time_serie}).assign(
        masked = lambda x: np.where(x['time_serie'] >= threshold, 1, 0))

    # Add the index and the reverse index
    dataBase = dataBase.assign(index = dataBase['masked'].cumsum(),
                               index_rev = (abs(dataBase['masked']-1)).cumsum())

    # Compute Duration, Severity and Intensity
    df1 = (dataBase.loc[dataBase['masked'] == 0]
            .groupby('index')
            .apply(lambda x: pd.DataFrame({'drought': pd.Series(x.shape[0], index=[0]),
                                           'severity': pd.Series(abs(x['time_serie'].sum()), index=[0]),
                                           'intensity': pd.Series(abs(x['time_serie'].sum())/x.shape[0], index=[0]),
                                           'date_ini': pd.Series(x.index[0], index=[0]),
                                           'date_fin': pd.Series(x.index[-1], index=[0])}))
            .reset_index(drop=True))

    # Compute Interarrival
    Int = (dataBase.loc[dataBase['masked'] != 0]
       .groupby('index_rev')
       .apply(lambda x: pd.DataFrame({'Int': x.shape[0]}, index=[x.name]))
       .values.flatten())
    
    # first condition
    if dataBase['masked'][0] == 1:
        Int = Int[1:]

    # second condition
    if dataBase['masked'].iloc[-1] == 1:
        Int = Int + df1['D']
    else:
        n = np.append(Int, 0) + df1['D']
        Int = n[:-1]
    
    # reorganize to build the dataframe, as all data must be the same size
    a = len(df1['date_ini']) - len(Int)
    new_int = np.append(Int, np.full(a,np.nan))

    # return the dataframe
    return pd.DataFrame({'Duration': df1['drought'].tolist(),
            'Severity': df1['severity'].tolist(),
            'Intensity': df1['intensity'].tolist(),
            'Date_ini_drought': df1['date_ini'].astype(str).tolist(),
            'Date_fin_drought': df1['date_fin'].astype(str).tolist(),
            'Interarrival': new_int.tolist()})
