import urllib.request
from datetime import datetime, timedelta, time
import datetime as dt
import pandas as pd
import numpy as np

def get_ecdc_data():
    datetimeToday = datetime.today()
    date = datetimeToday.date() #current day
    time = datetimeToday.time() #current time
    yesterday = date - timedelta(1) #day time yesterday
    yesterday = str(yesterday) #day yesterday
    timeFilter = dt.time(10, 00, 00) #time that data are uploaded
    filename = 'data/ecdcdata.csv'
    if time<timeFilter:
        print ("...getting yesterday's results...")
        try:
            url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+yesterday+'.xls'
            urllib.request.urlretrieve(url, filename)
            print ('downloaded yesterdays xls')
        except:
            url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+yesterday+'.xlsx'
            urllib.request.urlretrieve(url, filename)
            print ('downloaded yesterdays xlsx')
    else:
        print ("...getting today's results...")
        try:
            url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+str(date)+'.xls'
            urllib.request.urlretrieve(url, filename)
        except:
            try:
                url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+str(date)+'.xlsx'
                urllib.request.urlretrieve(url, filename)
            except:
                print ('no data yet')


def merge_data():
    """
    Merges 3 datasets
    """
    ecdc = pd.read_excel('data/ecdcdata.csv', converters={'GeoId':str})
    oecd = pd.read_csv('data/oecd_data.csv')
    world_bank = pd.read_csv('data/world_bank_data.csv', encoding='cp1252')

    # convert countries to lowercase
    oecd['Countries and territories'] = [c.lower() for c in oecd['Countries and territories']]
    ecdc['Countries and territories'] = [c.lower() for c in ecdc['Countries and territories']]
    world_bank['Countries and territories'] = [c.lower() for c in world_bank['Countries and territories']]

    summaries = ecdc.groupby(['Countries and territories']).agg({'Cases':  np.sum, 'Deaths': np.sum}).reset_index()
    merged = pd.merge(summaries, oecd, on="Countries and territories", how='left') # keep all countries in ecdc data

    # remove whitespaces
    merged['Countries and territories'] = [c.strip() for c in merged['Countries and territories']]
    world_bank['Countries and territories'] = [c.lower().strip() for c in world_bank['Countries and territories']]

    merged = pd.merge(merged, world_bank, on="Countries and territories", how='left') # keep all countries in ecdc data
    merged.to_csv('data/merged_data.csv', index=False)

if __name__ == "__main__":
    get_ecdc_data()
    merge_data()