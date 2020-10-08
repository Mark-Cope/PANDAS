import pandas as pd

file_object = open("Holiday_Schedule_Ranking_2019.csv",'r')

data = pd.read_csv(file_object, index_col = 0).T

file_object.close()

file_object = open("Holiday_Schedule_Ranking_2019.csv",'r')

schedule = pd.read_csv(file_object, index_col= 0)

for c in schedule.columns:
    schedule[c].values[:] = 0
    
    
data['col_sum'] = data.apply(lambda x:x.sum(), axis = 1)

data = data.sort_values(by = 'col_sum', ascending = False)

data = data.T

for date in data.columns:
    date_series = data[date].nsmallest(13, keep = 'all')
    for emp in date_series.index.values:
        pref = data[date].loc[emp]
        if ((schedule[date].sum() < 3) and (schedule.loc[emp].sum() < 2)):
            schedule.loc[emp][date] = pref

schedule.replace(0,'', inplace = True)
schedule.to_csv('final_schedule.csv')

print('Done')

