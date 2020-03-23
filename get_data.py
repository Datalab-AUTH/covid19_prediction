import urllib.request
from datetime import datetime, timedelta, time
import datetime as dt
import pandas as pd
import pickle

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


if __name__ == "__main__":
    get_ecdc_data()