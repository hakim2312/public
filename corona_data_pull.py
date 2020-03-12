# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:32:35 2020

@author: mohamed.tahoon
"""

import pandas as pd


from datetime import date, timedelta, datetime
import time
start = time.time()
start_date_dt = datetime.strptime("2020-01-22", '%Y-%m-%d').date()
end_date_dt = (datetime.now() - timedelta(1)).date()


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


df_tot = pd.DataFrame()
for target_date in daterange(start_date_dt, end_date_dt+ timedelta(1)):
    df = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'.
                     format(datetime.strftime(target_date, '%m-%d-%Y')))
    df["data_date"]=datetime.strftime(target_date, '%Y-%m-%d')
    df_tot = pd.concat([df, df_tot])
    
    
print(df_tot.head(10))
