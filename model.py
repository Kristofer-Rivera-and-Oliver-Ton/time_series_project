# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

#important import 
import pandas as pd
from fbprophet import Prophet

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
