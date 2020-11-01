import pandas as pd

df = pd.read_csv('test')
sum= 0
for label, row in df.iterrows():
    if (df['OFFICE_LOCATION'] == 'NORTHERN CALIFORNIA' || df['OFFICE_LOCATION'] == df['SOUTHERN CALIFORNIA']):
        if (df['EXISTING_DEBT'] == True):
            sum += 1
print(sum)
