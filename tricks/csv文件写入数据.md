```python3
with open('D:\ALI\Metro_testA\\ansplus.csv') as f:
   file.write('stationID'+','+'startTime'+','+'endTime'+','+'inNums'+','+'outNums'+'\n')
   for i in range(len(df)):
      file.write(str(df1['stationID'][i])+','+df1['startTime'][i]+','+df1['endTime'][i]+','+str(df['inNums'][i])+','+str(df['outNums'][i])+'\n')

```
