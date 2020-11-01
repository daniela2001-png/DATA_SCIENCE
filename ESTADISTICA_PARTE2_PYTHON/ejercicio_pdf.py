import pandas as pd

df = pd.read_csv('test')
sum= 0
for label, row in df.iterrows():
    if (df['OFFICE_LOCATIO'] == 'NORTHERN CALIFORNIA' OR  'SOUTHERN CALIFORNIA'):
        if (df[] == True):
            sum += 1
print(sum)