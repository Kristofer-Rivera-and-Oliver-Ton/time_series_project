# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

#important import 
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

def create_model(df, category, datetime_column, target = 'sales'):
    '''
    This function will extract from train data into 3 seperate categories and put them in a dataframe.
    Use prophet as machine learning algorithms to forecast future sales (set 5 years ahead)
    '''
    
    #Extract the data of Office Supplies, technology and furniture
    office_supplies = df.loc[df[category] == 'Office Supplies']
    furniture = df.loc[df[category] == 'Furniture']
    technology = df.loc[df[category] == 'Technology']
    
    #Drop all columns except the target variables
    office_supplies = office_supplies[[target]]
    furniture = furniture[[target]]
    technology = technology[[target]]

    #Set index for 3 catergories
    office_supplies = office_supplies.sort_values(datetime_column)
    office_supplies = office_supplies.groupby(datetime_column)[target].sum().reset_index()
    office_supplies = office_supplies.set_index(datetime_column)

    furniture = furniture.sort_values(datetime_column)
    furniture = furniture.groupby(datetime_column)[target].sum().reset_index()
    furniture = furniture.set_index(datetime_column)

    technology = technology.sort_values(datetime_column)
    technology = technology.groupby(datetime_column)[target].sum().reset_index()
    technology = technology.set_index(datetime_column)

    #Get monthly average sales of 3 categories
    monthly_office = office_supplies[target].resample('M').mean()
    monthly_furniture = furniture[target].resample('M').mean()
    monthly_technology = technology[target].resample('M').mean()

    #Put 3 catergories in a dataframe
    furniture = pd.DataFrame({'Order Date':monthly_furniture.index, 'Sales':monthly_furniture.values})
    office = pd.DataFrame({'Order Date': monthly_office.index, 'Sales': monthly_office.values})
    technology = pd.DataFrame({'Order Date': monthly_technology.index, 'Sales': monthly_technology.values})

    #Create model
    furniture = furniture.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
    furniture_model = Prophet(interval_width = 0.95)
    furniture_model.fit(furniture)

    office = office.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
    office_model = Prophet(interval_width=0.95)
    office_model.fit(office)

    technology = technology.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
    technology_model = Prophet(interval_width=0.95)
    technology_model.fit(technology)
    
    #Prophet has make_future_dataframe propterty that an argument periods (number of periods to forecast forward).
    #Look into five years ahead
    furniture_forecast = furniture_model.make_future_dataframe(periods = 48, freq = 'MS')
    furniture_forecast = furniture_model.predict(furniture_forecast)

    office_forecast = office_model.make_future_dataframe(periods = 48, freq = 'MS')
    office_forecast = office_model.predict(office_forecast)

    technology_forecast = technology_model.make_future_dataframe(periods = 48, freq = 'MS')
    technology_forecast = technology_model.predict(technology_forecast)
    
    return furniture_model, office_model, technology_model, furniture_forecast, office_forecast, technology_forecast
