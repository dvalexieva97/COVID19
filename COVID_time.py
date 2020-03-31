#Plotting COVID distribution by country in 2020 until March 14th 2020

import pandas as pd
import matplotlib.pyplot as plt

#import .xls table into python
df = pd.read_excel(r'C:\Users\Dia\Documents\UNI\Data Science NBU\semester 2\Data visualization\COVID distribution\COVID_EU.xlsx')
df = df.iloc[:,[0,1,2]]

#print(df)

df["DateRep"] = pd.to_datetime(df["DateRep"])
df = df.loc[(df['DateRep'] >= '2020-02-17') &(df['CountryExp'] != 'Italy')]
#df.rename(columns={'Date':'DateRep', 'Country':'CountryExp'}, inplace = True)
df.columns = ['Date', 'Country', 'Daily cases']
print(df)

df.pivot(index = "Date", columns = "Country", values="Daily cases").plot().legend(bbox_to_anchor=(1, 1))

plt.show()

#df = df.loc[(df['DateRep'] >= '2020-02-17') & (df['column_name'] <= B)]
#df.pivot(index = "DateRep", columns = "CountryExp", values="NewConfCases").plot()
#plt.show()
