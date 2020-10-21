'''
Author:         Namami Shanker
Date:           17/06/2020
Data Source:    https://github.com/CSSEGISandData/COVID-19
About:  This program extracts information of confirmed cases of Covid-19 and total deaths only in US, starting from the date 22-Jan-2020
        upto the latest updation on the GitHub repository from which it extracts the data, which is generally updated daily. Please be 
        informed that in US the clear data about number of patients is not available so that isnt provided by this script.
        
        Thanks for using my script. Below are the states from which it can extract data.


American Samoa
Guam
Northern Mariana Islands
Puerto Rico
Virgin Islands
Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
District of Columbia
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming
Diamond Princess
Grand Princess
'''


import pandas as pd
import time
import datetime
import re

def download_data(state):
    temp = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    raw_confirmed = temp[temp.Province_State == state]
    temp = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
    raw_deaths = temp[temp.Province_State == state]
    return raw_confirmed, raw_deaths

def extract_data(state, raw_confirmed, raw_deaths):
    raw_confirmed = raw_confirmed.iloc[:,11: ]
    lis = []
    for i in raw_confirmed.columns:
        s = raw_confirmed[i].sum()
        dic = {'state':state,'date':i, 'cases_confirmed': s}
        lis.append(dic)
    confirmed = pd.DataFrame(lis)
    raw_deaths = raw_deaths.iloc[:, 12:]
    lis = []
    for i in raw_deaths.columns:
        s = raw_deaths[i].sum()
        lis.append(s)
    lis = pd.Series(lis)
    confirmed['total_deaths'] = lis
    return confirmed

def add_US_deaths(confirmed_commulative):
    raw_total_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    raw_total_deaths = raw_total_deaths[raw_total_deaths['Country/Region'] == 'US']
    raw_total_deaths = raw_total_deaths.iloc[:, 4:]
    lis = []
    for i in raw_total_deaths.columns:
        s = raw_total_deaths[i].sum()
        lis.append(s)
    lis = pd.Series(lis)
    confirmed_commulative['total_US_deaths'] = lis
    return confirmed_commulative

def add_death_ratio(confirmed_commulative):
    death_ratio =confirmed_commulative['total_deaths'] / confirmed_commulative['total_US_deaths']
    death_ratio = death_ratio.fillna(0)
    confirmed_commulative['death_ratio'] = death_ratio
    return confirmed_commulative

def add_recovered_data(confirmed_commulative):
    raw_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    raw_recovered = raw_recovered[raw_recovered['Country/Region']=='US']
    raw_recovered = raw_recovered.iloc[:, 4:]
    lis = []
    for i in raw_recovered.columns:
        s = raw_recovered[i].sum()
        lis.append(s)
    lis = pd.Series(lis)
    confirmed_commulative['total_US_rec'] = lis
    return confirmed_commulative

def add_approx_rec(confirmed_commulative):
    approx_state_rec = confirmed_commulative['death_ratio']*confirmed_commulative['total_US_rec']
    confirmed_commulative['approx_state_rec_total'] = approx_state_rec.round()
    return confirmed_commulative

def cal_new_deaths(confirmed_commulative):
    tot_deaths = confirmed_commulative['total_deaths']
    lis = [0]
    prev_deaths = 0
    for i in tot_deaths[1:]:
        new_deaths = i - prev_deaths
        prev_deaths = i
        lis.append(new_deaths)
    confirmed_commulative['new_deaths'] = lis
    return confirmed_commulative

def main():
    state = 'Louisiana' # input("Enter the name of US state. Please be sure to enter the name exactly same as mentioned in the state list: ")
    
    print('Downloading data. Please wait...')
    raw_confirmed, raw_deaths = download_data(state)

    print('Extracting confirmed cases and deaths...')
    confirmed_commulative = extract_data(state, raw_confirmed, raw_deaths)

    print('Calculating new deaths...')
    confirmed_commulative = cal_new_deaths(confirmed_commulative)

    print('Incorporating totals deaths in US...')
    confirmed_commulative = add_US_deaths(confirmed_commulative)

    print('Calculating death ratio...')
    confirmed_commulative = add_death_ratio(confirmed_commulative)

    print('Adding data of recovered patients...')
    confirmed_commulative = add_recovered_data(confirmed_commulative)

    print('Extrapolating approximate numbers of recovered patient in', state)
    confirmed_commulative = add_approx_rec(confirmed_commulative)

    

    print('Saving data...')
    confirmed_commulative.to_csv('data.csv')

    print('Data downloaded. Exiting.')
    time.sleep(3)


if __name__ == '__main__':
    main()
