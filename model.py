# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

#important import 
import pandas as pd
from fbprophet import Prophet
import os

def create_model(df, category, datetime_column, variable1, variable2):
    '''
    This function will extract from train data into 3 seperate categories and put them in a dataframe.
    Use prophet as machine learning algorithms to forecast future sales (set 36 months ahead)
    '''
    
    #Extract the data of Office Supplies, technology and furniture
    technology = df.loc[df[category] == 'Technology']
    
    #Drop all columns except the target variables
    technology = technology[[variable1, variable2]]

    #Set index for 3 catergories
    technology = technology.sort_values(datetime_column)
    technology = technology.groupby(datetime_column)[variable1, variable2].sum().reset_index()
    technology = technology.set_index(datetime_column)

    #Get monthly average sales of 3 categories
    monthly_technology_sales = technology[variable1].resample('M').mean()
    monthly_technology_profit = technology[variable2].resample('M').mean()

    #Put 3 catergories in a dataframe
    technology_sales = pd.DataFrame({'Order Date': monthly_technology_sales.index, 'Sales': monthly_technology_sales.values})
    technology_profit = pd.DataFrame({'Order Date': monthly_technology_profit.index, 'Profit': monthly_technology_profit.values})

    #Create model
    technology_sales = technology_sales.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
    technology_sales_model = Prophet(interval_width=0.95)
    technology_sales_model.fit(technology_sales)

    technology_profit = technology_profit.rename(columns={'Order Date': 'ds', 'Profit': 'y'})
    technology_profit_model = Prophet(interval_width=0.95)
    technology_profit_model.fit(technology_profit)
    
    #Prophet has make_future_dataframe propterty that an argument periods (number of periods to forecast forward).
    #Look into five years ahead
    technology_sales_forecast = technology_sales_model.make_future_dataframe(periods = 36, freq = 'MS')
    technology_sales_forecast = technology_sales_model.predict(technology_sales_forecast)

    technology_profit_forecast = technology_profit_model.make_future_dataframe(periods = 36, freq = 'MS')
    technology_profit_forecast = technology_profit_model.predict(technology_profit_forecast)
    
    return technology_sales_model, technology_sales_forecast, technology_profit_forecast, technology_profit_model

class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in 
    Python, i.e. will suppress all print, even if the print originates in a 
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).      

    '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds =  [os.open(os.devnull,os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = [os.dup(1), os.dup(2)]

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0],1)
        os.dup2(self.null_fds[1],2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0],1)
        os.dup2(self.save_fds[1],2)
        # Close all file descriptors
        for fd in self.null_fds + self.save_fds:
            os.close(fd)