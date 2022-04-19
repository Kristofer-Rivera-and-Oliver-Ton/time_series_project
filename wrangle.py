# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

# visualize 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# working with dates
from datetime import datetime

#important import 
from env import user_name,password,host
import pandas as pd
import numpy as np
import os

#acquire data for the first time
def get_connection(db):
    '''
    Creates a connection URL
    '''
    return f'mysql+pymysql://{user_name}:{password}@{host}/{db}'

def new_superstore_data():
    '''
    Returns zillow into a dataframe
    '''
    sql_query =''' 
    select * from orders 
    join customers using (`Customer ID`)
    join products using(`Product ID`)
    join categories using (`Category ID`)
    join regions using (`Region ID`);
    '''
    df = pd.read_sql(sql_query, get_connection('superstore_db'))
    return df 

def get_superstore_data():
    '''get connection, returns superstore into a dataframe and creates a csv for us'''
    if os.path.isfile('superstore.csv'):
        df = pd.read_csv('superstore.csv', index_col=0)
    else:
        df = new_superstore_data()
        df.to_csv('superstore.csv')
    return df

def date_to_index (df, col_date1, col_date2):
    '''
    takes in a df and a name of the column that is a order date. 
    return a df with the selected column in datetime format  as Index 
    '''
    #convert sale_date to datetime format
    df[col_date1]= pd.to_datetime(df[col_date1])
    df[col_date2]= pd.to_datetime(df[col_date2])
    #set date as index
    df = df.set_index(col_date1).sort_index()
    return df

def prep_superstore (df, col_date1, col_date2):
    '''
    This function will takes in a df and the name of the column (order date).
    Renaming columns, dropping foreign keys and converting data type with the selected column in datetime format as Index, new columns:
    month, year and return dataframe.
    
    '''
    #Using function date_to_index
    df = date_to_index (df, col_date1, col_date2)

    #Converts column names to lower case and changes spaces to underscores
    df.columns = [col.lower().replace(" ","_").replace("-","_") for col in df.columns]

    #create new columns
    df['month'] = df.index.month_name()
    df['year' ] = df.index.year

    # Drop unnecessary foreign keys
    df = df.drop(columns = ['region_id','category_id'])
    return df
